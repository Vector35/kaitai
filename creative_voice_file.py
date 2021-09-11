# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class CreativeVoiceFile(KaitaiStruct):
    """Creative Voice File is a container file format for digital audio
    wave data. Initial revisions were able to support only unsigned
    8-bit PCM and ADPCM data, later versions were revised to add support
    for 16-bit PCM and a-law / u-law formats.
    
    This format was actively used in 1990s, around the advent of
    Creative's sound cards (Sound Blaster family). It was a popular
    choice for a digital sound container in lots of games and multimedia
    software due to simplicity and availability of Creative's recording
    / editing tools.
    
    .. seealso::
       Source - https://wiki.multimedia.cx/index.php?title=Creative_Voice
    """

    class BlockTypes(Enum):
        terminator = 0
        sound_data = 1
        sound_data_cont = 2
        silence = 3
        marker = 4
        text = 5
        repeat_start = 6
        repeat_end = 7
        extra_info = 8
        sound_data_new = 9

    class Codecs(Enum):
        pcm_8bit_unsigned = 0
        adpcm_4bit = 1
        adpcm_2_6bit = 2
        adpcm_2_bit = 3
        pcm_16bit_signed = 4
        alaw = 6
        ulaw = 7
        adpcm_4_to_16bit = 512
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(20)
        if not self.magic == b"\x43\x72\x65\x61\x74\x69\x76\x65\x20\x56\x6F\x69\x63\x65\x20\x46\x69\x6C\x65\x1A":
            raise kaitaistruct.ValidationNotEqualError(b"\x43\x72\x65\x61\x74\x69\x76\x65\x20\x56\x6F\x69\x63\x65\x20\x46\x69\x6C\x65\x1A", self.magic, self._io, u"/seq/0")
        self.header_size = self._io.read_u2le()
        self.version = self._io.read_u2le()
        self.checksum = self._io.read_u2le()
        self.blocks = []
        i = 0
        while not self._io.is_eof():
            self.blocks.append(CreativeVoiceFile.Block(self._io, self, self._root))
            i += 1


    class BlockMarker(KaitaiStruct):
        """
        .. seealso::
           Source - https://wiki.multimedia.cx/index.php?title=Creative_Voice#Block_type_0x04:_Marker
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.marker_id = self._io.read_u2le()


    class BlockSilence(KaitaiStruct):
        """
        .. seealso::
           Source - https://wiki.multimedia.cx/index.php?title=Creative_Voice#Block_type_0x03:_Silence
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.duration_samples = self._io.read_u2le()
            self.freq_div = self._io.read_u1()

        @property
        def sample_rate(self):
            if hasattr(self, '_m_sample_rate'):
                return self._m_sample_rate if hasattr(self, '_m_sample_rate') else None

            self._m_sample_rate = (1000000.0 / (256 - self.freq_div))
            return self._m_sample_rate if hasattr(self, '_m_sample_rate') else None

        @property
        def duration_sec(self):
            """Duration of silence, in seconds."""
            if hasattr(self, '_m_duration_sec'):
                return self._m_duration_sec if hasattr(self, '_m_duration_sec') else None

            self._m_duration_sec = (self.duration_samples / self.sample_rate)
            return self._m_duration_sec if hasattr(self, '_m_duration_sec') else None


    class BlockSoundDataNew(KaitaiStruct):
        """
        .. seealso::
           Source - https://wiki.multimedia.cx/index.php?title=Creative_Voice#Block_type_0x09:_Sound_data_.28New_format.29
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.sample_rate = self._io.read_u4le()
            self.bits_per_sample = self._io.read_u1()
            self.num_channels = self._io.read_u1()
            self.codec = KaitaiStream.resolve_enum(CreativeVoiceFile.Codecs, self._io.read_u2le())
            self.reserved = self._io.read_bytes(4)
            self.wave = self._io.read_bytes_full()


    class Block(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.block_type = KaitaiStream.resolve_enum(CreativeVoiceFile.BlockTypes, self._io.read_u1())
            if self.block_type != CreativeVoiceFile.BlockTypes.terminator:
                self.body_size1 = self._io.read_u2le()

            if self.block_type != CreativeVoiceFile.BlockTypes.terminator:
                self.body_size2 = self._io.read_u1()

            if self.block_type != CreativeVoiceFile.BlockTypes.terminator:
                _on = self.block_type
                if _on == CreativeVoiceFile.BlockTypes.sound_data_new:
                    self._raw_body = self._io.read_bytes(self.body_size)
                    _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                    self.body = CreativeVoiceFile.BlockSoundDataNew(_io__raw_body, self, self._root)
                elif _on == CreativeVoiceFile.BlockTypes.repeat_start:
                    self._raw_body = self._io.read_bytes(self.body_size)
                    _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                    self.body = CreativeVoiceFile.BlockRepeatStart(_io__raw_body, self, self._root)
                elif _on == CreativeVoiceFile.BlockTypes.marker:
                    self._raw_body = self._io.read_bytes(self.body_size)
                    _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                    self.body = CreativeVoiceFile.BlockMarker(_io__raw_body, self, self._root)
                elif _on == CreativeVoiceFile.BlockTypes.sound_data:
                    self._raw_body = self._io.read_bytes(self.body_size)
                    _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                    self.body = CreativeVoiceFile.BlockSoundData(_io__raw_body, self, self._root)
                elif _on == CreativeVoiceFile.BlockTypes.extra_info:
                    self._raw_body = self._io.read_bytes(self.body_size)
                    _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                    self.body = CreativeVoiceFile.BlockExtraInfo(_io__raw_body, self, self._root)
                elif _on == CreativeVoiceFile.BlockTypes.silence:
                    self._raw_body = self._io.read_bytes(self.body_size)
                    _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                    self.body = CreativeVoiceFile.BlockSilence(_io__raw_body, self, self._root)
                else:
                    self.body = self._io.read_bytes(self.body_size)


        @property
        def body_size(self):
            """body_size is a 24-bit little-endian integer, so we're
            emulating that by adding two standard-sized integers
            (body_size1 and body_size2).
            """
            if hasattr(self, '_m_body_size'):
                return self._m_body_size if hasattr(self, '_m_body_size') else None

            if self.block_type != CreativeVoiceFile.BlockTypes.terminator:
                self._m_body_size = (self.body_size1 + (self.body_size2 << 16))

            return self._m_body_size if hasattr(self, '_m_body_size') else None


    class BlockRepeatStart(KaitaiStruct):
        """
        .. seealso::
           Source - https://wiki.multimedia.cx/index.php?title=Creative_Voice#Block_type_0x06:_Repeat_start
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.repeat_count_1 = self._io.read_u2le()


    class BlockSoundData(KaitaiStruct):
        """
        .. seealso::
           Source - https://wiki.multimedia.cx/index.php?title=Creative_Voice#Block_type_0x01:_Sound_data
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.freq_div = self._io.read_u1()
            self.codec = KaitaiStream.resolve_enum(CreativeVoiceFile.Codecs, self._io.read_u1())
            self.wave = self._io.read_bytes_full()

        @property
        def sample_rate(self):
            if hasattr(self, '_m_sample_rate'):
                return self._m_sample_rate if hasattr(self, '_m_sample_rate') else None

            self._m_sample_rate = (1000000.0 / (256 - self.freq_div))
            return self._m_sample_rate if hasattr(self, '_m_sample_rate') else None


    class BlockExtraInfo(KaitaiStruct):
        """
        .. seealso::
           Source - https://wiki.multimedia.cx/index.php?title=Creative_Voice#Block_type_0x08:_Extra_info
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.freq_div = self._io.read_u2le()
            self.codec = KaitaiStream.resolve_enum(CreativeVoiceFile.Codecs, self._io.read_u1())
            self.num_channels_1 = self._io.read_u1()

        @property
        def num_channels(self):
            """Number of channels (1 = mono, 2 = stereo)."""
            if hasattr(self, '_m_num_channels'):
                return self._m_num_channels if hasattr(self, '_m_num_channels') else None

            self._m_num_channels = (self.num_channels_1 + 1)
            return self._m_num_channels if hasattr(self, '_m_num_channels') else None

        @property
        def sample_rate(self):
            if hasattr(self, '_m_sample_rate'):
                return self._m_sample_rate if hasattr(self, '_m_sample_rate') else None

            self._m_sample_rate = (256000000.0 / (self.num_channels * (65536 - self.freq_div)))
            return self._m_sample_rate if hasattr(self, '_m_sample_rate') else None



