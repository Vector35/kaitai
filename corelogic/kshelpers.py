#!/usr/bin/env python

import io
import os
import re
import sys
import enum
import types
import struct
import inspect
import binascii
import importlib
import collections

import kaitaistruct

#------------------------------------------------------------------------------
# id and parse
#------------------------------------------------------------------------------

# return the name of the kaitai module to service this data
#
# dsample:   str        data sample
# length:    int        total length of data
def data_id(sample, length):
    result = None
    #print('data_id() here with sample: %s' % repr(sample))

    # pad to 16 bytes
    sample = sample + b'\x00'*(16-len(sample))

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
    elif sample[0:2] in [b'BM', b'BA', b'CI', b'CP', b'IC', b'PT'] and struct.unpack('<I', sample[2:6])[0]==length:
        result = 'bmp'
    elif sample[0:2] == b'PK' and sample[2:4] in [b'\x01\x02', b'\x03\x04', b'\x05\x06']:
        result = 'zip'
    elif sample[0:6] == b'Rar!\x1a\x07':
        result = 'rar'
    elif sample[0:2] == b'\x1f\x8b' and sample[2:3]==b'\x08':
        result = 'gzip'
    elif sample[0:4] == b'dex\x0a':
        result = 'dex'

    #print('data_id() returning \'%s\'' % result)
    return result

def file_id(fpath):
    with open(fpath, 'rb') as fp:
        return data_id(fp.read(16), os.path.getsize(fpath))

# see notes in README-developers.md
repo_in_python_path = False
def ks_import_class(moduleName):
    print(f'ks_import_class({moduleName})')

    global repo_in_python_path
    if not repo_in_python_path:
        this_file = inspect.stack()[0][1]
        this_dir = os.path.dirname(this_file)
        repo_dir = os.path.join(this_dir, '..')
        sys.path.append(repo_dir)
        repo_in_python_path = True

    if not moduleName:
        print(f'ERROR: ks_import_class given module name: {moduleName}')
        return None

    class_ref = None
    try:
        #print(f'INFO: importlib.import_module({moduleName})')
        module = importlib.import_module('formats.' + moduleName)
        class_name = ''.join(map(lambda x: x.capitalize(), moduleName.split('_')))
        class_ref = getattr(module, class_name)
    except AttributeError as e:
        print('ERROR: importing kaitai module %s' % moduleName)
        pass

    return class_ref

def parseFpath(fpath, ksModuleName=None):
    print(f'parseFpath({fpath}, {ksModuleName})')

    if not ksModuleName:
        ksModuleName = file_id(fpath)
    #print('parseFpath() using kaitai format: %s' % ksModuleName)

    ks_class = ks_import_class(ksModuleName)
    if not ks_class:
        print(f'ERROR: importing {ksModuleName} to service {fpath}')
        return None

    parsed = None
    #try:
    parsed = ks_class.from_file(fpath)
    parsed._read()
    exercise_re(parsed)

    #except Exception as e:
    #    print('parseFpath(): kaitai module %s threw exception, check file type' % ksModuleName)
    #    parsed = None

    return parsed

def parseData(data, ksModuleName=None):
    print(f'parseData(data, {ksModuleName})')

    if not ksModuleName:
        ksModuleName = data_id(data, len(data))
    #print('parseData() using kaitai format: %s' % ksModuleName)

    ks_class = ks_import_class(ksModuleName)
    if not ks_class:
        print(f'ERROR: importing {ksModuleName} to service {fpath}')
        return None

    parsed = None
    try:
        parsed = ks_class.from_bytes(data)
        parsed._read()
        exercise_re(parsed)
    except Exception as e:
        print('parseData(): kaitai module %s threw exception, check file type' % ksModuleName)
        parsed = None

    return parsed

def parseIo(ioObj, ksModuleName=None):
    print(f'parseIo(ioObj, {ksModuleName})')

    ioObj.seek(0, io.SEEK_END)
    length = ioObj.tell()

    if not ksModuleName:
        ioObj.seek(0, io.SEEK_SET)
        ksModuleName = data_id(ioObj.read(16), length)
    #print('parseIo() using kaitai format: %s' % ksModuleName)

    ioObj.seek(0, io.SEEK_SET)
    ks_class = ks_import_class(ksModuleName)
    if not ks_class: return None

    parsed = None
    try:
        ioObj.seek(0, io.SEEK_SET)
        parsed = ks_class.from_io(ioObj)
        parsed._read()
        exercise_re(parsed)
    except Exception as e:
        print('parseIo(): kaitai module %s threw exception %s, check file type' % (ksModuleName, str(e)))
        parsed = None

    return parsed

#------------------------------------------------------------------------------
# misc
#------------------------------------------------------------------------------

# access all fields that may be properties, which could compute internal results
# (often '_m_XXX' fields)
#
# mark "exercised" kaitai structs with the _exercised attribute
def exercise_re(ksobj):
    queue = []

    for aname in dir(ksobj):
        try:
            attr = getattr(ksobj, aname, False)
            if isinstance(attr, kaitaistruct.KaitaiStruct) and not getattr(attr, '_exercised', False):
                setattr(attr, '_exercised', True)
                queue.append(attr)
        except AttributeError:
            pass

    #print('recursion queue: ' + str(queue))
    for attr in queue:
        exercise_re(attr)

#------------------------------------------------------------------------------
# Kaitai IO Wrapper
#------------------------------------------------------------------------------

# wraps a BinaryView into an "IO" that KaitaiStream can use
#
# now Kaitai can parse directly from the BinaryView and we can avoid making a
# potentially giant copy of the file contents just for kaitai parsing
#
class KaitaiBinaryViewIO:
    def __init__(self, binaryView):
        self.binaryView = binaryView
        self.position = 0

    def seek(self, offs, whence=io.SEEK_SET):
        #print('seek(0x%X, %d)' % (offs, whence))
        if whence == io.SEEK_SET:
            self.position = offs
        elif whence == io.SEEK_CUR:
            self.position += offs
        elif whence == io.SEEK_END:
            self.position = len(self.binaryView)
        else:
            raise Exception('unknown whence in seek(): %d' % whence)

    def tell(self):
        #print('tell() returning 0x%X' % (self.position))
        return self.position

    def read(self, length=None):
        # if no length is given (eg: see read_bytes_full() in kaitaistruct.py)
        if length == None:
            length = len(self.binaryView) - self.position

        #print('read(%d) (starting at position: 0x%X)' % (length, self.position))
        data = self.binaryView.read(self.position, length)
        self.position += length
        return data

    def close(self):
        pass

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

class TreeNode():
    def __init__(self, type_):
        self.type_ = type_

        self.name = None
        self.value = None    # string

        self.start = None    # int
        self.end = None      # int

        self.children = []

        self.io_size = None

    def __str__(self):
        result = ''

        if self.start != None and self.end != None:
            result += f' [{self.start:08X},{self.end:08X})'
        else:
            result += f' [{self.start}, {self.end})'

        #result += f' ({self.type_.name[0]})'

        result += ' '+self.name

        if self.value:
            result += f' value=\'{self.value}\''

        return result

#------------------------------------------------------------------------------
# build tree
#------------------------------------------------------------------------------

def build_tree_re(ksobj):
    assert isinstance(ksobj, kaitaistruct.KaitaiStruct)

    node = TreeNode(NodeType.NORMAL)

    field_names = list(ksobj._debug.keys())
    field_names = [x[3:] if x.startswith('_m_') else x for x in field_names]
    for field_name in field_names:
        # sometimes X._debug will contain an entry for an attribute Y and X.Y doesn't exist ::shrug::
        if not hasattr(ksobj, field_name):
            continue

        attr = getattr(ksobj, field_name)

        # CASE0: attribute is a KaitaiStruct
        if isinstance(attr, kaitaistruct.KaitaiStruct):
            child = build_tree(attr)
            populate_child(ksobj, field_name, None, child)
            node.children.append(child)

        # CASE1: attribute is a list
        elif isinstance(attr, list):
            child = TreeNode(NodeType.ARRAY)
            populate_child(ksobj, field_name, None, child)
            node.children.append(child)

            # grandchildren
            for i in range(len(attr)):
                gc_name = f'{field_name}[{i}]'
                if isinstance(attr[i], kaitaistruct.KaitaiStruct):
                    grandchild = build_tree(attr[i])
                else:
                    grandchild = create_leaf(gc_name, attr[i])
                populate_child(ksobj, gc_name, None, grandchild)
                child.children.append(grandchild)

        # CASE2: attribute is primitive
        else:
            child = create_leaf(field_name, attr)
            populate_child(ksobj, field_name, None, child)
            node.children.append(child)

    return node

def build_tree(ksobj):
    tree = build_tree_re(ksobj)
    tree.name = 'root'
    tree.start = 0
    tree.end = ksobj._io.size()
    normalize_offsets(tree)
    return tree

def create_leaf(field_name, obj):
    objtype = type(obj)

    if objtype == types.FunctionType:
        #print('reject %s because its a function' % field_name)
        return None
    elif isinstance(obj, type):
        #print('reject %s because its a type' % field_name)
        return None
    elif hasattr(obj, '__call__'):
        #print('reject %s because its a callable' % field_name)
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
        field_value = '%s' % (obj)
    elif str(objtype).startswith('<enum '):
        field_value = '%s' % (obj)
    else:
        #print('field %s has type: -%s-' % (field_name,str(objtype)))
        pass

    if field_value:
        node = TreeNode(NodeType.LEAF)
        node.name = field_name
        node.value = field_value
        return node
    else:
        #print('rejected leaf node to %s' % field_name)
        #print(obj)
        #print(type(obj))
        return None

# ARG                TYPE                    NOTES
# --------           -------                 -------
# ksobj:             KaitaiStruct            the current one we're on
# field_name:        string                  actual field name inside the kaitai struct
# field_value:       string                  value used in the tree view
# node:              TreeNode                the item to which we want to imprint(start/end)
def populate_child(ksobj, field_name, field_value, node):
    node.name = field_name

    if field_value:
        node.value = field_value

    # name like "foo[5]"
    if m := re.match(r'(.*)\[(\d+)\]', field_name):
        fnbase = m.group(1)
        fnidx = int(m.group(2))
        arr_info = ksobj._debug[fnbase].get('arr', None) or \
                   ksobj._debug['_m_'+fnbase].get('arr', None)
        start, end = arr_info[fnidx]['start'], arr_info[fnidx]['end']
    # name like "foo"
    else:
        start = ksobj._debug[field_name].get('start', None)
        if start == None:
            start = ksobj._debug['_m_'+field_name].get('start', None)

        end = ksobj._debug[field_name].get('end', None)
        if end == None:
            end = ksobj._debug['_m_'+field_name].get('end', None)

    if start != None:
        node.start = start
    if end != None:
        node.end = end

def normalize_offsets(node, delta=0):
    if node.start == None or node.end == None:
        return
    if node.children and node.children[0].start == None:
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
        normalize_offsets(child, delta+delta2)
