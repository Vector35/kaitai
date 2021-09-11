# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class ZxSpectrumTap(KaitaiStruct):
    """TAP files are used by emulators of ZX Spectrum computer (released in
    1982 by Sinclair Research). TAP file stores blocks of data as if
    they are written to magnetic tape, which was used as primary media
    for ZX Spectrum. Contents of this file can be viewed as a very
    simple linear filesystem, storing named files with some basic
    metainformation prepended as a header.
    
    .. seealso::
       Source - https://faqwiki.zxnet.co.uk/wiki/TAP_format
    """

    class FlagEnum(Enum):
        header = 0
        data = 255

    class HeaderTypeEnum(Enum):
        program = 0
        num_array = 1
        char_array = 2
        bytes = 3
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.blocks = []
        i = 0
        while not self._io.is_eof():
            self.blocks.append(ZxSpectrumTap.Block(self._io, self, self._root))
            i += 1


    class Block(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len_block = self._io.read_u2le()
            self.flag = KaitaiStream.resolve_enum(ZxSpectrumTap.FlagEnum, self._io.read_u1())
            if  ((self.len_block == 19) and (self.flag == ZxSpectrumTap.FlagEnum.header)) :
                self.header = ZxSpectrumTap.Header(self._io, self, self._root)

            if self.len_block == 19:
                self.data = self._io.read_bytes((self.header.len_data + 4))

            if self.flag == ZxSpectrumTap.FlagEnum.data:
                self.headerless_data = self._io.read_bytes((self.len_block - 1))



    class ProgramParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.autostart_line = self._io.read_u2le()
            self.len_program = self._io.read_u2le()


    class BytesParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.start_address = self._io.read_u2le()
            self.reserved = self._io.read_bytes(2)


    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.header_type = KaitaiStream.resolve_enum(ZxSpectrumTap.HeaderTypeEnum, self._io.read_u1())
            self.filename = KaitaiStream.bytes_strip_right(self._io.read_bytes(10), 32)
            self.len_data = self._io.read_u2le()
            _on = self.header_type
            if _on == ZxSpectrumTap.HeaderTypeEnum.program:
                self.params = ZxSpectrumTap.ProgramParams(self._io, self, self._root)
            elif _on == ZxSpectrumTap.HeaderTypeEnum.num_array:
                self.params = ZxSpectrumTap.ArrayParams(self._io, self, self._root)
            elif _on == ZxSpectrumTap.HeaderTypeEnum.char_array:
                self.params = ZxSpectrumTap.ArrayParams(self._io, self, self._root)
            elif _on == ZxSpectrumTap.HeaderTypeEnum.bytes:
                self.params = ZxSpectrumTap.BytesParams(self._io, self, self._root)
            self.checksum = self._io.read_u1()


    class ArrayParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.reserved = self._io.read_u1()
            self.var_name = self._io.read_u1()
            self.reserved1 = self._io.read_bytes(2)
            if not self.reserved1 == b"\x00\x80":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x80", self.reserved1, self._io, u"/types/array_params/seq/2")



