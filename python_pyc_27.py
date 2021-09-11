# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class PythonPyc27(KaitaiStruct):
    """Python interpreter runs .py files in 2 step process: first, it
    produces bytecode, which it then executes. Translation of .py source
    into bytecode is time-consuming, so Python dumps compiled bytecode
    into .pyc files, to be reused from cache at later time if possible.
    
    .pyc file is essentially a raw dump of `py_object` (see `body`) with
    a simple header prepended.
    """

    class Version(Enum):
        v15 = 20121
        v16 = 50428
        v20 = 50823
        v21 = 60202
        v22 = 60717
        v23_a0 = 62011
        v23_a0b = 62021
        v24_a0 = 62041
        v24_a3 = 62051
        v24_b1 = 62061
        v25_a0 = 62071
        v25_a0b = 62081
        v25_a0c = 62091
        v25_a0d = 62092
        v25_b3 = 62101
        v25_b3b = 62111
        v25_c1 = 62121
        v25_c2 = 62131
        v26_a0 = 62151
        v26_a1 = 62161
        v27_a0 = 62171
        v27_a0b = 62181
        v27_a0c = 62191
        v27_a0d = 62201
        v27_a0e = 62211
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.version_magic = KaitaiStream.resolve_enum(PythonPyc27.Version, self._io.read_u2le())
        self.crlf = self._io.read_u2le()
        self.modification_timestamp = self._io.read_u4le()
        self.body = PythonPyc27.PyObject(self._io, self, self._root)

    class CodeObject(KaitaiStruct):

        class FlagsEnum(Enum):
            has_args = 4
            has_kwargs = 8
            generator = 32
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.arg_count = self._io.read_u4le()
            self.local_count = self._io.read_u4le()
            self.stack_size = self._io.read_u4le()
            self.flags = KaitaiStream.resolve_enum(PythonPyc27.CodeObject.FlagsEnum, self._io.read_u4le())
            self.code = PythonPyc27.Assembly(self._io, self, self._root)
            self.consts = PythonPyc27.PyObject(self._io, self, self._root)
            self.names = PythonPyc27.PyObject(self._io, self, self._root)
            self.var_names = PythonPyc27.PyObject(self._io, self, self._root)
            self.free_vars = PythonPyc27.PyObject(self._io, self, self._root)
            self.cell_vars = PythonPyc27.PyObject(self._io, self, self._root)
            self.filename = PythonPyc27.PyObject(self._io, self, self._root)
            self.name = PythonPyc27.PyObject(self._io, self, self._root)
            self.first_line_no = self._io.read_u4le()
            self.lnotab = PythonPyc27.PyObject(self._io, self, self._root)


    class Assembly(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.string_magic = self._io.read_bytes(1)
            if not self.string_magic == b"\x73":
                raise kaitaistruct.ValidationNotEqualError(b"\x73", self.string_magic, self._io, u"/types/assembly/seq/0")
            self.length = self._io.read_u4le()
            self._raw_items = self._io.read_bytes(self.length)
            _io__raw_items = KaitaiStream(BytesIO(self._raw_items))
            self.items = PythonPyc27.OpArgs(_io__raw_items, self, self._root)


    class OpArg(KaitaiStruct):

        class OpCodeEnum(Enum):
            stop_code = 0
            pop_top = 1
            rot_two = 2
            rot_three = 3
            dup_top = 4
            rot_four = 5
            nop = 9
            unary_positive = 10
            unary_negative = 11
            unary_not = 12
            unary_convert = 13
            unary_invert = 15
            binary_power = 19
            binary_multiply = 20
            binary_divide = 21
            binary_modulo = 22
            binary_add = 23
            binary_subtract = 24
            binary_subscr = 25
            binary_floor_divide = 26
            binary_true_divide = 27
            inplace_floor_divide = 28
            inplace_true_divide = 29
            slice_0 = 30
            slice_1 = 31
            slice_2 = 32
            slice_3 = 33
            store_slice_0 = 40
            store_slice_1 = 41
            store_slice_2 = 42
            store_slice_3 = 43
            delete_slice_0 = 50
            delete_slice_1 = 51
            delete_slice_2 = 52
            delete_slice_3 = 53
            store_map = 54
            inplace_add = 55
            inplace_subtract = 56
            inplace_multiply = 57
            inplace_divide = 58
            inplace_modulo = 59
            store_subscr = 60
            delete_subscr = 61
            binary_lshift = 62
            binary_rshift = 63
            binary_and = 64
            binary_xor = 65
            binary_or = 66
            inplace_power = 67
            get_iter = 68
            print_expr = 70
            print_item = 71
            print_newline = 72
            print_item_to = 73
            print_newline_to = 74
            inplace_lshift = 75
            inplace_rshift = 76
            inplace_and = 77
            inplace_xor = 78
            inplace_or = 79
            break_loop = 80
            with_cleanup = 81
            load_locals = 82
            return_value = 83
            import_star = 84
            exec_stmt = 85
            yield_value = 86
            pop_block = 87
            end_finally = 88
            build_class = 89
            store_name = 90
            delete_name = 91
            unpack_sequence = 92
            for_iter = 93
            list_append = 94
            store_attr = 95
            delete_attr = 96
            store_global = 97
            delete_global = 98
            dup_topx = 99
            load_const = 100
            load_name = 101
            build_tuple = 102
            build_list = 103
            build_set = 104
            build_map = 105
            load_attr = 106
            compare_op = 107
            import_name = 108
            import_from = 109
            jump_forward = 110
            jump_if_false_or_pop = 111
            jump_if_true_or_pop = 112
            jump_absolute = 113
            pop_jump_if_false = 114
            pop_jump_if_true = 115
            load_global = 116
            continue_loop = 119
            setup_loop = 120
            setup_except = 121
            setup_finally = 122
            load_fast = 124
            store_fast = 125
            delete_fast = 126
            raise_varargs = 130
            call_function = 131
            make_function = 132
            build_slice = 133
            make_closure = 134
            load_closure = 135
            load_deref = 136
            store_deref = 137
            call_function_var = 140
            call_function_kw = 141
            call_function_var_kw = 142
            setup_with = 143
            extended_arg = 145
            set_add = 146
            map_add = 147
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.op_code = KaitaiStream.resolve_enum(PythonPyc27.OpArg.OpCodeEnum, self._io.read_u1())
            if self.op_code.value >= PythonPyc27.OpArg.OpCodeEnum.store_name.value:
                self.arg = self._io.read_u2le()



    class PyObject(KaitaiStruct):

        class ObjectType(Enum):
            tuple = 40
            py_false = 70
            none = 78
            string_ref = 82
            py_true = 84
            code_object = 99
            int = 105
            string = 115
            interned = 116
            unicode_string = 117
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.type = KaitaiStream.resolve_enum(PythonPyc27.PyObject.ObjectType, self._io.read_u1())
            _on = self.type
            if _on == PythonPyc27.PyObject.ObjectType.string:
                self.value = PythonPyc27.PyObject.PyString(self._io, self, self._root)
            elif _on == PythonPyc27.PyObject.ObjectType.tuple:
                self.value = PythonPyc27.PyObject.Tuple(self._io, self, self._root)
            elif _on == PythonPyc27.PyObject.ObjectType.int:
                self.value = self._io.read_u4le()
            elif _on == PythonPyc27.PyObject.ObjectType.py_true:
                self.value = PythonPyc27.PyObject.PyTrue(self._io, self, self._root)
            elif _on == PythonPyc27.PyObject.ObjectType.py_false:
                self.value = PythonPyc27.PyObject.PyFalse(self._io, self, self._root)
            elif _on == PythonPyc27.PyObject.ObjectType.none:
                self.value = PythonPyc27.PyObject.PyNone(self._io, self, self._root)
            elif _on == PythonPyc27.PyObject.ObjectType.string_ref:
                self.value = PythonPyc27.PyObject.StringRef(self._io, self, self._root)
            elif _on == PythonPyc27.PyObject.ObjectType.code_object:
                self.value = PythonPyc27.CodeObject(self._io, self, self._root)
            elif _on == PythonPyc27.PyObject.ObjectType.interned:
                self.value = PythonPyc27.PyObject.InternedString(self._io, self, self._root)

        class PyNone(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                pass


        class PyFalse(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                pass


        class StringRef(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.interned_list_index = self._io.read_u4le()


        class PyTrue(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                pass


        class Tuple(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.count = self._io.read_u4le()
                self.items = [None] * (self.count)
                for i in range(self.count):
                    self.items[i] = PythonPyc27.PyObject(self._io, self, self._root)



        class UnicodeString(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.length = self._io.read_u4le()
                self.data = (self._io.read_bytes(self.length)).decode(u"utf-8")


        class InternedString(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.length = self._io.read_u4le()
                self.data = (self._io.read_bytes(self.length)).decode(u"utf-8")


        class PyString(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.length = self._io.read_u4le()
                self.data = self._io.read_bytes(self.length)



    class OpArgs(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.items = []
            i = 0
            while not self._io.is_eof():
                self.items.append(PythonPyc27.OpArg(self._io, self, self._root))
                i += 1




