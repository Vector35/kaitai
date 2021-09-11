# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class ApmPartitionTable(KaitaiStruct):
    """
    .. seealso::
       Specification taken from https://en.wikipedia.org/wiki/Apple_Partition_Map
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
            self.magic = self._io.read_bytes(2)
            if not self.magic == b"\x50\x4D":
                raise kaitaistruct.ValidationNotEqualError(b"\x50\x4D", self.magic, self._io, u"/types/partition_entry/seq/0")
            self.reserved_1 = self._io.read_bytes(2)
            self.number_of_partitions = self._io.read_u4be()
            self.partition_start = self._io.read_u4be()
            self.partition_size = self._io.read_u4be()
            self.partition_name = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.partition_type = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.data_start = self._io.read_u4be()
            self.data_size = self._io.read_u4be()
            self.partition_status = self._io.read_u4be()
            self.boot_code_start = self._io.read_u4be()
            self.boot_code_size = self._io.read_u4be()
            self.boot_loader_address = self._io.read_u4be()
            self.reserved_2 = self._io.read_bytes(4)
            self.boot_code_entry = self._io.read_u4be()
            self.reserved_3 = self._io.read_bytes(4)
            self.boot_code_cksum = self._io.read_u4be()
            self.processor_type = (KaitaiStream.bytes_terminate(self._io.read_bytes(16), 0, False)).decode(u"ascii")

        @property
        def partition(self):
            if hasattr(self, '_m_partition'):
                return self._m_partition if hasattr(self, '_m_partition') else None

            if (self.partition_status & 1) != 0:
                io = self._root._io
                _pos = io.pos()
                io.seek((self.partition_start * self._root.sector_size))
                self._m_partition = io.read_bytes((self.partition_size * self._root.sector_size))
                io.seek(_pos)

            return self._m_partition if hasattr(self, '_m_partition') else None

        @property
        def data(self):
            if hasattr(self, '_m_data'):
                return self._m_data if hasattr(self, '_m_data') else None

            io = self._root._io
            _pos = io.pos()
            io.seek((self.data_start * self._root.sector_size))
            self._m_data = io.read_bytes((self.data_size * self._root.sector_size))
            io.seek(_pos)
            return self._m_data if hasattr(self, '_m_data') else None

        @property
        def boot_code(self):
            if hasattr(self, '_m_boot_code'):
                return self._m_boot_code if hasattr(self, '_m_boot_code') else None

            io = self._root._io
            _pos = io.pos()
            io.seek((self.boot_code_start * self._root.sector_size))
            self._m_boot_code = io.read_bytes(self.boot_code_size)
            io.seek(_pos)
            return self._m_boot_code if hasattr(self, '_m_boot_code') else None


    @property
    def sector_size(self):
        """0x200 (512) bytes for disks, 0x1000 (4096) bytes is not supported by APM
        0x800 (2048) bytes for CDROM
        """
        if hasattr(self, '_m_sector_size'):
            return self._m_sector_size if hasattr(self, '_m_sector_size') else None

        self._m_sector_size = 512
        return self._m_sector_size if hasattr(self, '_m_sector_size') else None

    @property
    def partition_lookup(self):
        """Every partition entry contains the number of partition entries.
        We parse the first entry, to know how many to parse, including the first one.
        No logic is given what to do if other entries have a different number.
        """
        if hasattr(self, '_m_partition_lookup'):
            return self._m_partition_lookup if hasattr(self, '_m_partition_lookup') else None

        io = self._root._io
        _pos = io.pos()
        io.seek(self._root.sector_size)
        self._raw__m_partition_lookup = io.read_bytes(self.sector_size)
        _io__raw__m_partition_lookup = KaitaiStream(BytesIO(self._raw__m_partition_lookup))
        self._m_partition_lookup = ApmPartitionTable.PartitionEntry(_io__raw__m_partition_lookup, self, self._root)
        io.seek(_pos)
        return self._m_partition_lookup if hasattr(self, '_m_partition_lookup') else None

    @property
    def partition_entries(self):
        if hasattr(self, '_m_partition_entries'):
            return self._m_partition_entries if hasattr(self, '_m_partition_entries') else None

        io = self._root._io
        _pos = io.pos()
        io.seek(self._root.sector_size)
        self._raw__m_partition_entries = [None] * (self._root.partition_lookup.number_of_partitions)
        self._m_partition_entries = [None] * (self._root.partition_lookup.number_of_partitions)
        for i in range(self._root.partition_lookup.number_of_partitions):
            self._raw__m_partition_entries[i] = io.read_bytes(self.sector_size)
            _io__raw__m_partition_entries = KaitaiStream(BytesIO(self._raw__m_partition_entries[i]))
            self._m_partition_entries[i] = ApmPartitionTable.PartitionEntry(_io__raw__m_partition_entries, self, self._root)

        io.seek(_pos)
        return self._m_partition_entries if hasattr(self, '_m_partition_entries') else None


