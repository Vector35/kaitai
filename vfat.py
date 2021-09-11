# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Vfat(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.boot_sector = Vfat.BootSector(self._io, self, self._root)

    class ExtBiosParamBlockFat32(KaitaiStruct):
        """Extended BIOS Parameter Block for FAT32."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ls_per_fat = self._io.read_u4le()
            self.has_active_fat = self._io.read_bits_int_be(1) != 0
            self.reserved1 = self._io.read_bits_int_be(3)
            self.active_fat_id = self._io.read_bits_int_be(4)
            self._io.align_to_byte()
            self.reserved2 = self._io.read_bytes(1)
            if not self.reserved2 == b"\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00", self.reserved2, self._io, u"/types/ext_bios_param_block_fat32/seq/4")
            self.fat_version = self._io.read_u2le()
            self.root_dir_start_clus = self._io.read_u4le()
            self.ls_fs_info = self._io.read_u2le()
            self.boot_sectors_copy_start_ls = self._io.read_u2le()
            self.reserved3 = self._io.read_bytes(12)
            self.phys_drive_num = self._io.read_u1()
            self.reserved4 = self._io.read_u1()
            self.ext_boot_sign = self._io.read_u1()
            self.volume_id = self._io.read_bytes(4)
            self.partition_volume_label = (KaitaiStream.bytes_strip_right(self._io.read_bytes(11), 32)).decode(u"ASCII")
            self.fs_type_str = (KaitaiStream.bytes_strip_right(self._io.read_bytes(8), 32)).decode(u"ASCII")


    class BootSector(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.jmp_instruction = self._io.read_bytes(3)
            self.oem_name = (KaitaiStream.bytes_strip_right(self._io.read_bytes(8), 32)).decode(u"ASCII")
            self.bpb = Vfat.BiosParamBlock(self._io, self, self._root)
            if not (self.is_fat32):
                self.ebpb_fat16 = Vfat.ExtBiosParamBlockFat16(self._io, self, self._root)

            if self.is_fat32:
                self.ebpb_fat32 = Vfat.ExtBiosParamBlockFat32(self._io, self, self._root)


        @property
        def pos_fats(self):
            """Offset of FATs in bytes from start of filesystem."""
            if hasattr(self, '_m_pos_fats'):
                return self._m_pos_fats if hasattr(self, '_m_pos_fats') else None

            self._m_pos_fats = (self.bpb.bytes_per_ls * self.bpb.num_reserved_ls)
            return self._m_pos_fats if hasattr(self, '_m_pos_fats') else None

        @property
        def ls_per_fat(self):
            if hasattr(self, '_m_ls_per_fat'):
                return self._m_ls_per_fat if hasattr(self, '_m_ls_per_fat') else None

            self._m_ls_per_fat = (self.ebpb_fat32.ls_per_fat if self.is_fat32 else self.bpb.ls_per_fat)
            return self._m_ls_per_fat if hasattr(self, '_m_ls_per_fat') else None

        @property
        def ls_per_root_dir(self):
            """Size of root directory in logical sectors.
            
            .. seealso::
               FAT: General Overview of On-Disk Format, section "FAT Data Structure"
            """
            if hasattr(self, '_m_ls_per_root_dir'):
                return self._m_ls_per_root_dir if hasattr(self, '_m_ls_per_root_dir') else None

            self._m_ls_per_root_dir = (((self.bpb.max_root_dir_rec * 32) + self.bpb.bytes_per_ls) - 1) // self.bpb.bytes_per_ls
            return self._m_ls_per_root_dir if hasattr(self, '_m_ls_per_root_dir') else None

        @property
        def is_fat32(self):
            """Determines if filesystem is FAT32 (true) or FAT12/16 (false)
            by analyzing some preliminary conditions in BPB. Used to
            determine whether we should parse post-BPB data as
            `ext_bios_param_block_fat16` or `ext_bios_param_block_fat32`.
            """
            if hasattr(self, '_m_is_fat32'):
                return self._m_is_fat32 if hasattr(self, '_m_is_fat32') else None

            self._m_is_fat32 = self.bpb.max_root_dir_rec == 0
            return self._m_is_fat32 if hasattr(self, '_m_is_fat32') else None

        @property
        def size_fat(self):
            """Size of one FAT in bytes."""
            if hasattr(self, '_m_size_fat'):
                return self._m_size_fat if hasattr(self, '_m_size_fat') else None

            self._m_size_fat = (self.bpb.bytes_per_ls * self.ls_per_fat)
            return self._m_size_fat if hasattr(self, '_m_size_fat') else None

        @property
        def pos_root_dir(self):
            """Offset of root directory in bytes from start of filesystem."""
            if hasattr(self, '_m_pos_root_dir'):
                return self._m_pos_root_dir if hasattr(self, '_m_pos_root_dir') else None

            self._m_pos_root_dir = (self.bpb.bytes_per_ls * (self.bpb.num_reserved_ls + (self.ls_per_fat * self.bpb.num_fats)))
            return self._m_pos_root_dir if hasattr(self, '_m_pos_root_dir') else None

        @property
        def size_root_dir(self):
            """Size of root directory in bytes."""
            if hasattr(self, '_m_size_root_dir'):
                return self._m_size_root_dir if hasattr(self, '_m_size_root_dir') else None

            self._m_size_root_dir = (self.ls_per_root_dir * self.bpb.bytes_per_ls)
            return self._m_size_root_dir if hasattr(self, '_m_size_root_dir') else None


    class BiosParamBlock(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.bytes_per_ls = self._io.read_u2le()
            self.ls_per_clus = self._io.read_u1()
            self.num_reserved_ls = self._io.read_u2le()
            self.num_fats = self._io.read_u1()
            self.max_root_dir_rec = self._io.read_u2le()
            self.total_ls_2 = self._io.read_u2le()
            self.media_code = self._io.read_u1()
            self.ls_per_fat = self._io.read_u2le()
            self.ps_per_track = self._io.read_u2le()
            self.num_heads = self._io.read_u2le()
            self.num_hidden_sectors = self._io.read_u4le()
            self.total_ls_4 = self._io.read_u4le()


    class RootDirectoryRec(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.file_name = self._io.read_bytes(11)
            self.attribute = self._io.read_u1()
            self.reserved = self._io.read_bytes(10)
            self.time = self._io.read_u2le()
            self.date = self._io.read_u2le()
            self.start_clus = self._io.read_u2le()
            self.file_size = self._io.read_u4le()


    class RootDirectory(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.records = [None] * (self._root.boot_sector.bpb.max_root_dir_rec)
            for i in range(self._root.boot_sector.bpb.max_root_dir_rec):
                self.records[i] = Vfat.RootDirectoryRec(self._io, self, self._root)



    class ExtBiosParamBlockFat16(KaitaiStruct):
        """Extended BIOS Parameter Block (DOS 4.0+, OS/2 1.0+). Used only
        for FAT12 and FAT16.
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.phys_drive_num = self._io.read_u1()
            self.reserved1 = self._io.read_u1()
            self.ext_boot_sign = self._io.read_u1()
            self.volume_id = self._io.read_bytes(4)
            self.partition_volume_label = (KaitaiStream.bytes_strip_right(self._io.read_bytes(11), 32)).decode(u"ASCII")
            self.fs_type_str = (KaitaiStream.bytes_strip_right(self._io.read_bytes(8), 32)).decode(u"ASCII")


    @property
    def fats(self):
        if hasattr(self, '_m_fats'):
            return self._m_fats if hasattr(self, '_m_fats') else None

        _pos = self._io.pos()
        self._io.seek(self.boot_sector.pos_fats)
        self._m_fats = [None] * (self.boot_sector.bpb.num_fats)
        for i in range(self.boot_sector.bpb.num_fats):
            self._m_fats[i] = self._io.read_bytes(self.boot_sector.size_fat)

        self._io.seek(_pos)
        return self._m_fats if hasattr(self, '_m_fats') else None

    @property
    def root_dir(self):
        if hasattr(self, '_m_root_dir'):
            return self._m_root_dir if hasattr(self, '_m_root_dir') else None

        _pos = self._io.pos()
        self._io.seek(self.boot_sector.pos_root_dir)
        self._raw__m_root_dir = self._io.read_bytes(self.boot_sector.size_root_dir)
        _io__raw__m_root_dir = KaitaiStream(BytesIO(self._raw__m_root_dir))
        self._m_root_dir = Vfat.RootDirectory(_io__raw__m_root_dir, self, self._root)
        self._io.seek(_pos)
        return self._m_root_dir if hasattr(self, '_m_root_dir') else None


