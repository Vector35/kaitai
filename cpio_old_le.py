# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class CpioOldLe(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.files = []
        i = 0
        while not self._io.is_eof():
            self.files.append(CpioOldLe.File(self._io, self, self._root))
            i += 1


    class File(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.header = CpioOldLe.FileHeader(self._io, self, self._root)
            self.path_name = self._io.read_bytes((self.header.path_name_size - 1))
            self.string_terminator = self._io.read_bytes(1)
            if not self.string_terminator == b"\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00", self.string_terminator, self._io, u"/types/file/seq/2")
            if (self.header.path_name_size % 2) == 1:
                self.path_name_padding = self._io.read_bytes(1)
                if not self.path_name_padding == b"\x00":
                    raise kaitaistruct.ValidationNotEqualError(b"\x00", self.path_name_padding, self._io, u"/types/file/seq/3")

            self.file_data = self._io.read_bytes(self.header.file_size.value)
            if (self.header.file_size.value % 2) == 1:
                self.file_data_padding = self._io.read_bytes(1)
                if not self.file_data_padding == b"\x00":
                    raise kaitaistruct.ValidationNotEqualError(b"\x00", self.file_data_padding, self._io, u"/types/file/seq/5")

            if  ((self.path_name == b"\x54\x52\x41\x49\x4C\x45\x52\x21\x21\x21") and (self.header.file_size.value == 0)) :
                self.end_of_file_padding = self._io.read_bytes_full()



    class FileHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(2)
            if not self.magic == b"\xC7\x71":
                raise kaitaistruct.ValidationNotEqualError(b"\xC7\x71", self.magic, self._io, u"/types/file_header/seq/0")
            self.device_number = self._io.read_u2le()
            self.inode_number = self._io.read_u2le()
            self.mode = self._io.read_u2le()
            self.user_id = self._io.read_u2le()
            self.group_id = self._io.read_u2le()
            self.number_of_links = self._io.read_u2le()
            self.r_device_number = self._io.read_u2le()
            self.modification_time = CpioOldLe.FourByteUnsignedInteger(self._io, self, self._root)
            self.path_name_size = self._io.read_u2le()
            self.file_size = CpioOldLe.FourByteUnsignedInteger(self._io, self, self._root)


    class FourByteUnsignedInteger(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.most_significant_bits = self._io.read_u2le()
            self.least_significant_bits = self._io.read_u2le()

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value if hasattr(self, '_m_value') else None

            self._m_value = (self.least_significant_bits + (self.most_significant_bits << 16))
            return self._m_value if hasattr(self, '_m_value') else None



