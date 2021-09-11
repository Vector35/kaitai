# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Vp8Ivf(KaitaiStruct):
    """IVF is a simple container format for raw VP8 data, which is an open
    and royalty-free video compression format, currently developed by
    Google.
    
    Test .ivf files are available at https://chromium.googlesource.com/webm/vp8-test-vectors
    
    .. seealso::
       Source - https://wiki.multimedia.cx/index.php/IVF
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic1 = self._io.read_bytes(4)
        if not self.magic1 == b"\x44\x4B\x49\x46":
            raise kaitaistruct.ValidationNotEqualError(b"\x44\x4B\x49\x46", self.magic1, self._io, u"/seq/0")
        self.version = self._io.read_u2le()
        self.len_header = self._io.read_u2le()
        self.codec = self._io.read_bytes(4)
        if not self.codec == b"\x56\x50\x38\x30":
            raise kaitaistruct.ValidationNotEqualError(b"\x56\x50\x38\x30", self.codec, self._io, u"/seq/3")
        self.width = self._io.read_u2le()
        self.height = self._io.read_u2le()
        self.framerate = self._io.read_u4le()
        self.timescale = self._io.read_u4le()
        self.num_frames = self._io.read_u4le()
        self.unused = self._io.read_u4le()
        self.image_data = [None] * (self.num_frames)
        for i in range(self.num_frames):
            self.image_data[i] = Vp8Ivf.Blocks(self._io, self, self._root)


    class Blocks(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.entries = Vp8Ivf.Block(self._io, self, self._root)


    class Block(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len_frame = self._io.read_u4le()
            self.timestamp = self._io.read_u8le()
            self.framedata = self._io.read_bytes(self.len_frame)



