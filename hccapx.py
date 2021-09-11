# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Hccapx(KaitaiStruct):
    """Native format of Hashcat password "recovery" utility
    
    .. seealso::
       Source - https://hashcat.net/wiki/doku.php?id=hccapx
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.records = []
        i = 0
        while not self._io.is_eof():
            self.records.append(Hccapx.HccapxRecord(self._io, self, self._root))
            i += 1


    class HccapxRecord(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(4)
            if not self.magic == b"\x48\x43\x50\x58":
                raise kaitaistruct.ValidationNotEqualError(b"\x48\x43\x50\x58", self.magic, self._io, u"/types/hccapx_record/seq/0")
            self.version = self._io.read_u4le()
            self.ignore_replay_counter = self._io.read_bits_int_be(1) != 0
            self.message_pair = self._io.read_bits_int_be(7)
            self._io.align_to_byte()
            self.len_essid = self._io.read_u1()
            self.essid = self._io.read_bytes(self.len_essid)
            self.padding1 = self._io.read_bytes((32 - self.len_essid))
            self.keyver = self._io.read_u1()
            self.keymic = self._io.read_bytes(16)
            self.mac_ap = self._io.read_bytes(6)
            self.nonce_ap = self._io.read_bytes(32)
            self.mac_station = self._io.read_bytes(6)
            self.nonce_station = self._io.read_bytes(32)
            self.len_eapol = self._io.read_u2le()
            self.eapol = self._io.read_bytes(self.len_eapol)
            self.padding2 = self._io.read_bytes((256 - self.len_eapol))



