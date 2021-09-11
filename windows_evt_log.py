# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class WindowsEvtLog(KaitaiStruct):
    """EVT files are Windows Event Log files written by older Windows
    operating systems (2000, XP, 2003). They are used as binary log
    files by several major Windows subsystems and
    applications. Typically, several of them can be found in
    `%WINDIR%\system32\config` directory:
    
    * Application = `AppEvent.evt`
    * System = `SysEvent.evt`
    * Security = `SecEvent.evt`
    
    Alternatively, one can export any system event log as distinct .evt
    file using relevant option in Event Viewer application.
    
    A Windows application can submit an entry into these logs using
    [ReportEvent](https://msdn.microsoft.com/en-us/library/aa363679(v=vs.85).aspx)
    function of Windows API.
    
    Internally, EVT files consist of a fixed-size header and event
    records. There are several usage scenarios (non-wrapping vs wrapping
    log files) which result in slightly different organization of
    records.
    
    .. seealso::
       Source - https://msdn.microsoft.com/en-us/library/bb309026(v=vs.85).aspx
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.header = WindowsEvtLog.Header(self._io, self, self._root)
        self.records = []
        i = 0
        while not self._io.is_eof():
            self.records.append(WindowsEvtLog.Record(self._io, self, self._root))
            i += 1


    class Header(KaitaiStruct):
        """
        .. seealso::
           Source - https://msdn.microsoft.com/en-us/library/bb309024(v=vs.85).aspx
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len_header = self._io.read_u4le()
            self.magic = self._io.read_bytes(4)
            if not self.magic == b"\x4C\x66\x4C\x65":
                raise kaitaistruct.ValidationNotEqualError(b"\x4C\x66\x4C\x65", self.magic, self._io, u"/types/header/seq/1")
            self.version_major = self._io.read_u4le()
            self.version_minor = self._io.read_u4le()
            self.ofs_start = self._io.read_u4le()
            self.ofs_end = self._io.read_u4le()
            self.cur_rec_idx = self._io.read_u4le()
            self.oldest_rec_idx = self._io.read_u4le()
            self.len_file_max = self._io.read_u4le()
            self.flags = WindowsEvtLog.Header.Flags(self._io, self, self._root)
            self.retention = self._io.read_u4le()
            self.len_header_2 = self._io.read_u4le()

        class Flags(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.reserved = self._io.read_bits_int_be(28)
                self.archive = self._io.read_bits_int_be(1) != 0
                self.log_full = self._io.read_bits_int_be(1) != 0
                self.wrap = self._io.read_bits_int_be(1) != 0
                self.dirty = self._io.read_bits_int_be(1) != 0



    class Record(KaitaiStruct):
        """
        .. seealso::
           Source - https://msdn.microsoft.com/en-us/library/windows/desktop/aa363646(v=vs.85).aspx
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len_record = self._io.read_u4le()
            self.type = self._io.read_u4le()
            _on = self.type
            if _on == 1699505740:
                self._raw_body = self._io.read_bytes((self.len_record - 12))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = WindowsEvtLog.RecordBody(_io__raw_body, self, self._root)
            elif _on == 286331153:
                self._raw_body = self._io.read_bytes((self.len_record - 12))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = WindowsEvtLog.CursorRecordBody(_io__raw_body, self, self._root)
            else:
                self.body = self._io.read_bytes((self.len_record - 12))
            self.len_record2 = self._io.read_u4le()


    class RecordBody(KaitaiStruct):
        """
        .. seealso::
           Source - https://msdn.microsoft.com/en-us/library/windows/desktop/aa363646(v=vs.85).aspx
        """

        class EventTypes(Enum):
            error = 1
            audit_failure = 2
            audit_success = 3
            info = 4
            warning = 5
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.idx = self._io.read_u4le()
            self.time_generated = self._io.read_u4le()
            self.time_written = self._io.read_u4le()
            self.event_id = self._io.read_u4le()
            self.event_type = KaitaiStream.resolve_enum(WindowsEvtLog.RecordBody.EventTypes, self._io.read_u2le())
            self.num_strings = self._io.read_u2le()
            self.event_category = self._io.read_u2le()
            self.reserved = self._io.read_bytes(6)
            self.ofs_strings = self._io.read_u4le()
            self.len_user_sid = self._io.read_u4le()
            self.ofs_user_sid = self._io.read_u4le()
            self.len_data = self._io.read_u4le()
            self.ofs_data = self._io.read_u4le()

        @property
        def user_sid(self):
            if hasattr(self, '_m_user_sid'):
                return self._m_user_sid if hasattr(self, '_m_user_sid') else None

            _pos = self._io.pos()
            self._io.seek((self.ofs_user_sid - 8))
            self._m_user_sid = self._io.read_bytes(self.len_user_sid)
            self._io.seek(_pos)
            return self._m_user_sid if hasattr(self, '_m_user_sid') else None

        @property
        def data(self):
            if hasattr(self, '_m_data'):
                return self._m_data if hasattr(self, '_m_data') else None

            _pos = self._io.pos()
            self._io.seek((self.ofs_data - 8))
            self._m_data = self._io.read_bytes(self.len_data)
            self._io.seek(_pos)
            return self._m_data if hasattr(self, '_m_data') else None


    class CursorRecordBody(KaitaiStruct):
        """
        .. seealso::
           Source - http://www.forensicswiki.xyz/page/Windows_Event_Log_(EVT)#Cursor_Record
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(12)
            if not self.magic == b"\x22\x22\x22\x22\x33\x33\x33\x33\x44\x44\x44\x44":
                raise kaitaistruct.ValidationNotEqualError(b"\x22\x22\x22\x22\x33\x33\x33\x33\x44\x44\x44\x44", self.magic, self._io, u"/types/cursor_record_body/seq/0")
            self.ofs_first_record = self._io.read_u4le()
            self.ofs_next_record = self._io.read_u4le()
            self.idx_next_record = self._io.read_u4le()
            self.idx_first_record = self._io.read_u4le()



