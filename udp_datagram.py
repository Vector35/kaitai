# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class UdpDatagram(KaitaiStruct):
    """UDP is a simple stateless transport layer (AKA OSI layer 4)
    protocol, one of the core Internet protocols. It provides source and
    destination ports, basic checksumming, but provides not guarantees
    of delivery, order of packets, or duplicate delivery.
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.src_port = self._io.read_u2be()
        self.dst_port = self._io.read_u2be()
        self.length = self._io.read_u2be()
        self.checksum = self._io.read_u2be()
        self.body = self._io.read_bytes((self.length - 8))


