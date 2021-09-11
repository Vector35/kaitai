# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

from . import ipv4_packet
from . import ipv6_packet
class EthernetFrame(KaitaiStruct):
    """Ethernet frame is a OSI data link layer (layer 2) protocol data unit
    for Ethernet networks. In practice, many other networks and/or
    in-file dumps adopted the same format for encapsulation purposes.
    
    .. seealso::
       Source - https://ieeexplore.ieee.org/document/7428776
    """

    class EtherTypeEnum(Enum):
        ipv4 = 2048
        x_75_internet = 2049
        nbs_internet = 2050
        ecma_internet = 2051
        chaosnet = 2052
        x_25_level_3 = 2053
        arp = 2054
        ieee_802_1q_tpid = 33024
        ipv6 = 34525
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.dst_mac = self._io.read_bytes(6)
        self.src_mac = self._io.read_bytes(6)
        self.ether_type_1 = KaitaiStream.resolve_enum(EthernetFrame.EtherTypeEnum, self._io.read_u2be())
        if self.ether_type_1 == EthernetFrame.EtherTypeEnum.ieee_802_1q_tpid:
            self.tci = EthernetFrame.TagControlInfo(self._io, self, self._root)

        if self.ether_type_1 == EthernetFrame.EtherTypeEnum.ieee_802_1q_tpid:
            self.ether_type_2 = KaitaiStream.resolve_enum(EthernetFrame.EtherTypeEnum, self._io.read_u2be())

        _on = self.ether_type
        if _on == EthernetFrame.EtherTypeEnum.ipv4:
            self._raw_body = self._io.read_bytes_full()
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = ipv4_packet.Ipv4Packet(_io__raw_body)
        elif _on == EthernetFrame.EtherTypeEnum.ipv6:
            self._raw_body = self._io.read_bytes_full()
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = ipv6_packet.Ipv6Packet(_io__raw_body)
        else:
            self.body = self._io.read_bytes_full()

    class TagControlInfo(KaitaiStruct):
        """Tag Control Information (TCI) is an extension of IEEE 802.1Q to
        support VLANs on normal IEEE 802.3 Ethernet network.
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.priority = self._io.read_bits_int_be(3)
            self.drop_eligible = self._io.read_bits_int_be(1) != 0
            self.vlan_id = self._io.read_bits_int_be(12)


    @property
    def ether_type(self):
        """Ether type can be specied in several places in the frame. If
        first location bears special marker (0x8100), then it is not the
        real ether frame yet, an additional payload (`tci`) is expected
        and real ether type is upcoming next.
        """
        if hasattr(self, '_m_ether_type'):
            return self._m_ether_type if hasattr(self, '_m_ether_type') else None

        self._m_ether_type = (self.ether_type_2 if self.ether_type_1 == EthernetFrame.EtherTypeEnum.ieee_802_1q_tpid else self.ether_type_1)
        return self._m_ether_type if hasattr(self, '_m_ether_type') else None


