# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class QuakePak(KaitaiStruct):
    """
    .. seealso::
       Source - https://quakewiki.org/wiki/.pak#Format_specification
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(4)
        if not self.magic == b"\x50\x41\x43\x4B":
            raise kaitaistruct.ValidationNotEqualError(b"\x50\x41\x43\x4B", self.magic, self._io, u"/seq/0")
        self.ofs_index = self._io.read_u4le()
        self.len_index = self._io.read_u4le()

    class IndexStruct(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self.entries.append(QuakePak.IndexEntry(self._io, self, self._root))
                i += 1



    class IndexEntry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = (KaitaiStream.bytes_terminate(KaitaiStream.bytes_strip_right(self._io.read_bytes(56), 0), 0, False)).decode(u"UTF-8")
            self.ofs = self._io.read_u4le()
            self.size = self._io.read_u4le()

        @property
        def body(self):
            if hasattr(self, '_m_body'):
                return self._m_body if hasattr(self, '_m_body') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.ofs)
            self._m_body = io.read_bytes(self.size)
            io.seek(_pos)
            return self._m_body if hasattr(self, '_m_body') else None


    @property
    def index(self):
        if hasattr(self, '_m_index'):
            return self._m_index if hasattr(self, '_m_index') else None

        _pos = self._io.pos()
        self._io.seek(self.ofs_index)
        self._raw__m_index = self._io.read_bytes(self.len_index)
        _io__raw__m_index = KaitaiStream(BytesIO(self._raw__m_index))
        self._m_index = QuakePak.IndexStruct(_io__raw__m_index, self, self._root)
        self._io.seek(_pos)
        return self._m_index if hasattr(self, '_m_index') else None


