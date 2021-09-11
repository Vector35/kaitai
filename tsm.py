# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Tsm(KaitaiStruct):
    """InfluxDB is a scalable database optimized for storage of time
    series, real-time application metrics, operations monitoring events,
    etc, written in Go.
    
    Data is stored in .tsm files, which are kept pretty simple
    conceptually. Each .tsm file contains a header and footer, which
    stores offset to an index. Index is used to find a data block for a
    requested time boundary.
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.header = Tsm.Header(self._io, self, self._root)

    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(4)
            if not self.magic == b"\x16\xD1\x16\xD1":
                raise kaitaistruct.ValidationNotEqualError(b"\x16\xD1\x16\xD1", self.magic, self._io, u"/types/header/seq/0")
            self.version = self._io.read_u1()


    class Index(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.offset = self._io.read_u8be()

        class IndexHeader(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.key_len = self._io.read_u2be()
                self.key = (self._io.read_bytes(self.key_len)).decode(u"UTF-8")
                self.type = self._io.read_u1()
                self.entry_count = self._io.read_u2be()
                self.index_entries = [None] * (self.entry_count)
                for i in range(self.entry_count):
                    self.index_entries[i] = Tsm.Index.IndexHeader.IndexEntry(self._io, self, self._root)


            class IndexEntry(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.min_time = self._io.read_u8be()
                    self.max_time = self._io.read_u8be()
                    self.block_offset = self._io.read_u8be()
                    self.block_size = self._io.read_u4be()

                class BlockEntry(KaitaiStruct):
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self._read()

                    def _read(self):
                        self.crc32 = self._io.read_u4be()
                        self.data = self._io.read_bytes((self._parent.block_size - 4))


                @property
                def block(self):
                    if hasattr(self, '_m_block'):
                        return self._m_block if hasattr(self, '_m_block') else None

                    io = self._root._io
                    _pos = io.pos()
                    io.seek(self.block_offset)
                    self._m_block = Tsm.Index.IndexHeader.IndexEntry.BlockEntry(io, self, self._root)
                    io.seek(_pos)
                    return self._m_block if hasattr(self, '_m_block') else None



        @property
        def entries(self):
            if hasattr(self, '_m_entries'):
                return self._m_entries if hasattr(self, '_m_entries') else None

            _pos = self._io.pos()
            self._io.seek(self.offset)
            self._m_entries = []
            i = 0
            while True:
                _ = Tsm.Index.IndexHeader(self._io, self, self._root)
                self._m_entries.append(_)
                if self._io.pos() == (self._io.size() - 8):
                    break
                i += 1
            self._io.seek(_pos)
            return self._m_entries if hasattr(self, '_m_entries') else None


    @property
    def index(self):
        if hasattr(self, '_m_index'):
            return self._m_index if hasattr(self, '_m_index') else None

        _pos = self._io.pos()
        self._io.seek((self._io.size() - 8))
        self._m_index = Tsm.Index(self._io, self, self._root)
        self._io.seek(_pos)
        return self._m_index if hasattr(self, '_m_index') else None


