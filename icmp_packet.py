# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class IcmpPacket(KaitaiStruct):

    class IcmpTypeEnum(Enum):
        echo_reply = 0
        destination_unreachable = 3
        source_quench = 4
        redirect = 5
        echo = 8
        time_exceeded = 11
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.icmp_type = KaitaiStream.resolve_enum(IcmpPacket.IcmpTypeEnum, self._io.read_u1())
        if self.icmp_type == IcmpPacket.IcmpTypeEnum.destination_unreachable:
            self.destination_unreachable = IcmpPacket.DestinationUnreachableMsg(self._io, self, self._root)

        if self.icmp_type == IcmpPacket.IcmpTypeEnum.time_exceeded:
            self.time_exceeded = IcmpPacket.TimeExceededMsg(self._io, self, self._root)

        if  ((self.icmp_type == IcmpPacket.IcmpTypeEnum.echo) or (self.icmp_type == IcmpPacket.IcmpTypeEnum.echo_reply)) :
            self.echo = IcmpPacket.EchoMsg(self._io, self, self._root)


    class DestinationUnreachableMsg(KaitaiStruct):

        class DestinationUnreachableCode(Enum):
            net_unreachable = 0
            host_unreachable = 1
            protocol_unreachable = 2
            port_unreachable = 3
            fragmentation_needed_and_df_set = 4
            source_route_failed = 5
            dst_net_unkown = 6
            sdt_host_unkown = 7
            src_isolated = 8
            net_prohibited_by_admin = 9
            host_prohibited_by_admin = 10
            net_unreachable_for_tos = 11
            host_unreachable_for_tos = 12
            communication_prohibited_by_admin = 13
            host_precedence_violation = 14
            precedence_cuttoff_in_effect = 15
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.code = KaitaiStream.resolve_enum(IcmpPacket.DestinationUnreachableMsg.DestinationUnreachableCode, self._io.read_u1())
            self.checksum = self._io.read_u2be()


    class TimeExceededMsg(KaitaiStruct):

        class TimeExceededCode(Enum):
            time_to_live_exceeded_in_transit = 0
            fragment_reassembly_time_exceeded = 1
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.code = KaitaiStream.resolve_enum(IcmpPacket.TimeExceededMsg.TimeExceededCode, self._io.read_u1())
            self.checksum = self._io.read_u2be()


    class EchoMsg(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.code = self._io.read_bytes(1)
            if not self.code == b"\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00", self.code, self._io, u"/types/echo_msg/seq/0")
            self.checksum = self._io.read_u2be()
            self.identifier = self._io.read_u2be()
            self.seq_num = self._io.read_u2be()
            self.data = self._io.read_bytes_full()



