# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class MbrPartitionTable(KaitaiStruct):
    """MBR (Master Boot Record) partition table is a traditional way of
    MS-DOS to partition larger hard disc drives into distinct
    partitions.
    
    This table is stored in the end of the boot sector (first sector) of
    the drive, after the bootstrap code. Original DOS 2.0 specification
    allowed only 4 partitions per disc, but DOS 3.2 introduced concept
    of "extended partitions", which work as nested extra "boot records"
    which are pointed to by original ("primary") partitions in MBR.
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.bootstrap_code = self._io.read_bytes(446)
        self.partitions = [None] * (4)
        for i in range(4):
            self.partitions[i] = MbrPartitionTable.PartitionEntry(self._io, self, self._root)

        self.boot_signature = self._io.read_bytes(2)
        if not self.boot_signature == b"\x55\xAA":
            raise kaitaistruct.ValidationNotEqualError(b"\x55\xAA", self.boot_signature, self._io, u"/seq/2")

    class PartitionEntry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.chs_start = MbrPartitionTable.Chs(self._io, self, self._root)
            self.partition_type = self._io.read_u1()
            self.chs_end = MbrPartitionTable.Chs(self._io, self, self._root)
            self.lba_start = self._io.read_u4le()
            self.num_sectors = self._io.read_u4le()


    class Chs(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.head = self._io.read_u1()
            self.b2 = self._io.read_u1()
            self.b3 = self._io.read_u1()

        @property
        def sector(self):
            if hasattr(self, '_m_sector'):
                return self._m_sector if hasattr(self, '_m_sector') else None

            self._m_sector = (self.b2 & 63)
            return self._m_sector if hasattr(self, '_m_sector') else None

        @property
        def cylinder(self):
            if hasattr(self, '_m_cylinder'):
                return self._m_cylinder if hasattr(self, '_m_cylinder') else None

            self._m_cylinder = (self.b3 + ((self.b2 & 192) << 2))
            return self._m_cylinder if hasattr(self, '_m_cylinder') else None



