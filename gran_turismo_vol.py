# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class GranTurismoVol(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(8)
        if not self.magic == b"\x47\x54\x46\x53\x00\x00\x00\x00":
            raise kaitaistruct.ValidationNotEqualError(b"\x47\x54\x46\x53\x00\x00\x00\x00", self.magic, self._io, u"/seq/0")
        self.num_files = self._io.read_u2le()
        self.num_entries = self._io.read_u2le()
        self.reserved = self._io.read_bytes(4)
        if not self.reserved == b"\x00\x00\x00\x00":
            raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00", self.reserved, self._io, u"/seq/3")
        self.offsets = [None] * (self.num_files)
        for i in range(self.num_files):
            self.offsets[i] = self._io.read_u4le()


    class FileInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.timestamp = self._io.read_u4le()
            self.offset_idx = self._io.read_u2le()
            self.flags = self._io.read_u1()
            self.name = (KaitaiStream.bytes_terminate(KaitaiStream.bytes_strip_right(self._io.read_bytes(25), 0), 0, False)).decode(u"ASCII")

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size if hasattr(self, '_m_size') else None

            self._m_size = ((self._root.offsets[(self.offset_idx + 1)] & 4294965248) - self._root.offsets[self.offset_idx])
            return self._m_size if hasattr(self, '_m_size') else None

        @property
        def body(self):
            if hasattr(self, '_m_body'):
                return self._m_body if hasattr(self, '_m_body') else None

            if not (self.is_dir):
                _pos = self._io.pos()
                self._io.seek((self._root.offsets[self.offset_idx] & 4294965248))
                self._m_body = self._io.read_bytes(self.size)
                self._io.seek(_pos)

            return self._m_body if hasattr(self, '_m_body') else None

        @property
        def is_dir(self):
            if hasattr(self, '_m_is_dir'):
                return self._m_is_dir if hasattr(self, '_m_is_dir') else None

            self._m_is_dir = (self.flags & 1) != 0
            return self._m_is_dir if hasattr(self, '_m_is_dir') else None

        @property
        def is_last_entry(self):
            if hasattr(self, '_m_is_last_entry'):
                return self._m_is_last_entry if hasattr(self, '_m_is_last_entry') else None

            self._m_is_last_entry = (self.flags & 128) != 0
            return self._m_is_last_entry if hasattr(self, '_m_is_last_entry') else None


    @property
    def ofs_dir(self):
        if hasattr(self, '_m_ofs_dir'):
            return self._m_ofs_dir if hasattr(self, '_m_ofs_dir') else None

        self._m_ofs_dir = self.offsets[1]
        return self._m_ofs_dir if hasattr(self, '_m_ofs_dir') else None

    @property
    def files(self):
        if hasattr(self, '_m_files'):
            return self._m_files if hasattr(self, '_m_files') else None

        _pos = self._io.pos()
        self._io.seek((self.ofs_dir & 4294965248))
        self._m_files = [None] * (self._root.num_entries)
        for i in range(self._root.num_entries):
            self._m_files[i] = GranTurismoVol.FileInfo(self._io, self, self._root)

        self._io.seek(_pos)
        return self._m_files if hasattr(self, '_m_files') else None


