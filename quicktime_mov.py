# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class QuicktimeMov(KaitaiStruct):
    """
    .. seealso::
       Source - https://developer.apple.com/library/content/documentation/QuickTime/QTFF/QTFFChap1/qtff1.html#//apple_ref/doc/uid/TP40000939-CH203-BBCGDDDF
    """

    class AtomType(Enum):
        xtra = 1484026465
        dinf = 1684631142
        dref = 1685218662
        edts = 1701082227
        elst = 1701606260
        free = 1718773093
        ftyp = 1718909296
        hdlr = 1751411826
        iods = 1768907891
        mdat = 1835295092
        mdhd = 1835296868
        mdia = 1835297121
        meta = 1835365473
        minf = 1835626086
        moof = 1836019558
        moov = 1836019574
        mvhd = 1836476516
        smhd = 1936549988
        stbl = 1937007212
        stco = 1937007471
        stsc = 1937011555
        stsd = 1937011556
        stsz = 1937011578
        stts = 1937011827
        tkhd = 1953196132
        traf = 1953653094
        trak = 1953653099
        tref = 1953654118
        udta = 1969517665
        vmhd = 1986881636

    class Brand(Enum):
        x_3g2a = 862401121
        x_3ge6 = 862414134
        x_3ge9 = 862414137
        x_3gf9 = 862414393
        x_3gg6 = 862414646
        x_3gg9 = 862414649
        x_3gh9 = 862414905
        x_3gm9 = 862416185
        x_3gp4 = 862416948
        x_3gp5 = 862416949
        x_3gp6 = 862416950
        x_3gp7 = 862416951
        x_3gp8 = 862416952
        x_3gp9 = 862416953
        x_3gr6 = 862417462
        x_3gr9 = 862417465
        x_3gs6 = 862417718
        x_3gs9 = 862417721
        x_3gt9 = 862417977
        arri = 1095914057
        caep = 1128351056
        cdes = 1128555891
        j2p0 = 1244811312
        j2p1 = 1244811313
        lcag = 1279476039
        m4a = 1295270176
        m4b = 1295270432
        m4p = 1295274016
        m4v = 1295275552
        mfsm = 1296454477
        mgsv = 1296520022
        mppi = 1297109065
        msnv = 1297305174
        ross = 1380930387
        seau = 1397047637
        sebk = 1397047883
        xavc = 1480676931
        avc1 = 1635148593
        bbxm = 1650620525
        caqv = 1667330422
        ccff = 1667458662
        da0a = 1684090977
        da0b = 1684090978
        da1a = 1684091233
        da1b = 1684091234
        da2a = 1684091489
        da2b = 1684091490
        da3a = 1684091745
        da3b = 1684091746
        dash = 1684108136
        dby1 = 1684175153
        dmb1 = 1684890161
        dsms = 1685286259
        dv1a = 1685467489
        dv1b = 1685467490
        dv2a = 1685467745
        dv2b = 1685467746
        dv3a = 1685468001
        dv3b = 1685468002
        dvr1 = 1685484081
        dvt1 = 1685484593
        dxo = 1685614368
        emsg = 1701671783
        ifrm = 1768321645
        isc2 = 1769169714
        iso2 = 1769172786
        iso3 = 1769172787
        iso4 = 1769172788
        iso5 = 1769172789
        iso6 = 1769172790
        isom = 1769172845
        jp2 = 1785737760
        jpm = 1785752864
        jpsi = 1785754473
        jpx = 1785755680
        jpxb = 1785755746
        lmsg = 1819112295
        mj2s = 1835676275
        mjp2 = 1835692082
        mp21 = 1836069425
        mp41 = 1836069937
        mp42 = 1836069938
        mp71 = 1836070705
        msdh = 1836278888
        msix = 1836280184
        niko = 1852402543
        odcf = 1868850022
        opf2 = 1869637170
        opx2 = 1869641778
        pana = 1885433441
        piff = 1885955686
        pnvi = 1886287465
        qt = 1903435808
        risx = 1919513464
        sdv = 1935963680
        senv = 1936027254
        sims = 1936289139
        sisx = 1936290680
        ssss = 1936946035
        uvvu = 1970697845
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.atoms = QuicktimeMov.AtomList(self._io, self, self._root)

    class MvhdBody(KaitaiStruct):
        """
        .. seealso::
           Source - https://developer.apple.com/library/content/documentation/QuickTime/QTFF/QTFFChap2/qtff2.html#//apple_ref/doc/uid/TP40000939-CH204-BBCGFGJG
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.version = self._io.read_u1()
            self.flags = self._io.read_bytes(3)
            self.creation_time = self._io.read_u4be()
            self.modification_time = self._io.read_u4be()
            self.time_scale = self._io.read_u4be()
            self.duration = self._io.read_u4be()
            self.preferred_rate = QuicktimeMov.Fixed32(self._io, self, self._root)
            self.preferred_volume = QuicktimeMov.Fixed16(self._io, self, self._root)
            self.reserved1 = self._io.read_bytes(10)
            self.matrix = self._io.read_bytes(36)
            self.preview_time = self._io.read_u4be()
            self.preview_duration = self._io.read_u4be()
            self.poster_time = self._io.read_u4be()
            self.selection_time = self._io.read_u4be()
            self.selection_duration = self._io.read_u4be()
            self.current_time = self._io.read_u4be()
            self.next_track_id = self._io.read_u4be()


    class FtypBody(KaitaiStruct):
        """
        .. seealso::
           Source - https://developer.apple.com/library/content/documentation/QuickTime/QTFF/QTFFChap1/qtff1.html#//apple_ref/doc/uid/TP40000939-CH203-CJBCBIFF
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.major_brand = KaitaiStream.resolve_enum(QuicktimeMov.Brand, self._io.read_u4be())
            self.minor_version = self._io.read_bytes(4)
            self.compatible_brands = []
            i = 0
            while not self._io.is_eof():
                self.compatible_brands.append(KaitaiStream.resolve_enum(QuicktimeMov.Brand, self._io.read_u4be()))
                i += 1



    class Fixed32(KaitaiStruct):
        """Fixed-point 32-bit number."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.int_part = self._io.read_s2be()
            self.frac_part = self._io.read_u2be()


    class Fixed16(KaitaiStruct):
        """Fixed-point 16-bit number."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.int_part = self._io.read_s1()
            self.frac_part = self._io.read_u1()


    class Atom(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len32 = self._io.read_u4be()
            self.atom_type = KaitaiStream.resolve_enum(QuicktimeMov.AtomType, self._io.read_u4be())
            if self.len32 == 1:
                self.len64 = self._io.read_u8be()

            _on = self.atom_type
            if _on == QuicktimeMov.AtomType.moof:
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = QuicktimeMov.AtomList(_io__raw_body, self, self._root)
            elif _on == QuicktimeMov.AtomType.tkhd:
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = QuicktimeMov.TkhdBody(_io__raw_body, self, self._root)
            elif _on == QuicktimeMov.AtomType.stbl:
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = QuicktimeMov.AtomList(_io__raw_body, self, self._root)
            elif _on == QuicktimeMov.AtomType.traf:
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = QuicktimeMov.AtomList(_io__raw_body, self, self._root)
            elif _on == QuicktimeMov.AtomType.minf:
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = QuicktimeMov.AtomList(_io__raw_body, self, self._root)
            elif _on == QuicktimeMov.AtomType.trak:
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = QuicktimeMov.AtomList(_io__raw_body, self, self._root)
            elif _on == QuicktimeMov.AtomType.moov:
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = QuicktimeMov.AtomList(_io__raw_body, self, self._root)
            elif _on == QuicktimeMov.AtomType.mdia:
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = QuicktimeMov.AtomList(_io__raw_body, self, self._root)
            elif _on == QuicktimeMov.AtomType.dinf:
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = QuicktimeMov.AtomList(_io__raw_body, self, self._root)
            elif _on == QuicktimeMov.AtomType.mvhd:
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = QuicktimeMov.MvhdBody(_io__raw_body, self, self._root)
            elif _on == QuicktimeMov.AtomType.ftyp:
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = QuicktimeMov.FtypBody(_io__raw_body, self, self._root)
            else:
                self.body = self._io.read_bytes(self.len)

        @property
        def len(self):
            if hasattr(self, '_m_len'):
                return self._m_len if hasattr(self, '_m_len') else None

            self._m_len = ((self._io.size() - 8) if self.len32 == 0 else ((self.len64 - 16) if self.len32 == 1 else (self.len32 - 8)))
            return self._m_len if hasattr(self, '_m_len') else None


    class TkhdBody(KaitaiStruct):
        """
        .. seealso::
           Source - https://developer.apple.com/library/content/documentation/QuickTime/QTFF/QTFFChap2/qtff2.html#//apple_ref/doc/uid/TP40000939-CH204-25550
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.version = self._io.read_u1()
            self.flags = self._io.read_bytes(3)
            self.creation_time = self._io.read_u4be()
            self.modification_time = self._io.read_u4be()
            self.track_id = self._io.read_u4be()
            self.reserved1 = self._io.read_bytes(4)
            self.duration = self._io.read_u4be()
            self.reserved2 = self._io.read_bytes(8)
            self.layer = self._io.read_u2be()
            self.alternative_group = self._io.read_u2be()
            self.volume = self._io.read_u2be()
            self.reserved3 = self._io.read_u2be()
            self.matrix = self._io.read_bytes(36)
            self.width = QuicktimeMov.Fixed32(self._io, self, self._root)
            self.height = QuicktimeMov.Fixed32(self._io, self, self._root)


    class AtomList(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.items = []
            i = 0
            while not self._io.is_eof():
                self.items.append(QuicktimeMov.Atom(self._io, self, self._root))
                i += 1




