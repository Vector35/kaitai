# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

from . import vlq_base128_be
class StandardMidiFile(KaitaiStruct):
    """Standard MIDI file, typically knows just as "MID", is a standard way
    to serialize series of MIDI events, which is a protocol used in many
    music synthesizers to transfer music data: notes being played,
    effects being applied, etc.
    
    Internally, file consists of a header and series of tracks, every
    track listing MIDI events with certain header designating time these
    events are happening.
    
    NOTE: Rarely, MIDI files employ certain stateful compression scheme
    to avoid storing certain elements of further elements, instead
    reusing them from events which happened earlier in the
    stream. Kaitai Struct (as of v0.9) is currently unable to parse
    these, but files employing this mechanism are relatively rare.
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.hdr = StandardMidiFile.Header(self._io, self, self._root)
        self.tracks = [None] * (self.hdr.num_tracks)
        for i in range(self.hdr.num_tracks):
            self.tracks[i] = StandardMidiFile.Track(self._io, self, self._root)


    class TrackEvents(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.event = []
            i = 0
            while not self._io.is_eof():
                self.event.append(StandardMidiFile.TrackEvent(self._io, self, self._root))
                i += 1



    class TrackEvent(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.v_time = vlq_base128_be.VlqBase128Be(self._io)
            self.event_header = self._io.read_u1()
            if self.event_header == 255:
                self.meta_event_body = StandardMidiFile.MetaEventBody(self._io, self, self._root)

            if self.event_header == 240:
                self.sysex_body = StandardMidiFile.SysexEventBody(self._io, self, self._root)

            _on = self.event_type
            if _on == 224:
                self.event_body = StandardMidiFile.PitchBendEvent(self._io, self, self._root)
            elif _on == 144:
                self.event_body = StandardMidiFile.NoteOnEvent(self._io, self, self._root)
            elif _on == 208:
                self.event_body = StandardMidiFile.ChannelPressureEvent(self._io, self, self._root)
            elif _on == 192:
                self.event_body = StandardMidiFile.ProgramChangeEvent(self._io, self, self._root)
            elif _on == 160:
                self.event_body = StandardMidiFile.PolyphonicPressureEvent(self._io, self, self._root)
            elif _on == 176:
                self.event_body = StandardMidiFile.ControllerEvent(self._io, self, self._root)
            elif _on == 128:
                self.event_body = StandardMidiFile.NoteOffEvent(self._io, self, self._root)

        @property
        def event_type(self):
            if hasattr(self, '_m_event_type'):
                return self._m_event_type if hasattr(self, '_m_event_type') else None

            self._m_event_type = (self.event_header & 240)
            return self._m_event_type if hasattr(self, '_m_event_type') else None

        @property
        def channel(self):
            if hasattr(self, '_m_channel'):
                return self._m_channel if hasattr(self, '_m_channel') else None

            if self.event_type != 240:
                self._m_channel = (self.event_header & 15)

            return self._m_channel if hasattr(self, '_m_channel') else None


    class PitchBendEvent(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.b1 = self._io.read_u1()
            self.b2 = self._io.read_u1()

        @property
        def bend_value(self):
            if hasattr(self, '_m_bend_value'):
                return self._m_bend_value if hasattr(self, '_m_bend_value') else None

            self._m_bend_value = (((self.b2 << 7) + self.b1) - 16384)
            return self._m_bend_value if hasattr(self, '_m_bend_value') else None

        @property
        def adj_bend_value(self):
            if hasattr(self, '_m_adj_bend_value'):
                return self._m_adj_bend_value if hasattr(self, '_m_adj_bend_value') else None

            self._m_adj_bend_value = (self.bend_value - 16384)
            return self._m_adj_bend_value if hasattr(self, '_m_adj_bend_value') else None


    class ProgramChangeEvent(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.program = self._io.read_u1()


    class NoteOnEvent(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.note = self._io.read_u1()
            self.velocity = self._io.read_u1()


    class PolyphonicPressureEvent(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.note = self._io.read_u1()
            self.pressure = self._io.read_u1()


    class Track(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(4)
            if not self.magic == b"\x4D\x54\x72\x6B":
                raise kaitaistruct.ValidationNotEqualError(b"\x4D\x54\x72\x6B", self.magic, self._io, u"/types/track/seq/0")
            self.len_events = self._io.read_u4be()
            self._raw_events = self._io.read_bytes(self.len_events)
            _io__raw_events = KaitaiStream(BytesIO(self._raw_events))
            self.events = StandardMidiFile.TrackEvents(_io__raw_events, self, self._root)


    class MetaEventBody(KaitaiStruct):

        class MetaTypeEnum(Enum):
            sequence_number = 0
            text_event = 1
            copyright = 2
            sequence_track_name = 3
            instrument_name = 4
            lyric_text = 5
            marker_text = 6
            cue_point = 7
            midi_channel_prefix_assignment = 32
            end_of_track = 47
            tempo = 81
            smpte_offset = 84
            time_signature = 88
            key_signature = 89
            sequencer_specific_event = 127
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.meta_type = KaitaiStream.resolve_enum(StandardMidiFile.MetaEventBody.MetaTypeEnum, self._io.read_u1())
            self.len = vlq_base128_be.VlqBase128Be(self._io)
            self.body = self._io.read_bytes(self.len.value)


    class ControllerEvent(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.controller = self._io.read_u1()
            self.value = self._io.read_u1()


    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(4)
            if not self.magic == b"\x4D\x54\x68\x64":
                raise kaitaistruct.ValidationNotEqualError(b"\x4D\x54\x68\x64", self.magic, self._io, u"/types/header/seq/0")
            self.len_header = self._io.read_u4be()
            self.format = self._io.read_u2be()
            self.num_tracks = self._io.read_u2be()
            self.division = self._io.read_s2be()


    class SysexEventBody(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len = vlq_base128_be.VlqBase128Be(self._io)
            self.data = self._io.read_bytes(self.len.value)


    class NoteOffEvent(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.note = self._io.read_u1()
            self.velocity = self._io.read_u1()


    class ChannelPressureEvent(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.pressure = self._io.read_u1()



