# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class GptPartitionTable(KaitaiStruct):
    """
    .. seealso::
       Specification taken from https://en.wikipedia.org/wiki/GUID_Partition_Table
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        pass

    class PartitionEntry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.type_guid = self._io.read_bytes(16)
            self.guid = self._io.read_bytes(16)
            self.first_lba = self._io.read_u8le()
            self.last_lba = self._io.read_u8le()
            self.attributes = self._io.read_u8le()
            self.name = (self._io.read_bytes(72)).decode(u"UTF-16LE")


    class PartitionHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.signature = self._io.read_bytes(8)
            if not self.signature == b"\x45\x46\x49\x20\x50\x41\x52\x54":
                raise kaitaistruct.ValidationNotEqualError(b"\x45\x46\x49\x20\x50\x41\x52\x54", self.signature, self._io, u"/types/partition_header/seq/0")
            self.revision = self._io.read_u4le()
            self.header_size = self._io.read_u4le()
            self.crc32_header = self._io.read_u4le()
            self.reserved = self._io.read_u4le()
            self.current_lba = self._io.read_u8le()
            self.backup_lba = self._io.read_u8le()
            self.first_usable_lba = self._io.read_u8le()
            self.last_usable_lba = self._io.read_u8le()
            self.disk_guid = self._io.read_bytes(16)
            self.entries_start = self._io.read_u8le()
            self.entries_count = self._io.read_u4le()
            self.entries_size = self._io.read_u4le()
            self.crc32_array = self._io.read_u4le()

        @property
        def entries(self):
            if hasattr(self, '_m_entries'):
                return self._m_entries if hasattr(self, '_m_entries') else None

            io = self._root._io
            _pos = io.pos()
            io.seek((self.entries_start * self._root.sector_size))
            self._raw__m_entries = [None] * (self.entries_count)
            self._m_entries = [None] * (self.entries_count)
            for i in range(self.entries_count):
                self._raw__m_entries[i] = io.read_bytes(self.entries_size)
                _io__raw__m_entries = KaitaiStream(BytesIO(self._raw__m_entries[i]))
                self._m_entries[i] = GptPartitionTable.PartitionEntry(_io__raw__m_entries, self, self._root)

            io.seek(_pos)
            return self._m_entries if hasattr(self, '_m_entries') else None


    @property
    def sector_size(self):
        if hasattr(self, '_m_sector_size'):
            return self._m_sector_size if hasattr(self, '_m_sector_size') else None

        self._m_sector_size = 512
        return self._m_sector_size if hasattr(self, '_m_sector_size') else None

    @property
    def primary(self):
        if hasattr(self, '_m_primary'):
            return self._m_primary if hasattr(self, '_m_primary') else None

        io = self._root._io
        _pos = io.pos()
        io.seek(self._root.sector_size)
        self._m_primary = GptPartitionTable.PartitionHeader(io, self, self._root)
        io.seek(_pos)
        return self._m_primary if hasattr(self, '_m_primary') else None

    @property
    def backup(self):
        if hasattr(self, '_m_backup'):
            return self._m_backup if hasattr(self, '_m_backup') else None

        io = self._root._io
        _pos = io.pos()
        io.seek((self._io.size() - self._root.sector_size))
        self._m_backup = GptPartitionTable.PartitionHeader(io, self, self._root)
        io.seek(_pos)
        return self._m_backup if hasattr(self, '_m_backup') else None


