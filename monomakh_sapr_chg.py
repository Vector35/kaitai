# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class MonomakhSaprChg(KaitaiStruct):
    """CHG is a container format file used by
    [MONOMAKH-SAPR](https://www.liraland.com/mono/index.php), a software
    package for analysis & design of reinforced concrete multi-storey
    buildings with arbitrary configuration in plan.
    
    CHG is a simple container, which bundles several project files
    together.
    
    Written and tested by Vladimir Shulzhitskiy, 2017
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.title = (self._io.read_bytes(10)).decode(u"ascii")
        self.ent = []
        i = 0
        while not self._io.is_eof():
            self.ent.append(MonomakhSaprChg.Block(self._io, self, self._root))
            i += 1


    class Block(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.header = (self._io.read_bytes(13)).decode(u"ascii")
            self.file_size = self._io.read_u8le()
            self.file = self._io.read_bytes(self.file_size)



