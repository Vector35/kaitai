# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class SudoersTs(KaitaiStruct):
    """This spec can be used to parse sudo time stamp files located in directories
    such as /run/sudo/ts/$USER or /var/lib/sudo/ts/$USER.
    
    .. seealso::
       Source - https://www.sudo.ws/man/1.8.27/sudoers_timestamp.man.html
    """

    class TsType(Enum):
        global = 1
        tty = 2
        ppid = 3
        lockexcl = 4
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.records = []
        i = 0
        while not self._io.is_eof():
            self.records.append(SudoersTs.Record(self._io, self, self._root))
            i += 1


    class RecordV2(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.type = KaitaiStream.resolve_enum(SudoersTs.TsType, self._io.read_u2le())
            self.flags = SudoersTs.TsFlag(self._io, self, self._root)
            self.auth_uid = self._io.read_u4le()
            self.sid = self._io.read_u4le()
            self.start_time = SudoersTs.Timespec(self._io, self, self._root)
            self.ts = SudoersTs.Timespec(self._io, self, self._root)
            if self.type == SudoersTs.TsType.tty:
                self.ttydev = self._io.read_u4le()

            if self.type == SudoersTs.TsType.ppid:
                self.ppid = self._io.read_u4le()



    class TsFlag(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.reserved0 = self._io.read_bits_int_be(6)
            self.anyuid = self._io.read_bits_int_be(1) != 0
            self.disabled = self._io.read_bits_int_be(1) != 0
            self.reserved1 = self._io.read_bits_int_be(8)


    class RecordV1(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.type = KaitaiStream.resolve_enum(SudoersTs.TsType, self._io.read_u2le())
            self.flags = SudoersTs.TsFlag(self._io, self, self._root)
            self.auth_uid = self._io.read_u4le()
            self.sid = self._io.read_u4le()
            self.ts = SudoersTs.Timespec(self._io, self, self._root)
            if self.type == SudoersTs.TsType.tty:
                self.ttydev = self._io.read_u4le()

            if self.type == SudoersTs.TsType.ppid:
                self.ppid = self._io.read_u4le()



    class Timespec(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.sec = self._io.read_s8le()
            self.nsec = self._io.read_s8le()


    class Record(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.version = self._io.read_u2le()
            self.len_record = self._io.read_u2le()
            _on = self.version
            if _on == 1:
                self._raw_payload = self._io.read_bytes((self.len_record - 4))
                _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
                self.payload = SudoersTs.RecordV1(_io__raw_payload, self, self._root)
            elif _on == 2:
                self._raw_payload = self._io.read_bytes((self.len_record - 4))
                _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
                self.payload = SudoersTs.RecordV2(_io__raw_payload, self, self._root)
            else:
                self.payload = self._io.read_bytes((self.len_record - 4))



