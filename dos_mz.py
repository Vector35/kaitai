# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class DosMz(KaitaiStruct):
    """DOS MZ file format is a traditional format for executables in MS-DOS
    environment. Many modern formats (i.e. Windows PE) still maintain
    compatibility stub with this format.
    
    As opposed to .com file format (which basically sports one 64K code
    segment of raw CPU instructions), DOS MZ .exe file format allowed
    more flexible memory management, loading of larger programs and
    added support for relocations.
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.hdr = DosMz.MzHeader(self._io, self, self._root)
        self.mz_header2 = self._io.read_bytes((self.hdr.ofs_relocations - 28))
        self.relocations = [None] * (self.hdr.num_relocations)
        for i in range(self.hdr.num_relocations):
            self.relocations[i] = DosMz.Relocation(self._io, self, self._root)

        self.body = self._io.read_bytes_full()

    class MzHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(2)
            self.last_page_extra_bytes = self._io.read_u2le()
            self.num_pages = self._io.read_u2le()
            self.num_relocations = self._io.read_u2le()
            self.header_size = self._io.read_u2le()
            self.min_allocation = self._io.read_u2le()
            self.max_allocation = self._io.read_u2le()
            self.initial_ss = self._io.read_u2le()
            self.initial_sp = self._io.read_u2le()
            self.checksum = self._io.read_u2le()
            self.initial_ip = self._io.read_u2le()
            self.initial_cs = self._io.read_u2le()
            self.ofs_relocations = self._io.read_u2le()
            self.overlay_id = self._io.read_u2le()


    class Relocation(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ofs = self._io.read_u2le()
            self.seg = self._io.read_u2le()



