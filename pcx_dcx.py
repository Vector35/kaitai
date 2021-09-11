# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

from . import pcx
class PcxDcx(KaitaiStruct):
    """DCX is a simple extension of PCX image format allowing to bundle
    many PCX images (typically, pages of a document) in one file. It saw
    some limited use in DOS-era fax software, but was largely
    superseeded with multi-page TIFFs and PDFs since then.
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(4)
        if not self.magic == b"\xB1\x68\xDE\x3A":
            raise kaitaistruct.ValidationNotEqualError(b"\xB1\x68\xDE\x3A", self.magic, self._io, u"/seq/0")
        self.files = []
        i = 0
        while True:
            _ = PcxDcx.PcxOffset(self._io, self, self._root)
            self.files.append(_)
            if _.ofs_body == 0:
                break
            i += 1

    class PcxOffset(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ofs_body = self._io.read_u4le()

        @property
        def body(self):
            if hasattr(self, '_m_body'):
                return self._m_body if hasattr(self, '_m_body') else None

            if self.ofs_body != 0:
                _pos = self._io.pos()
                self._io.seek(self.ofs_body)
                self._m_body = pcx.Pcx(self._io)
                self._io.seek(_pos)

            return self._m_body if hasattr(self, '_m_body') else None



