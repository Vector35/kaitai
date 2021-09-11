# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class FtlDat(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.num_files = self._io.read_u4le()
        self.files = [None] * (self.num_files)
        for i in range(self.num_files):
            self.files[i] = FtlDat.File(self._io, self, self._root)


    class File(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ofs_meta = self._io.read_u4le()

        @property
        def meta(self):
            if hasattr(self, '_m_meta'):
                return self._m_meta if hasattr(self, '_m_meta') else None

            if self.ofs_meta != 0:
                _pos = self._io.pos()
                self._io.seek(self.ofs_meta)
                self._m_meta = FtlDat.Meta(self._io, self, self._root)
                self._io.seek(_pos)

            return self._m_meta if hasattr(self, '_m_meta') else None


    class Meta(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len_file = self._io.read_u4le()
            self.len_filename = self._io.read_u4le()
            self.filename = (self._io.read_bytes(self.len_filename)).decode(u"UTF-8")
            self.body = self._io.read_bytes(self.len_file)



