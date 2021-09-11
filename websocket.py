# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Websocket(KaitaiStruct):
    """The WebSocket protocol establishes a two-way communication channel via TCP.
    Messages are made up of one or more dataframes, and are delineated by
    frames with the `fin` bit set.
    """

    class Opcode(Enum):
        continuation = 0
        text = 1
        binary = 2
        reserved_3 = 3
        reserved_4 = 4
        reserved_5 = 5
        reserved_6 = 6
        reserved_7 = 7
        close = 8
        ping = 9
        pong = 10
        reserved_control_b = 11
        reserved_control_c = 12
        reserved_control_d = 13
        reserved_control_e = 14
        reserved_control_f = 15
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.initial_frame = Websocket.InitialFrame(self._io, self, self._root)
        if self.initial_frame.header.finished != True:
            self.trailing_frames = []
            i = 0
            while True:
                _ = Websocket.Dataframe(self._io, self, self._root)
                self.trailing_frames.append(_)
                if _.header.finished:
                    break
                i += 1


    class FrameHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.finished = self._io.read_bits_int_be(1) != 0
            self.reserved = self._io.read_bits_int_be(3)
            self.opcode = KaitaiStream.resolve_enum(Websocket.Opcode, self._io.read_bits_int_be(4))
            self.is_masked = self._io.read_bits_int_be(1) != 0
            self.len_payload_primary = self._io.read_bits_int_be(7)
            self._io.align_to_byte()
            if self.len_payload_primary == 126:
                self.len_payload_extended_1 = self._io.read_u2be()

            if self.len_payload_primary == 127:
                self.len_payload_extended_2 = self._io.read_u4be()

            if self.is_masked:
                self.mask_key = self._io.read_u4be()


        @property
        def len_payload(self):
            if hasattr(self, '_m_len_payload'):
                return self._m_len_payload if hasattr(self, '_m_len_payload') else None

            self._m_len_payload = (self.len_payload_primary if self.len_payload_primary <= 125 else (self.len_payload_extended_1 if self.len_payload_primary == 126 else self.len_payload_extended_2))
            return self._m_len_payload if hasattr(self, '_m_len_payload') else None


    class InitialFrame(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.header = Websocket.FrameHeader(self._io, self, self._root)
            if self.header.opcode != Websocket.Opcode.text:
                self.payload_bytes = self._io.read_bytes(self.header.len_payload)

            if self.header.opcode == Websocket.Opcode.text:
                self.payload_text = (self._io.read_bytes(self.header.len_payload)).decode(u"UTF-8")



    class Dataframe(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.header = Websocket.FrameHeader(self._io, self, self._root)
            if self._root.initial_frame.header.opcode != Websocket.Opcode.text:
                self.payload_bytes = self._io.read_bytes(self.header.len_payload)

            if self._root.initial_frame.header.opcode == Websocket.Opcode.text:
                self.payload_text = (self._io.read_bytes(self.header.len_payload)).decode(u"UTF-8")




