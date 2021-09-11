# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class AixUtmp(KaitaiStruct):
    """This spec can be used to parse utmp, wtmp and other similar as created by IBM AIX.
    
    .. seealso::
       Source - https://www.ibm.com/support/knowledgecenter/en/ssw_aix_71/com.ibm.aix.files/utmp.h.htm
    """

    class EntryType(Enum):
        empty = 0
        run_lvl = 1
        boot_time = 2
        old_time = 3
        new_time = 4
        init_process = 5
        login_process = 6
        user_process = 7
        dead_process = 8
        accounting = 9
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.records = []
        i = 0
        while not self._io.is_eof():
            self.records.append(AixUtmp.Record(self._io, self, self._root))
            i += 1


    class Record(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.user = (self._io.read_bytes(256)).decode(u"ascii")
            self.inittab_id = (self._io.read_bytes(14)).decode(u"ascii")
            self.device = (self._io.read_bytes(64)).decode(u"ascii")
            self.pid = self._io.read_u8be()
            self.type = KaitaiStream.resolve_enum(AixUtmp.EntryType, self._io.read_s2be())
            self.timestamp = self._io.read_s8be()
            self.exit_status = AixUtmp.ExitStatus(self._io, self, self._root)
            self.hostname = (self._io.read_bytes(256)).decode(u"ascii")
            self.dbl_word_pad = self._io.read_s4be()
            self.reserved_a = self._io.read_bytes(8)
            self.reserved_v = self._io.read_bytes(24)


    class ExitStatus(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.termination_code = self._io.read_s2be()
            self.exit_code = self._io.read_s2be()



