# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class TcpSegment(KaitaiStruct):
    """TCP is one of the core Internet protocols on transport layer (AKA
    OSI layer 4), providing stateful connections with error checking,
    guarantees of delivery, order of segments and avoidance of duplicate
    delivery.
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.src_port = self._io.read_u2be()
        self.dst_port = self._io.read_u2be()
        self.seq_num = self._io.read_u4be()
        self.ack_num = self._io.read_u4be()
        self.b12 = self._io.read_u1()
        self.b13 = self._io.read_u1()
        self.window_size = self._io.read_u2be()
        self.checksum = self._io.read_u2be()
        self.urgent_pointer = self._io.read_u2be()
        self.body = self._io.read_bytes_full()


