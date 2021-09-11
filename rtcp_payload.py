# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class RtcpPayload(KaitaiStruct):
    """RTCP is the Real-Time Control Protocol.
    
    .. seealso::
       Source - https://tools.ietf.org/html/rfc3550
    """

    class PayloadType(Enum):
        fir = 192
        nack = 193
        ij = 195
        sr = 200
        rr = 201
        sdes = 202
        bye = 203
        app = 204
        rtpfb = 205
        psfb = 206
        xr = 207
        avb = 208
        rsi = 209

    class SdesSubtype(Enum):
        pad = 0
        cname = 1
        name = 2
        email = 3
        phone = 4
        loc = 5
        tool = 6
        note = 7
        priv = 8

    class PsfbSubtype(Enum):
        pli = 1
        sli = 2
        rpsi = 3
        fir = 4
        tstr = 5
        tstn = 6
        vbcm = 7
        afb = 15

    class RtpfbSubtype(Enum):
        nack = 1
        tmmbr = 3
        tmmbn = 4
        rrr = 5
        transport_feedback = 15
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.rtcp_packets = []
        i = 0
        while not self._io.is_eof():
            self.rtcp_packets.append(RtcpPayload.RtcpPacket(self._io, self, self._root))
            i += 1


    class PsfbAfbRembPacket(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_ssrc = self._io.read_u1()
            self.br_exp = self._io.read_bits_int_be(6)
            self.br_mantissa = self._io.read_bits_int_be(18)
            self._io.align_to_byte()
            self.ssrc_list = [None] * (self.num_ssrc)
            for i in range(self.num_ssrc):
                self.ssrc_list[i] = self._io.read_u4be()


        @property
        def max_total_bitrate(self):
            if hasattr(self, '_m_max_total_bitrate'):
                return self._m_max_total_bitrate if hasattr(self, '_m_max_total_bitrate') else None

            self._m_max_total_bitrate = (self.br_mantissa * (1 << self.br_exp))
            return self._m_max_total_bitrate if hasattr(self, '_m_max_total_bitrate') else None


    class SrPacket(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ssrc = self._io.read_u4be()
            self.ntp_msw = self._io.read_u4be()
            self.ntp_lsw = self._io.read_u4be()
            self.rtp_timestamp = self._io.read_u4be()
            self.sender_packet_count = self._io.read_u4be()
            self.sender_octet_count = self._io.read_u4be()
            self.report_block = [None] * (self._parent.subtype)
            for i in range(self._parent.subtype):
                self.report_block[i] = RtcpPayload.ReportBlock(self._io, self, self._root)


        @property
        def ntp(self):
            if hasattr(self, '_m_ntp'):
                return self._m_ntp if hasattr(self, '_m_ntp') else None

            self._m_ntp = ((self.ntp_msw << 32) & self.ntp_lsw)
            return self._m_ntp if hasattr(self, '_m_ntp') else None


    class RrPacket(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ssrc = self._io.read_u4be()
            self.report_block = [None] * (self._parent.subtype)
            for i in range(self._parent.subtype):
                self.report_block[i] = RtcpPayload.ReportBlock(self._io, self, self._root)



    class RtcpPacket(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.version = self._io.read_bits_int_be(2)
            self.padding = self._io.read_bits_int_be(1) != 0
            self.subtype = self._io.read_bits_int_be(5)
            self._io.align_to_byte()
            self.payload_type = KaitaiStream.resolve_enum(RtcpPayload.PayloadType, self._io.read_u1())
            self.length = self._io.read_u2be()
            _on = self.payload_type
            if _on == RtcpPayload.PayloadType.sr:
                self._raw_body = self._io.read_bytes((4 * self.length))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = RtcpPayload.SrPacket(_io__raw_body, self, self._root)
            elif _on == RtcpPayload.PayloadType.psfb:
                self._raw_body = self._io.read_bytes((4 * self.length))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = RtcpPayload.PsfbPacket(_io__raw_body, self, self._root)
            elif _on == RtcpPayload.PayloadType.rr:
                self._raw_body = self._io.read_bytes((4 * self.length))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = RtcpPayload.RrPacket(_io__raw_body, self, self._root)
            elif _on == RtcpPayload.PayloadType.rtpfb:
                self._raw_body = self._io.read_bytes((4 * self.length))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = RtcpPayload.RtpfbPacket(_io__raw_body, self, self._root)
            elif _on == RtcpPayload.PayloadType.sdes:
                self._raw_body = self._io.read_bytes((4 * self.length))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = RtcpPayload.SdesPacket(_io__raw_body, self, self._root)
            else:
                self.body = self._io.read_bytes((4 * self.length))


    class SdesTlv(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.type = KaitaiStream.resolve_enum(RtcpPayload.SdesSubtype, self._io.read_u1())
            if self.type != RtcpPayload.SdesSubtype.pad:
                self.length = self._io.read_u1()

            if self.type != RtcpPayload.SdesSubtype.pad:
                self.value = self._io.read_bytes(self.length)



    class ReportBlock(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ssrc_source = self._io.read_u4be()
            self.lost_val = self._io.read_u1()
            self.highest_seq_num_received = self._io.read_u4be()
            self.interarrival_jitter = self._io.read_u4be()
            self.lsr = self._io.read_u4be()
            self.dlsr = self._io.read_u4be()

        @property
        def fraction_lost(self):
            if hasattr(self, '_m_fraction_lost'):
                return self._m_fraction_lost if hasattr(self, '_m_fraction_lost') else None

            self._m_fraction_lost = (self.lost_val >> 24)
            return self._m_fraction_lost if hasattr(self, '_m_fraction_lost') else None

        @property
        def cumulative_packets_lost(self):
            if hasattr(self, '_m_cumulative_packets_lost'):
                return self._m_cumulative_packets_lost if hasattr(self, '_m_cumulative_packets_lost') else None

            self._m_cumulative_packets_lost = (self.lost_val & 16777215)
            return self._m_cumulative_packets_lost if hasattr(self, '_m_cumulative_packets_lost') else None


    class RtpfbTransportFeedbackPacket(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_sequence_number = self._io.read_u2be()
            self.packet_status_count = self._io.read_u2be()
            self.b4 = self._io.read_u4be()
            self.remaining = self._io.read_bytes_full()

        @property
        def reference_time(self):
            if hasattr(self, '_m_reference_time'):
                return self._m_reference_time if hasattr(self, '_m_reference_time') else None

            self._m_reference_time = (self.b4 >> 8)
            return self._m_reference_time if hasattr(self, '_m_reference_time') else None

        @property
        def fb_pkt_count(self):
            if hasattr(self, '_m_fb_pkt_count'):
                return self._m_fb_pkt_count if hasattr(self, '_m_fb_pkt_count') else None

            self._m_fb_pkt_count = (self.b4 & 255)
            return self._m_fb_pkt_count if hasattr(self, '_m_fb_pkt_count') else None

        @property
        def packet_status(self):
            if hasattr(self, '_m_packet_status'):
                return self._m_packet_status if hasattr(self, '_m_packet_status') else None

            self._m_packet_status = self._io.read_bytes(0)
            return self._m_packet_status if hasattr(self, '_m_packet_status') else None

        @property
        def recv_delta(self):
            if hasattr(self, '_m_recv_delta'):
                return self._m_recv_delta if hasattr(self, '_m_recv_delta') else None

            self._m_recv_delta = self._io.read_bytes(0)
            return self._m_recv_delta if hasattr(self, '_m_recv_delta') else None


    class PsfbPacket(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ssrc = self._io.read_u4be()
            self.ssrc_media_source = self._io.read_u4be()
            _on = self.fmt
            if _on == RtcpPayload.PsfbSubtype.afb:
                self._raw_fci_block = self._io.read_bytes_full()
                _io__raw_fci_block = KaitaiStream(BytesIO(self._raw_fci_block))
                self.fci_block = RtcpPayload.PsfbAfbPacket(_io__raw_fci_block, self, self._root)
            else:
                self.fci_block = self._io.read_bytes_full()

        @property
        def fmt(self):
            if hasattr(self, '_m_fmt'):
                return self._m_fmt if hasattr(self, '_m_fmt') else None

            self._m_fmt = KaitaiStream.resolve_enum(RtcpPayload.PsfbSubtype, self._parent.subtype)
            return self._m_fmt if hasattr(self, '_m_fmt') else None


    class SourceChunk(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ssrc = self._io.read_u4be()
            self.sdes_tlv = []
            i = 0
            while not self._io.is_eof():
                self.sdes_tlv.append(RtcpPayload.SdesTlv(self._io, self, self._root))
                i += 1



    class SdesPacket(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.source_chunk = [None] * (self.source_count)
            for i in range(self.source_count):
                self.source_chunk[i] = RtcpPayload.SourceChunk(self._io, self, self._root)


        @property
        def source_count(self):
            if hasattr(self, '_m_source_count'):
                return self._m_source_count if hasattr(self, '_m_source_count') else None

            self._m_source_count = self._parent.subtype
            return self._m_source_count if hasattr(self, '_m_source_count') else None


    class RtpfbPacket(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ssrc = self._io.read_u4be()
            self.ssrc_media_source = self._io.read_u4be()
            _on = self.fmt
            if _on == RtcpPayload.RtpfbSubtype.transport_feedback:
                self._raw_fci_block = self._io.read_bytes_full()
                _io__raw_fci_block = KaitaiStream(BytesIO(self._raw_fci_block))
                self.fci_block = RtcpPayload.RtpfbTransportFeedbackPacket(_io__raw_fci_block, self, self._root)
            else:
                self.fci_block = self._io.read_bytes_full()

        @property
        def fmt(self):
            if hasattr(self, '_m_fmt'):
                return self._m_fmt if hasattr(self, '_m_fmt') else None

            self._m_fmt = KaitaiStream.resolve_enum(RtcpPayload.RtpfbSubtype, self._parent.subtype)
            return self._m_fmt if hasattr(self, '_m_fmt') else None


    class PacketStatusChunk(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.t = self._io.read_bits_int_be(1) != 0
            if int(self.t) == 0:
                self.s2 = self._io.read_bits_int_be(2)

            if int(self.t) == 1:
                self.s1 = self._io.read_bits_int_be(1) != 0

            if int(self.t) == 0:
                self.rle = self._io.read_bits_int_be(13)

            if int(self.t) == 1:
                self.symbol_list = self._io.read_bits_int_be(14)


        @property
        def s(self):
            if hasattr(self, '_m_s'):
                return self._m_s if hasattr(self, '_m_s') else None

            self._m_s = (self.s2 if int(self.t) == 0 else (1 if int(self.s1) == 0 else 0))
            return self._m_s if hasattr(self, '_m_s') else None


    class PsfbAfbPacket(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.uid = self._io.read_u4be()
            _on = self.uid
            if _on == 1380273474:
                self._raw_contents = self._io.read_bytes_full()
                _io__raw_contents = KaitaiStream(BytesIO(self._raw_contents))
                self.contents = RtcpPayload.PsfbAfbRembPacket(_io__raw_contents, self, self._root)
            else:
                self.contents = self._io.read_bytes_full()



