# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Pcx(KaitaiStruct):

    class Versions(Enum):
        v2_5 = 0
        v2_8_with_palette = 2
        v2_8_without_palette = 3
        paintbrush_for_windows = 4
        v3_0 = 5

    class Encodings(Enum):
        rle = 1
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self._raw_hdr = self._io.read_bytes(128)
        _io__raw_hdr = KaitaiStream(BytesIO(self._raw_hdr))
        self.hdr = Pcx.Header(_io__raw_hdr, self, self._root)

    class Header(KaitaiStruct):
        """
        .. seealso::
           - "ZSoft .PCX FILE HEADER FORMAT" - http://web.archive.org/web/20100206055706/http://www.qzx.com/pc-gpe/pcx.txt
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(1)
            if not self.magic == b"\x0A":
                raise kaitaistruct.ValidationNotEqualError(b"\x0A", self.magic, self._io, u"/types/header/seq/0")
            self.version = KaitaiStream.resolve_enum(Pcx.Versions, self._io.read_u1())
            self.encoding = KaitaiStream.resolve_enum(Pcx.Encodings, self._io.read_u1())
            self.bits_per_pixel = self._io.read_u1()
            self.img_x_min = self._io.read_u2le()
            self.img_y_min = self._io.read_u2le()
            self.img_x_max = self._io.read_u2le()
            self.img_y_max = self._io.read_u2le()
            self.hdpi = self._io.read_u2le()
            self.vdpi = self._io.read_u2le()
            self.palette_16 = self._io.read_bytes(48)
            self.reserved = self._io.read_bytes(1)
            if not self.reserved == b"\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00", self.reserved, self._io, u"/types/header/seq/11")
            self.num_planes = self._io.read_u1()
            self.bytes_per_line = self._io.read_u2le()
            self.palette_info = self._io.read_u2le()
            self.h_screen_size = self._io.read_u2le()
            self.v_screen_size = self._io.read_u2le()


    class TPalette256(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(1)
            if not self.magic == b"\x0C":
                raise kaitaistruct.ValidationNotEqualError(b"\x0C", self.magic, self._io, u"/types/t_palette_256/seq/0")
            self.colors = [None] * (256)
            for i in range(256):
                self.colors[i] = Pcx.Rgb(self._io, self, self._root)



    class Rgb(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.r = self._io.read_u1()
            self.g = self._io.read_u1()
            self.b = self._io.read_u1()


    @property
    def palette_256(self):
        """
        .. seealso::
           - "VGA 256 Color Palette Information" - http://web.archive.org/web/20100206055706/http://www.qzx.com/pc-gpe/pcx.txt
        """
        if hasattr(self, '_m_palette_256'):
            return self._m_palette_256 if hasattr(self, '_m_palette_256') else None

        if  ((self.hdr.version == Pcx.Versions.v3_0) and (self.hdr.bits_per_pixel == 8) and (self.hdr.num_planes == 1)) :
            _pos = self._io.pos()
            self._io.seek((self._io.size() - 769))
            self._m_palette_256 = Pcx.TPalette256(self._io, self, self._root)
            self._io.seek(_pos)

        return self._m_palette_256 if hasattr(self, '_m_palette_256') else None


