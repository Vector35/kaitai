import audioop
import inspect
import io
import os
import re
import enum
import types
import importlib
from typing import Optional

from binaryninja import BinaryView
from kaitaistruct import *

#------------------------------------------------------------------------------
# Kaitai IO Wrapper
#------------------------------------------------------------------------------

# wraps a BinaryView into an "IO" that KaitaiStream can use
#
# now Kaitai can parse directly from the BinaryView and we can avoid making a
# potentially giant copy of the file contents just for kaitai parsing
#
class KaitaiBinaryViewIO:
    def __init__(self, binary_view: BinaryView):
        # TODO: Why does it need to be a raw view type?
        assert binary_view.view_type == 'Raw'
        self.binary_view = binary_view
        self.position = 0

    def seek(self, offs: int, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.position = offs
        elif whence == io.SEEK_CUR:
            self.position += offs
        elif whence == io.SEEK_END:
            self.position = self.binary_view.length
        else:
            raise Exception(f'unknown whence in seek(): {whence}')
        return self.position

    def tell(self):
        return self.position

    def read(self, length=None):
        # if no length is given (eg: see read_bytes_full() in kaitaistruct.py)
        if length is None:
            length = self.binary_view.length - self.position
        data = self.binary_view.read(self.position, length)
        self.position += length
        return data

    def close(self):
        pass


#------------------------------------------------------------------------------
# id and parse
#------------------------------------------------------------------------------

# Return the name of the kaitai module to service this data
def infer_kaitai_module(sample: Optional[bytes], length: int = 0, fpath: Optional[str] = None):
    # if no sample given, but path to file is, take sample
    if sample is None and fpath:
        length = os.path.getsize(fpath)
        with open(fpath, 'rb') as fp:
            sample = fp.read(min(16, length))

    result = None

    # pad to 16 bytes
    sample = sample + b'\x00' * (16 - len(sample))

    # can we infer the module from the file's data?
    if sample[0:4] == b'\x7fELF':
        result = 'elf'
    elif sample[0:4] in [b'\xfe\xed\xfa\xce', b'\xce\xfa\xed\xfe', b'\xfe\xed\xfa\xcf', b'\xcf\xfa\xed\xfe']:
        result = 'mach_o'
    elif sample[0:2] == b'MZ':
        result = 'microsoft_pe'
    elif sample[0:8] == b'\x89PNG\x0d\x0a\x1a\x0a':
        result = 'png'
    elif sample[2:11] == b'\xFF\xe0\x00\x10JFelif\x00':
        result = 'jpeg'
    elif sample[0:4] == b'Gelif8':
        result = 'gelif'
    elif sample[0:6] in [b'GIF89a', b'GIF87a']:
        result = 'gif'
    elif sample[0:2] in [b'BM', b'BA', b'CI', b'CP', b'IC', b'PT'] and struct.unpack('<I', sample[2:6])[0] == length:
        result = 'bmp'
    elif sample[0:2] == b'PK' and sample[2:4] in [b'\x01\x02', b'\x03\x04', b'\x05\x06']:
        result = 'zip'
    elif sample[0:6] == b'Rar!\x1a\x07':
        result = 'rar'
    elif sample[0:2] == b'\x1f\x8b' and sample[2:3] == b'\x08':
        result = 'gzip'
    elif sample[0:4] == b'dex\x0a':
        result = 'dex'

    # if not, make best guess on extension
    if not result and fpath:
        lookup = {'.png': 'png', '.jpg': 'jpeg', '.jpeg': 'jpeg', '.gif': 'gif',
                  '.bmp': 'bmp', '.zip': 'zip', '.rar': 'rar',
                  '.gz': 'gzip'}
        _, ext = os.path.splitext(fpath)
        result = lookup.get(ext)

    return result


REPO_IN_PYTHON_PATH = False


def ks_import_class(module_name: str):
    # TODO: Remove this for something not completely insane
    global REPO_IN_PYTHON_PATH
    if not REPO_IN_PYTHON_PATH:
        this_file = inspect.stack()[0][1]
        this_dir = os.path.dirname(this_file)
        repo_dir = os.path.join(this_dir, '.')
        sys.path.append(repo_dir)
        REPO_IN_PYTHON_PATH = True

    class_ref = None
    try:
        # TODO: The formats module here needs to be not relative
        module = importlib.import_module(f'formats.{module_name}')
        class_name = ''.join(map(lambda x: x.capitalize(), module_name.split('_')))
        class_ref = getattr(module, class_name)
    except ModuleNotFoundError as e:
        print(f'ERROR: importing kaitai module {module_name} {e}')
        pass
    except AttributeError as e:
        print(f'ERROR: importing kaitai module {module_name} {e}')
        pass
    return class_ref


def parse_file_path(file_path: str, module_name: Optional[str] = None) -> Optional[KaitaiStruct]:
    if not module_name:
        module_name = infer_kaitai_module(None, 0, file_path)

    ks_class = ks_import_class(module_name)
    if not ks_class:
        print(f'ERROR: importing {module_name} to service {file_path}')
        return None

    parsed = ks_class.from_file(file_path)
    parsed._read()
    exercise_re(parsed)

    return parsed


def parse_io_view(io_view: KaitaiBinaryViewIO, module_name: Optional[str] = None) -> Optional[KaitaiStruct]:
    io_view.seek(0, io.SEEK_END)
    length = io_view.tell()

    if not module_name:
        io_view.seek(0, io.SEEK_SET)
        module_name = infer_kaitai_module(io_view.read(16), length)

    io_view.seek(0, io.SEEK_SET)
    ks_class = ks_import_class(module_name)
    if not ks_class: return None

    parsed = None
    try:
        io_view.seek(0, io.SEEK_SET)
        parsed = ks_class.from_io(io_view)
        parsed._read()
        exercise_re(parsed)
    except Exception as e:
        print(f'ERROR: parse_io_view(): kaitai module {module_name} threw exception {e}, check file type')
        parsed = None

    return parsed


#------------------------------------------------------------------------------
# misc
#------------------------------------------------------------------------------

# access all fields that may be properties, which could compute internal results
# (often '_m_XXX' fields)
#
# mark "exercised" kaitai structs with the _exercised attribute
def exercise_re(kt_struct: KaitaiStruct):
    queue = []
    for entry in dir(kt_struct):
        try:
            attr = getattr(kt_struct, entry, False)
            if isinstance(attr, KaitaiStruct) and not getattr(attr, '_exercised', False):
                setattr(attr, '_exercised', True)
                queue.append(attr)
        except AttributeError:
            pass
    for attr in queue:
        exercise_re(attr)


#------------------------------------------------------------------------------
# Qt/Kaitai OOP
#------------------------------------------------------------------------------

class NodeType(enum.Enum):
    NORMAL = 0
    ARRAY = 1
    LEAF = 2


# why subclass?
# - override "<" to get sorting to work right
# - centralized location to modify field names and labels (eg: remove '_m_')

class TreeNode:
    def __init__(self, type_):
        self.type_ = type_
        self.name = None
        self.value = None  # string
        self.start = None  # int
        self.end = None  # int
        self.children = []
        self.io_size = None

    def __str__(self):
        result = ''

        if self.start is not None and self.end is not None:
            result += f' [{self.start:08X},{self.end:08X})'
        else:
            result += f' [{self.start}, {self.end})'

        result += ' ' + self.name

        if self.value:
            result += f' value=\'{self.value}\''

        return result


#------------------------------------------------------------------------------
# build tree
#------------------------------------------------------------------------------

def build_tree_re(kt_struct: KaitaiStruct):
    node = TreeNode(NodeType.NORMAL)

    field_names = list(kt_struct._debug.keys())
    field_names = [x[3:] if x.startswith('_m_') else x for x in field_names]
    for field_name in field_names:
        # sometimes X._debug will contain an entry for an attribute Y and X.Y doesn't exist ::shrug::
        if not hasattr(kt_struct, field_name):
            continue

        attr = getattr(kt_struct, field_name)

        # CASE0: attribute is a KaitaiStruct
        if isinstance(attr, KaitaiStruct):
            child = build_tree(attr)
            populate_child(kt_struct, field_name, None, child)
            node.children.append(child)

        # CASE1: attribute is a list
        elif isinstance(attr, list):
            child = TreeNode(NodeType.ARRAY)
            populate_child(kt_struct, field_name, None, child)
            node.children.append(child)

            # grandchildren
            for i in range(len(attr)):
                gc_name = f'{field_name}[{i}]'
                if isinstance(attr[i], KaitaiStruct):
                    grandchild = build_tree(attr[i])
                else:
                    grandchild = create_leaf(gc_name, attr[i])
                populate_child(kt_struct, gc_name, None, grandchild)
                child.children.append(grandchild)

        # CASE2: attribute is primitive
        else:
            child = create_leaf(field_name, attr)
            populate_child(kt_struct, field_name, None, child)
            node.children.append(child)

    return node


def build_tree(kt_struct: KaitaiStruct):
    tree = build_tree_re(kt_struct)
    tree.name = 'root'
    tree.start = 0
    tree.end = kt_struct._io.size()
    normalize_offsets(tree)
    return tree


def create_leaf(field_name, obj):
    obj_ty = type(obj)

    if obj_ty == types.FunctionType:
        return None
    elif isinstance(obj, type):
        return None
    elif hasattr(obj, '__call__'):
        return None

    field_value = None

    if isinstance(obj, str) or isinstance(obj, bytes):
        if len(obj) > 8:
            field_value = str(repr(obj[0:8])) + '...'
        else:
            field_value = repr(obj)
    elif isinstance(obj, int):
        field_value = '0x%X (%d)' % (obj, obj)
    elif isinstance(obj, bool):
        field_value = '%s' % obj
    elif str(obj_ty).startswith('<enum '):
        field_value = '%s' % obj
    else:
        pass

    if field_value:
        node = TreeNode(NodeType.LEAF)
        node.name = field_name
        node.value = field_value
        return node
    else:
        return None


def populate_child(kt_struct: KaitaiStruct, field_name: str, field_value: Optional[str], node: TreeNode):
    node.name = field_name

    if field_value:
        node.value = field_value

    # name like "foo[5]"
    if m := re.match(r'(.*)\[(\d+)', field_name):
        fnbase = m.group(1)
        fnidx = int(m.group(2))
        arr_info = kt_struct._debug[fnbase].get('arr', None) or \
                   kt_struct._debug['_m_' + fnbase].get('arr', None)
        start, end = arr_info[fnidx]['start'], arr_info[fnidx]['end']
    # name like "foo"
    else:
        start = kt_struct._debug[field_name].get('start', None)
        if start is None:
            start = kt_struct._debug['_m_' + field_name].get('start', None)

        end = kt_struct._debug[field_name].get('end', None)
        if end is None:
            end = kt_struct._debug['_m_' + field_name].get('end', None)

    if start is not None:
        node.start = start
    if end is not None:
        node.end = end


def normalize_offsets(node, delta=0):
    if node.start is None or node.end is None:
        return
    if node.children and node.children[0].start is None:
        return

    base = node.start

    node.start += delta
    node.end += delta

    # abort on erroneous case
    if node.children and base < node.children[0].start:
        return

    # base >= child.start
    delta2 = 0 if not node.children else base - node.children[0].start

    for child in node.children:
        normalize_offsets(child, delta + delta2)
