# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

from . import protocol_body
class Ipv6Packet(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.version = self._io.read_bits_int_be(4)
        self.traffic_class = self._io.read_bits_int_be(8)
        self.flow_label = self._io.read_bits_int_be(20)
        self._io.align_to_byte()
        self.payload_length = self._io.read_u2be()
        self.next_header_type = self._io.read_u1()
        self.hop_limit = self._io.read_u1()
        self.src_ipv6_addr = self._io.read_bytes(16)
        self.dst_ipv6_addr = self._io.read_bytes(16)
        self.next_header = protocol_body.ProtocolBody(self.next_header_type, self._io)
        self.rest = self._io.read_bytes_full()


