# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Ext2(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        pass

    class SuperBlockStruct(KaitaiStruct):

        class StateEnum(Enum):
            valid_fs = 1
            error_fs = 2

        class ErrorsEnum(Enum):
            act_continue = 1
            act_ro = 2
            act_panic = 3
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.inodes_count = self._io.read_u4le()
            self.blocks_count = self._io.read_u4le()
            self.r_blocks_count = self._io.read_u4le()
            self.free_blocks_count = self._io.read_u4le()
            self.free_inodes_count = self._io.read_u4le()
            self.first_data_block = self._io.read_u4le()
            self.log_block_size = self._io.read_u4le()
            self.log_frag_size = self._io.read_u4le()
            self.blocks_per_group = self._io.read_u4le()
            self.frags_per_group = self._io.read_u4le()
            self.inodes_per_group = self._io.read_u4le()
            self.mtime = self._io.read_u4le()
            self.wtime = self._io.read_u4le()
            self.mnt_count = self._io.read_u2le()
            self.max_mnt_count = self._io.read_u2le()
            self.magic = self._io.read_bytes(2)
            if not self.magic == b"\x53\xEF":
                raise kaitaistruct.ValidationNotEqualError(b"\x53\xEF", self.magic, self._io, u"/types/super_block_struct/seq/15")
            self.state = KaitaiStream.resolve_enum(Ext2.SuperBlockStruct.StateEnum, self._io.read_u2le())
            self.errors = KaitaiStream.resolve_enum(Ext2.SuperBlockStruct.ErrorsEnum, self._io.read_u2le())
            self.minor_rev_level = self._io.read_u2le()
            self.lastcheck = self._io.read_u4le()
            self.checkinterval = self._io.read_u4le()
            self.creator_os = self._io.read_u4le()
            self.rev_level = self._io.read_u4le()
            self.def_resuid = self._io.read_u2le()
            self.def_resgid = self._io.read_u2le()
            self.first_ino = self._io.read_u4le()
            self.inode_size = self._io.read_u2le()
            self.block_group_nr = self._io.read_u2le()
            self.feature_compat = self._io.read_u4le()
            self.feature_incompat = self._io.read_u4le()
            self.feature_ro_compat = self._io.read_u4le()
            self.uuid = self._io.read_bytes(16)
            self.volume_name = self._io.read_bytes(16)
            self.last_mounted = self._io.read_bytes(64)
            self.algo_bitmap = self._io.read_u4le()
            self.prealloc_blocks = self._io.read_u1()
            self.prealloc_dir_blocks = self._io.read_u1()
            self.padding1 = self._io.read_bytes(2)
            self.journal_uuid = self._io.read_bytes(16)
            self.journal_inum = self._io.read_u4le()
            self.journal_dev = self._io.read_u4le()
            self.last_orphan = self._io.read_u4le()
            self.hash_seed = [None] * (4)
            for i in range(4):
                self.hash_seed[i] = self._io.read_u4le()

            self.def_hash_version = self._io.read_u1()

        @property
        def block_size(self):
            if hasattr(self, '_m_block_size'):
                return self._m_block_size if hasattr(self, '_m_block_size') else None

            self._m_block_size = (1024 << self.log_block_size)
            return self._m_block_size if hasattr(self, '_m_block_size') else None

        @property
        def block_group_count(self):
            if hasattr(self, '_m_block_group_count'):
                return self._m_block_group_count if hasattr(self, '_m_block_group_count') else None

            self._m_block_group_count = self.blocks_count // self.blocks_per_group
            return self._m_block_group_count if hasattr(self, '_m_block_group_count') else None


    class DirEntry(KaitaiStruct):

        class FileTypeEnum(Enum):
            unknown = 0
            reg_file = 1
            dir = 2
            chrdev = 3
            blkdev = 4
            fifo = 5
            sock = 6
            symlink = 7
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.inode_ptr = self._io.read_u4le()
            self.rec_len = self._io.read_u2le()
            self.name_len = self._io.read_u1()
            self.file_type = KaitaiStream.resolve_enum(Ext2.DirEntry.FileTypeEnum, self._io.read_u1())
            self.name = (self._io.read_bytes(self.name_len)).decode(u"UTF-8")
            self.padding = self._io.read_bytes(((self.rec_len - self.name_len) - 8))

        @property
        def inode(self):
            if hasattr(self, '_m_inode'):
                return self._m_inode if hasattr(self, '_m_inode') else None

            self._m_inode = self._root.bg1.block_groups[(self.inode_ptr - 1) // self._root.bg1.super_block.inodes_per_group].inodes[((self.inode_ptr - 1) % self._root.bg1.super_block.inodes_per_group)]
            return self._m_inode if hasattr(self, '_m_inode') else None


    class Inode(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.mode = self._io.read_u2le()
            self.uid = self._io.read_u2le()
            self.size = self._io.read_u4le()
            self.atime = self._io.read_u4le()
            self.ctime = self._io.read_u4le()
            self.mtime = self._io.read_u4le()
            self.dtime = self._io.read_u4le()
            self.gid = self._io.read_u2le()
            self.links_count = self._io.read_u2le()
            self.blocks = self._io.read_u4le()
            self.flags = self._io.read_u4le()
            self.osd1 = self._io.read_u4le()
            self.block = [None] * (15)
            for i in range(15):
                self.block[i] = Ext2.BlockPtr(self._io, self, self._root)

            self.generation = self._io.read_u4le()
            self.file_acl = self._io.read_u4le()
            self.dir_acl = self._io.read_u4le()
            self.faddr = self._io.read_u4le()
            self.osd2 = self._io.read_bytes(12)

        @property
        def as_dir(self):
            if hasattr(self, '_m_as_dir'):
                return self._m_as_dir if hasattr(self, '_m_as_dir') else None

            io = self.block[0].body._io
            _pos = io.pos()
            io.seek(0)
            self._m_as_dir = Ext2.Dir(io, self, self._root)
            io.seek(_pos)
            return self._m_as_dir if hasattr(self, '_m_as_dir') else None


    class BlockPtr(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ptr = self._io.read_u4le()

        @property
        def body(self):
            if hasattr(self, '_m_body'):
                return self._m_body if hasattr(self, '_m_body') else None

            _pos = self._io.pos()
            self._io.seek((self.ptr * self._root.bg1.super_block.block_size))
            self._raw__m_body = self._io.read_bytes(self._root.bg1.super_block.block_size)
            _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
            self._m_body = Ext2.RawBlock(_io__raw__m_body, self, self._root)
            self._io.seek(_pos)
            return self._m_body if hasattr(self, '_m_body') else None


    class Dir(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self.entries.append(Ext2.DirEntry(self._io, self, self._root))
                i += 1



    class BlockGroup(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw_super_block = self._io.read_bytes(1024)
            _io__raw_super_block = KaitaiStream(BytesIO(self._raw_super_block))
            self.super_block = Ext2.SuperBlockStruct(_io__raw_super_block, self, self._root)
            self.block_groups = [None] * (self.super_block.block_group_count)
            for i in range(self.super_block.block_group_count):
                self.block_groups[i] = Ext2.Bgd(self._io, self, self._root)



    class Bgd(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.block_bitmap_block = self._io.read_u4le()
            self.inode_bitmap_block = self._io.read_u4le()
            self.inode_table_block = self._io.read_u4le()
            self.free_blocks_count = self._io.read_u2le()
            self.free_inodes_count = self._io.read_u2le()
            self.used_dirs_count = self._io.read_u2le()
            self.pad_reserved = self._io.read_bytes((2 + 12))

        @property
        def block_bitmap(self):
            if hasattr(self, '_m_block_bitmap'):
                return self._m_block_bitmap if hasattr(self, '_m_block_bitmap') else None

            _pos = self._io.pos()
            self._io.seek((self.block_bitmap_block * self._root.bg1.super_block.block_size))
            self._m_block_bitmap = self._io.read_bytes(1024)
            self._io.seek(_pos)
            return self._m_block_bitmap if hasattr(self, '_m_block_bitmap') else None

        @property
        def inode_bitmap(self):
            if hasattr(self, '_m_inode_bitmap'):
                return self._m_inode_bitmap if hasattr(self, '_m_inode_bitmap') else None

            _pos = self._io.pos()
            self._io.seek((self.inode_bitmap_block * self._root.bg1.super_block.block_size))
            self._m_inode_bitmap = self._io.read_bytes(1024)
            self._io.seek(_pos)
            return self._m_inode_bitmap if hasattr(self, '_m_inode_bitmap') else None

        @property
        def inodes(self):
            if hasattr(self, '_m_inodes'):
                return self._m_inodes if hasattr(self, '_m_inodes') else None

            _pos = self._io.pos()
            self._io.seek((self.inode_table_block * self._root.bg1.super_block.block_size))
            self._m_inodes = [None] * (self._root.bg1.super_block.inodes_per_group)
            for i in range(self._root.bg1.super_block.inodes_per_group):
                self._m_inodes[i] = Ext2.Inode(self._io, self, self._root)

            self._io.seek(_pos)
            return self._m_inodes if hasattr(self, '_m_inodes') else None


    class RawBlock(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.body = self._io.read_bytes(self._root.bg1.super_block.block_size)


    @property
    def bg1(self):
        if hasattr(self, '_m_bg1'):
            return self._m_bg1 if hasattr(self, '_m_bg1') else None

        _pos = self._io.pos()
        self._io.seek(1024)
        self._m_bg1 = Ext2.BlockGroup(self._io, self, self._root)
        self._io.seek(_pos)
        return self._m_bg1 if hasattr(self, '_m_bg1') else None

    @property
    def root_dir(self):
        if hasattr(self, '_m_root_dir'):
            return self._m_root_dir if hasattr(self, '_m_root_dir') else None

        self._m_root_dir = self.bg1.block_groups[0].inodes[1].as_dir
        return self._m_root_dir if hasattr(self, '_m_root_dir') else None


