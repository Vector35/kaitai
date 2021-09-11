# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Xwd(KaitaiStruct):
    """xwd is a file format written by eponymous X11 screen capture
    application (xwd stands for "X Window Dump"). Typically, an average
    user transforms xwd format into something more widespread by any of
    `xwdtopnm` and `pnmto...` utilities right away.
    
    xwd format itself provides a raw uncompressed bitmap with some
    metainformation, like pixel format, width, height, bit depth,
    etc. Note that technically format includes machine-dependent fields
    and thus is probably a poor choice for true cross-platform usage.
    """

    class PixmapFormat(Enum):
        x_y_bitmap = 0
        x_y_pixmap = 1
        z_pixmap = 2

    class ByteOrder(Enum):
        le = 0
        be = 1

    class VisualClass(Enum):
        static_gray = 0
        gray_scale = 1
        static_color = 2
        pseudo_color = 3
        true_color = 4
        direct_color = 5
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.len_header = self._io.read_u4be()
        self._raw_hdr = self._io.read_bytes((self.len_header - 4))
        _io__raw_hdr = KaitaiStream(BytesIO(self._raw_hdr))
        self.hdr = Xwd.Header(_io__raw_hdr, self, self._root)
        self._raw_color_map = [None] * (self.hdr.color_map_entries)
        self.color_map = [None] * (self.hdr.color_map_entries)
        for i in range(self.hdr.color_map_entries):
            self._raw_color_map[i] = self._io.read_bytes(12)
            _io__raw_color_map = KaitaiStream(BytesIO(self._raw_color_map[i]))
            self.color_map[i] = Xwd.ColorMapEntry(_io__raw_color_map, self, self._root)


    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.file_version = self._io.read_u4be()
            self.pixmap_format = KaitaiStream.resolve_enum(Xwd.PixmapFormat, self._io.read_u4be())
            self.pixmap_depth = self._io.read_u4be()
            self.pixmap_width = self._io.read_u4be()
            self.pixmap_height = self._io.read_u4be()
            self.x_offset = self._io.read_u4be()
            self.byte_order = KaitaiStream.resolve_enum(Xwd.ByteOrder, self._io.read_u4be())
            self.bitmap_unit = self._io.read_u4be()
            self.bitmap_bit_order = self._io.read_u4be()
            self.bitmap_pad = self._io.read_u4be()
            self.bits_per_pixel = self._io.read_u4be()
            self.bytes_per_line = self._io.read_u4be()
            self.visual_class = KaitaiStream.resolve_enum(Xwd.VisualClass, self._io.read_u4be())
            self.red_mask = self._io.read_u4be()
            self.green_mask = self._io.read_u4be()
            self.blue_mask = self._io.read_u4be()
            self.bits_per_rgb = self._io.read_u4be()
            self.number_of_colors = self._io.read_u4be()
            self.color_map_entries = self._io.read_u4be()
            self.window_width = self._io.read_u4be()
            self.window_height = self._io.read_u4be()
            self.window_x = self._io.read_s4be()
            self.window_y = self._io.read_s4be()
            self.window_border_width = self._io.read_u4be()
            self.creator = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")


    class ColorMapEntry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.entry_number = self._io.read_u4be()
            self.red = self._io.read_u2be()
            self.green = self._io.read_u2be()
            self.blue = self._io.read_u2be()
            self.flags = self._io.read_u1()
            self.padding = self._io.read_u1()



