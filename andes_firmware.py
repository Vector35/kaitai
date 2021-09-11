# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class AndesFirmware(KaitaiStruct):
    """Firmware image found with MediaTek MT76xx wifi chipsets."""
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self._raw_image_header = self._io.read_bytes(32)
        _io__raw_image_header = KaitaiStream(BytesIO(self._raw_image_header))
        self.image_header = AndesFirmware.ImageHeader(_io__raw_image_header, self, self._root)
        self.ilm = self._io.read_bytes(self.image_header.ilm_len)
        self.dlm = self._io.read_bytes(self.image_header.dlm_len)

    class ImageHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ilm_len = self._io.read_u4le()
            self.dlm_len = self._io.read_u4le()
            self.fw_ver = self._io.read_u2le()
            self.build_ver = self._io.read_u2le()
            self.extra = self._io.read_u4le()
            self.build_time = (self._io.read_bytes(16)).decode(u"UTF-8")



