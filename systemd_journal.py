# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class SystemdJournal(KaitaiStruct):
    """systemd, a popular user-space system/service management suite on Linux,
    offers logging functionality, storing incoming logs in a binary journal
    format.
    
    On live Linux system running systemd, these journals are typically located at:
    
    * /run/log/journal/machine-id/*.journal (volatile, lost after reboot)
    * /var/log/journal/machine-id/*.journal (persistent, but disabled by default on Debian / Ubuntu)
    
    .. seealso::
       Source - https://www.freedesktop.org/wiki/Software/systemd/journal-files/
    """

    class State(Enum):
        offline = 0
        online = 1
        archived = 2
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self._raw_header = self._io.read_bytes(self.len_header)
        _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
        self.header = SystemdJournal.Header(_io__raw_header, self, self._root)
        self.objects = [None] * (self.header.num_objects)
        for i in range(self.header.num_objects):
            self.objects[i] = SystemdJournal.JournalObject(self._io, self, self._root)


    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.signature = self._io.read_bytes(8)
            if not self.signature == b"\x4C\x50\x4B\x53\x48\x48\x52\x48":
                raise kaitaistruct.ValidationNotEqualError(b"\x4C\x50\x4B\x53\x48\x48\x52\x48", self.signature, self._io, u"/types/header/seq/0")
            self.compatible_flags = self._io.read_u4le()
            self.incompatible_flags = self._io.read_u4le()
            self.state = KaitaiStream.resolve_enum(SystemdJournal.State, self._io.read_u1())
            self.reserved = self._io.read_bytes(7)
            self.file_id = self._io.read_bytes(16)
            self.machine_id = self._io.read_bytes(16)
            self.boot_id = self._io.read_bytes(16)
            self.seqnum_id = self._io.read_bytes(16)
            self.len_header = self._io.read_u8le()
            self.len_arena = self._io.read_u8le()
            self.ofs_data_hash_table = self._io.read_u8le()
            self.len_data_hash_table = self._io.read_u8le()
            self.ofs_field_hash_table = self._io.read_u8le()
            self.len_field_hash_table = self._io.read_u8le()
            self.ofs_tail_object = self._io.read_u8le()
            self.num_objects = self._io.read_u8le()
            self.num_entries = self._io.read_u8le()
            self.tail_entry_seqnum = self._io.read_u8le()
            self.head_entry_seqnum = self._io.read_u8le()
            self.ofs_entry_array = self._io.read_u8le()
            self.head_entry_realtime = self._io.read_u8le()
            self.tail_entry_realtime = self._io.read_u8le()
            self.tail_entry_monotonic = self._io.read_u8le()
            if not (self._io.is_eof()):
                self.num_data = self._io.read_u8le()

            if not (self._io.is_eof()):
                self.num_fields = self._io.read_u8le()

            if not (self._io.is_eof()):
                self.num_tags = self._io.read_u8le()

            if not (self._io.is_eof()):
                self.num_entry_arrays = self._io.read_u8le()



    class JournalObject(KaitaiStruct):
        """
        .. seealso::
           Source - https://www.freedesktop.org/wiki/Software/systemd/journal-files/#objects
        """

        class ObjectTypes(Enum):
            unused = 0
            data = 1
            field = 2
            entry = 3
            data_hash_table = 4
            field_hash_table = 5
            entry_array = 6
            tag = 7
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.padding = self._io.read_bytes(((8 - self._io.pos()) % 8))
            self.object_type = KaitaiStream.resolve_enum(SystemdJournal.JournalObject.ObjectTypes, self._io.read_u1())
            self.flags = self._io.read_u1()
            self.reserved = self._io.read_bytes(6)
            self.len_object = self._io.read_u8le()
            _on = self.object_type
            if _on == SystemdJournal.JournalObject.ObjectTypes.data:
                self._raw_payload = self._io.read_bytes((self.len_object - 16))
                _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
                self.payload = SystemdJournal.DataObject(_io__raw_payload, self, self._root)
            else:
                self.payload = self._io.read_bytes((self.len_object - 16))


    class DataObject(KaitaiStruct):
        """Data objects are designed to carry log payload, typically in
        form of a "key=value" string in `payload` attribute.
        
        .. seealso::
           Source - https://www.freedesktop.org/wiki/Software/systemd/journal-files/#dataobjects
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.hash = self._io.read_u8le()
            self.ofs_next_hash = self._io.read_u8le()
            self.ofs_head_field = self._io.read_u8le()
            self.ofs_entry = self._io.read_u8le()
            self.ofs_entry_array = self._io.read_u8le()
            self.num_entries = self._io.read_u8le()
            self.payload = self._io.read_bytes_full()

        @property
        def next_hash(self):
            if hasattr(self, '_m_next_hash'):
                return self._m_next_hash if hasattr(self, '_m_next_hash') else None

            if self.ofs_next_hash != 0:
                io = self._root._io
                _pos = io.pos()
                io.seek(self.ofs_next_hash)
                self._m_next_hash = SystemdJournal.JournalObject(io, self, self._root)
                io.seek(_pos)

            return self._m_next_hash if hasattr(self, '_m_next_hash') else None

        @property
        def head_field(self):
            if hasattr(self, '_m_head_field'):
                return self._m_head_field if hasattr(self, '_m_head_field') else None

            if self.ofs_head_field != 0:
                io = self._root._io
                _pos = io.pos()
                io.seek(self.ofs_head_field)
                self._m_head_field = SystemdJournal.JournalObject(io, self, self._root)
                io.seek(_pos)

            return self._m_head_field if hasattr(self, '_m_head_field') else None

        @property
        def entry(self):
            if hasattr(self, '_m_entry'):
                return self._m_entry if hasattr(self, '_m_entry') else None

            if self.ofs_entry != 0:
                io = self._root._io
                _pos = io.pos()
                io.seek(self.ofs_entry)
                self._m_entry = SystemdJournal.JournalObject(io, self, self._root)
                io.seek(_pos)

            return self._m_entry if hasattr(self, '_m_entry') else None

        @property
        def entry_array(self):
            if hasattr(self, '_m_entry_array'):
                return self._m_entry_array if hasattr(self, '_m_entry_array') else None

            if self.ofs_entry_array != 0:
                io = self._root._io
                _pos = io.pos()
                io.seek(self.ofs_entry_array)
                self._m_entry_array = SystemdJournal.JournalObject(io, self, self._root)
                io.seek(_pos)

            return self._m_entry_array if hasattr(self, '_m_entry_array') else None


    @property
    def len_header(self):
        """Header length is used to set substream size, as it thus required
        prior to declaration of header.
        """
        if hasattr(self, '_m_len_header'):
            return self._m_len_header if hasattr(self, '_m_len_header') else None

        _pos = self._io.pos()
        self._io.seek(88)
        self._m_len_header = self._io.read_u8le()
        self._io.seek(_pos)
        return self._m_len_header if hasattr(self, '_m_len_header') else None

    @property
    def data_hash_table(self):
        if hasattr(self, '_m_data_hash_table'):
            return self._m_data_hash_table if hasattr(self, '_m_data_hash_table') else None

        _pos = self._io.pos()
        self._io.seek(self.header.ofs_data_hash_table)
        self._m_data_hash_table = self._io.read_bytes(self.header.len_data_hash_table)
        self._io.seek(_pos)
        return self._m_data_hash_table if hasattr(self, '_m_data_hash_table') else None

    @property
    def field_hash_table(self):
        if hasattr(self, '_m_field_hash_table'):
            return self._m_field_hash_table if hasattr(self, '_m_field_hash_table') else None

        _pos = self._io.pos()
        self._io.seek(self.header.ofs_field_hash_table)
        self._m_field_hash_table = self._io.read_bytes(self.header.len_field_hash_table)
        self._io.seek(_pos)
        return self._m_field_hash_table if hasattr(self, '_m_field_hash_table') else None


