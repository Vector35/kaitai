# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class GlibcUtmp(KaitaiStruct):

    class EntryType(Enum):
        empty = 0
        run_lvl = 1
        boot_time = 2
        new_time = 3
        old_time = 4
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
        self._raw_records = []
        self.records = []
        i = 0
        while not self._io.is_eof():
            self._raw_records.append(self._io.read_bytes(384))
            _io__raw_records = KaitaiStream(BytesIO(self._raw_records[-1]))
            self.records.append(GlibcUtmp.Record(_io__raw_records, self, self._root))
            i += 1


    class Record(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ut_type = KaitaiStream.resolve_enum(GlibcUtmp.EntryType, self._io.read_s4le())
            self.pid = self._io.read_u4le()
            self.line = (self._io.read_bytes(32)).decode(u"UTF-8")
            self.id = (self._io.read_bytes(4)).decode(u"UTF-8")
            self.user = (self._io.read_bytes(32)).decode(u"UTF-8")
            self.host = (self._io.read_bytes(256)).decode(u"UTF-8")
            self.exit = self._io.read_u4le()
            self.session = self._io.read_s4le()
            self.tv = GlibcUtmp.Timeval(self._io, self, self._root)
            self.addr_v6 = self._io.read_bytes(16)
            self.reserved = self._io.read_bytes(20)


    class Timeval(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.sec = self._io.read_s4le()
            self.usec = self._io.read_s4le()



