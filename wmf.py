# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Wmf(KaitaiStruct):
    """WMF (Windows Metafile) is a relatively early vector image format
    introduced for Microsoft Windows in 1990.
    
    Inside, it provides a serialized list of Windows GDI (Graphics
    Device Interface) function calls, which, if played back, result in
    an image being drawn on a given surface (display, off-screen buffer,
    printer, etc).
    
    .. seealso::
       Source - http://www.digitalpreservation.gov/formats/digformatspecs/WindowsMetafileFormat(wmf)Specification.pdf
    """

    class Func(Enum):
        eof = 0
        savedc = 30
        realizepalette = 53
        setpalentries = 55
        createpalette = 247
        setbkmode = 258
        setmapmode = 259
        setrop2 = 260
        setrelabs = 261
        setpolyfillmode = 262
        setstretchbltmode = 263
        settextcharextra = 264
        restoredc = 295
        invertregion = 298
        paintregion = 299
        selectclipregion = 300
        selectobject = 301
        settextalign = 302
        resizepalette = 313
        dibcreatepatternbrush = 322
        setlayout = 329
        deleteobject = 496
        createpatternbrush = 505
        setbkcolor = 513
        settextcolor = 521
        settextjustification = 522
        setwindoworg = 523
        setwindowext = 524
        setviewportorg = 525
        setviewportext = 526
        offsetwindoworg = 527
        offsetviewportorg = 529
        lineto = 531
        moveto = 532
        offsetcliprgn = 544
        fillregion = 552
        setmapperflags = 561
        selectpalette = 564
        createpenindirect = 762
        createfontindirect = 763
        createbrushindirect = 764
        polygon = 804
        polyline = 805
        scalewindowext = 1040
        scaleviewportext = 1042
        excludecliprect = 1045
        intersectcliprect = 1046
        ellipse = 1048
        floodfill = 1049
        rectangle = 1051
        setpixel = 1055
        frameregion = 1065
        animatepalette = 1078
        textout = 1313
        polypolygon = 1336
        extfloodfill = 1352
        roundrect = 1564
        patblt = 1565
        escape = 1574
        createregion = 1791
        arc = 2071
        pie = 2074
        chord = 2096
        bitblt = 2338
        dibbitblt = 2368
        exttextout = 2610
        stretchblt = 2851
        dibstretchblt = 2881
        setdibtodev = 3379
        stretchdib = 3907

    class BinRasterOp(Enum):
        black = 1
        notmergepen = 2
        masknotpen = 3
        notcopypen = 4
        maskpennot = 5
        not = 6
        xorpen = 7
        notmaskpen = 8
        maskpen = 9
        notxorpen = 10
        nop = 11
        mergenotpen = 12
        copypen = 13
        mergepennot = 14
        mergepen = 15
        white = 16

    class MixMode(Enum):
        transparent = 1
        opaque = 2

    class PolyFillMode(Enum):
        alternate = 1
        winding = 2
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.special_header = Wmf.SpecialHeader(self._io, self, self._root)
        self.header = Wmf.Header(self._io, self, self._root)
        self.records = []
        i = 0
        while True:
            _ = Wmf.Record(self._io, self, self._root)
            self.records.append(_)
            if _.function == Wmf.Func.eof:
                break
            i += 1

    class ParamsSetwindoworg(KaitaiStruct):
        """
        .. seealso::
           section 2.3.5.31
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.y = self._io.read_s2le()
            self.x = self._io.read_s2le()


    class ParamsSetbkmode(KaitaiStruct):
        """
        .. seealso::
           section 2.3.5.15
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.bk_mode = KaitaiStream.resolve_enum(Wmf.MixMode, self._io.read_u2le())


    class PointS(KaitaiStruct):
        """
        .. seealso::
           section 2.2.1.12
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_s2le()
            self.y = self._io.read_s2le()


    class ParamsSetwindowext(KaitaiStruct):
        """
        .. seealso::
           section 2.3.5.30
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.y = self._io.read_s2le()
            self.x = self._io.read_s2le()


    class ParamsPolygon(KaitaiStruct):
        """
        .. seealso::
           section 2.3.3.15 = params_polyline
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_points = self._io.read_s2le()
            self.points = [None] * (self.num_points)
            for i in range(self.num_points):
                self.points[i] = Wmf.PointS(self._io, self, self._root)



    class Header(KaitaiStruct):

        class MetafileType(Enum):
            memory_metafile = 1
            disk_metafile = 2
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.metafile_type = KaitaiStream.resolve_enum(Wmf.Header.MetafileType, self._io.read_u2le())
            self.header_size = self._io.read_u2le()
            self.version = self._io.read_u2le()
            self.size = self._io.read_u4le()
            self.number_of_objects = self._io.read_u2le()
            self.max_record = self._io.read_u4le()
            self.number_of_members = self._io.read_u2le()


    class ColorRef(KaitaiStruct):
        """
        .. seealso::
           section 2.2.1.7
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.red = self._io.read_u1()
            self.green = self._io.read_u1()
            self.blue = self._io.read_u1()
            self.reserved = self._io.read_u1()


    class ParamsSetrop2(KaitaiStruct):
        """
        .. seealso::
           section 2.3.5.22
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.draw_mode = KaitaiStream.resolve_enum(Wmf.BinRasterOp, self._io.read_u2le())


    class ParamsSetpolyfillmode(KaitaiStruct):
        """
        .. seealso::
           section 2.3.5.20
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.poly_fill_mode = KaitaiStream.resolve_enum(Wmf.PolyFillMode, self._io.read_u2le())


    class ParamsPolyline(KaitaiStruct):
        """
        .. seealso::
           section 2.3.3.14
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_points = self._io.read_s2le()
            self.points = [None] * (self.num_points)
            for i in range(self.num_points):
                self.points[i] = Wmf.PointS(self._io, self, self._root)



    class SpecialHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(4)
            if not self.magic == b"\xD7\xCD\xC6\x9A":
                raise kaitaistruct.ValidationNotEqualError(b"\xD7\xCD\xC6\x9A", self.magic, self._io, u"/types/special_header/seq/0")
            self.handle = self._io.read_bytes(2)
            if not self.handle == b"\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00", self.handle, self._io, u"/types/special_header/seq/1")
            self.left = self._io.read_s2le()
            self.top = self._io.read_s2le()
            self.right = self._io.read_s2le()
            self.bottom = self._io.read_s2le()
            self.inch = self._io.read_u2le()
            self.reserved = self._io.read_bytes(4)
            if not self.reserved == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00", self.reserved, self._io, u"/types/special_header/seq/7")
            self.checksum = self._io.read_u2le()


    class Record(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.size = self._io.read_u4le()
            self.function = KaitaiStream.resolve_enum(Wmf.Func, self._io.read_u2le())
            _on = self.function
            if _on == Wmf.Func.setbkmode:
                self._raw_params = self._io.read_bytes(((self.size - 3) * 2))
                _io__raw_params = KaitaiStream(BytesIO(self._raw_params))
                self.params = Wmf.ParamsSetbkmode(_io__raw_params, self, self._root)
            elif _on == Wmf.Func.polygon:
                self._raw_params = self._io.read_bytes(((self.size - 3) * 2))
                _io__raw_params = KaitaiStream(BytesIO(self._raw_params))
                self.params = Wmf.ParamsPolygon(_io__raw_params, self, self._root)
            elif _on == Wmf.Func.setbkcolor:
                self._raw_params = self._io.read_bytes(((self.size - 3) * 2))
                _io__raw_params = KaitaiStream(BytesIO(self._raw_params))
                self.params = Wmf.ColorRef(_io__raw_params, self, self._root)
            elif _on == Wmf.Func.setpolyfillmode:
                self._raw_params = self._io.read_bytes(((self.size - 3) * 2))
                _io__raw_params = KaitaiStream(BytesIO(self._raw_params))
                self.params = Wmf.ParamsSetpolyfillmode(_io__raw_params, self, self._root)
            elif _on == Wmf.Func.setwindoworg:
                self._raw_params = self._io.read_bytes(((self.size - 3) * 2))
                _io__raw_params = KaitaiStream(BytesIO(self._raw_params))
                self.params = Wmf.ParamsSetwindoworg(_io__raw_params, self, self._root)
            elif _on == Wmf.Func.setrop2:
                self._raw_params = self._io.read_bytes(((self.size - 3) * 2))
                _io__raw_params = KaitaiStream(BytesIO(self._raw_params))
                self.params = Wmf.ParamsSetrop2(_io__raw_params, self, self._root)
            elif _on == Wmf.Func.setwindowext:
                self._raw_params = self._io.read_bytes(((self.size - 3) * 2))
                _io__raw_params = KaitaiStream(BytesIO(self._raw_params))
                self.params = Wmf.ParamsSetwindowext(_io__raw_params, self, self._root)
            elif _on == Wmf.Func.polyline:
                self._raw_params = self._io.read_bytes(((self.size - 3) * 2))
                _io__raw_params = KaitaiStream(BytesIO(self._raw_params))
                self.params = Wmf.ParamsPolyline(_io__raw_params, self, self._root)
            else:
                self.params = self._io.read_bytes(((self.size - 3) * 2))



