# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Tga(KaitaiStruct):
    """TGA (AKA Truevision TGA, AKA TARGA), is a raster image file format created by Truevision. It supports up to 32 bits per pixel (three 8-bit RGB channels + 8-bit alpha channel), color mapping and optional lossless RLE compression.
    
    .. seealso::
       Source - http://www.dca.fee.unicamp.br/~martino/disciplinas/ea978/tgaffs.pdf
    """

    class ColorMapEnum(Enum):
        no_color_map = 0
        has_color_map = 1

    class ImageTypeEnum(Enum):
        no_image_data = 0
        uncomp_color_mapped = 1
        uncomp_true_color = 2
        uncomp_bw = 3
        rle_color_mapped = 9
        rle_true_color = 10
        rle_bw = 11
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.image_id_len = self._io.read_u1()
        self.color_map_type = KaitaiStream.resolve_enum(Tga.ColorMapEnum, self._io.read_u1())
        self.image_type = KaitaiStream.resolve_enum(Tga.ImageTypeEnum, self._io.read_u1())
        self.color_map_ofs = self._io.read_u2le()
        self.num_color_map = self._io.read_u2le()
        self.color_map_depth = self._io.read_u1()
        self.x_offset = self._io.read_u2le()
        self.y_offset = self._io.read_u2le()
        self.width = self._io.read_u2le()
        self.height = self._io.read_u2le()
        self.image_depth = self._io.read_u1()
        self.img_descriptor = self._io.read_u1()
        self.image_id = self._io.read_bytes(self.image_id_len)
        if self.color_map_type == Tga.ColorMapEnum.has_color_map:
            self.color_map = [None] * (self.num_color_map)
            for i in range(self.num_color_map):
                self.color_map[i] = self._io.read_bytes((self.color_map_depth + 7) // 8)



    class TgaFooter(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ext_area_ofs = self._io.read_u4le()
            self.dev_dir_ofs = self._io.read_u4le()
            self.version_magic = self._io.read_bytes(18)

        @property
        def is_valid(self):
            if hasattr(self, '_m_is_valid'):
                return self._m_is_valid if hasattr(self, '_m_is_valid') else None

            self._m_is_valid = self.version_magic == b"\x54\x52\x55\x45\x56\x49\x53\x49\x4F\x4E\x2D\x58\x46\x49\x4C\x45\x2E\x00"
            return self._m_is_valid if hasattr(self, '_m_is_valid') else None

        @property
        def ext_area(self):
            if hasattr(self, '_m_ext_area'):
                return self._m_ext_area if hasattr(self, '_m_ext_area') else None

            if self.is_valid:
                _pos = self._io.pos()
                self._io.seek(self.ext_area_ofs)
                self._m_ext_area = Tga.TgaExtArea(self._io, self, self._root)
                self._io.seek(_pos)

            return self._m_ext_area if hasattr(self, '_m_ext_area') else None


    class TgaExtArea(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ext_area_size = self._io.read_u2le()
            self.author_name = (self._io.read_bytes(41)).decode(u"ASCII")
            self.comments = [None] * (4)
            for i in range(4):
                self.comments[i] = (self._io.read_bytes(81)).decode(u"ASCII")

            self.timestamp = self._io.read_bytes(12)
            self.job_id = (self._io.read_bytes(41)).decode(u"ASCII")
            self.job_time = (self._io.read_bytes(6)).decode(u"ASCII")
            self.software_id = (self._io.read_bytes(41)).decode(u"ASCII")
            self.software_version = self._io.read_bytes(3)
            self.key_color = self._io.read_u4le()
            self.pixel_aspect_ratio = self._io.read_u4le()
            self.gamma_value = self._io.read_u4le()
            self.color_corr_ofs = self._io.read_u4le()
            self.postage_stamp_ofs = self._io.read_u4le()
            self.scan_line_ofs = self._io.read_u4le()
            self.attributes = self._io.read_u1()


    @property
    def footer(self):
        if hasattr(self, '_m_footer'):
            return self._m_footer if hasattr(self, '_m_footer') else None

        _pos = self._io.pos()
        self._io.seek((self._io.size() - 26))
        self._m_footer = Tga.TgaFooter(self._io, self, self._root)
        self._io.seek(_pos)
        return self._m_footer if hasattr(self, '_m_footer') else None


