# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Ogg(KaitaiStruct):
    """Ogg is a popular media container format, which provides basic
    streaming / buffering mechanisms and is content-agnostic. Most
    popular codecs that are used within Ogg streams are Vorbis (thus
    making Ogg/Vorbis streams) and Theora (Ogg/Theora).
    
    Ogg stream is a sequence Ogg pages. They can be read sequentially,
    or one can jump into arbitrary stream location and scan for "OggS"
    sync code to find the beginning of a new Ogg page and continue
    decoding the stream contents from that one.
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.pages = []
        i = 0
        while not self._io.is_eof():
            self.pages.append(Ogg.Page(self._io, self, self._root))
            i += 1


    class Page(KaitaiStruct):
        """Ogg page is a basic unit of data in an Ogg bitstream, usually
        it's around 4-8 KB, with a maximum size of 65307 bytes.
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.sync_code = self._io.read_bytes(4)
            if not self.sync_code == b"\x4F\x67\x67\x53":
                raise kaitaistruct.ValidationNotEqualError(b"\x4F\x67\x67\x53", self.sync_code, self._io, u"/types/page/seq/0")
            self.version = self._io.read_bytes(1)
            if not self.version == b"\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00", self.version, self._io, u"/types/page/seq/1")
            self.reserved1 = self._io.read_bits_int_be(5)
            self.is_end_of_stream = self._io.read_bits_int_be(1) != 0
            self.is_beginning_of_stream = self._io.read_bits_int_be(1) != 0
            self.is_continuation = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.granule_pos = self._io.read_u8le()
            self.bitstream_serial = self._io.read_u4le()
            self.page_seq_num = self._io.read_u4le()
            self.crc32 = self._io.read_u4le()
            self.num_segments = self._io.read_u1()
            self.len_segments = [None] * (self.num_segments)
            for i in range(self.num_segments):
                self.len_segments[i] = self._io.read_u1()

            self.segments = [None] * (self.num_segments)
            for i in range(self.num_segments):
                self.segments[i] = self._io.read_bytes(self.len_segments[i])




