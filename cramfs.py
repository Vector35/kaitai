# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Cramfs(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.super_block = Cramfs.SuperBlockStruct(self._io, self, self._root)

    class SuperBlockStruct(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(4)
            if not self.magic == b"\x45\x3D\xCD\x28":
                raise kaitaistruct.ValidationNotEqualError(b"\x45\x3D\xCD\x28", self.magic, self._io, u"/types/super_block_struct/seq/0")
            self.size = self._io.read_u4le()
            self.flags = self._io.read_u4le()
            self.future = self._io.read_u4le()
            self.signature = self._io.read_bytes(16)
            if not self.signature == b"\x43\x6F\x6D\x70\x72\x65\x73\x73\x65\x64\x20\x52\x4F\x4D\x46\x53":
                raise kaitaistruct.ValidationNotEqualError(b"\x43\x6F\x6D\x70\x72\x65\x73\x73\x65\x64\x20\x52\x4F\x4D\x46\x53", self.signature, self._io, u"/types/super_block_struct/seq/4")
            self.fsid = Cramfs.Info(self._io, self, self._root)
            self.name = (self._io.read_bytes(16)).decode(u"ASCII")
            self.root = Cramfs.Inode(self._io, self, self._root)

        @property
        def flag_fsid_v2(self):
            if hasattr(self, '_m_flag_fsid_v2'):
                return self._m_flag_fsid_v2 if hasattr(self, '_m_flag_fsid_v2') else None

            self._m_flag_fsid_v2 = ((self.flags >> 0) & 1)
            return self._m_flag_fsid_v2 if hasattr(self, '_m_flag_fsid_v2') else None

        @property
        def flag_holes(self):
            if hasattr(self, '_m_flag_holes'):
                return self._m_flag_holes if hasattr(self, '_m_flag_holes') else None

            self._m_flag_holes = ((self.flags >> 8) & 1)
            return self._m_flag_holes if hasattr(self, '_m_flag_holes') else None

        @property
        def flag_wrong_signature(self):
            if hasattr(self, '_m_flag_wrong_signature'):
                return self._m_flag_wrong_signature if hasattr(self, '_m_flag_wrong_signature') else None

            self._m_flag_wrong_signature = ((self.flags >> 9) & 1)
            return self._m_flag_wrong_signature if hasattr(self, '_m_flag_wrong_signature') else None

        @property
        def flag_sorted_dirs(self):
            if hasattr(self, '_m_flag_sorted_dirs'):
                return self._m_flag_sorted_dirs if hasattr(self, '_m_flag_sorted_dirs') else None

            self._m_flag_sorted_dirs = ((self.flags >> 1) & 1)
            return self._m_flag_sorted_dirs if hasattr(self, '_m_flag_sorted_dirs') else None

        @property
        def flag_shifted_root_offset(self):
            if hasattr(self, '_m_flag_shifted_root_offset'):
                return self._m_flag_shifted_root_offset if hasattr(self, '_m_flag_shifted_root_offset') else None

            self._m_flag_shifted_root_offset = ((self.flags >> 10) & 1)
            return self._m_flag_shifted_root_offset if hasattr(self, '_m_flag_shifted_root_offset') else None


    class ChunkedDataInode(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.block_end_index = [None] * (((self._parent.size + self._root.page_size) - 1) // self._root.page_size)
            for i in range(((self._parent.size + self._root.page_size) - 1) // self._root.page_size):
                self.block_end_index[i] = self._io.read_u4le()

            self.raw_blocks = self._io.read_bytes_full()


    class Inode(KaitaiStruct):

        class FileType(Enum):
            fifo = 1
            chrdev = 2
            dir = 4
            blkdev = 6
            reg_file = 8
            symlink = 10
            socket = 12
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.mode = self._io.read_u2le()
            self.uid = self._io.read_u2le()
            self.size_gid = self._io.read_u4le()
            self.namelen_offset = self._io.read_u4le()
            self.name = (self._io.read_bytes(self.namelen)).decode(u"utf-8")

        @property
        def attr(self):
            if hasattr(self, '_m_attr'):
                return self._m_attr if hasattr(self, '_m_attr') else None

            self._m_attr = ((self.mode >> 9) & 7)
            return self._m_attr if hasattr(self, '_m_attr') else None

        @property
        def as_reg_file(self):
            if hasattr(self, '_m_as_reg_file'):
                return self._m_as_reg_file if hasattr(self, '_m_as_reg_file') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.offset)
            self._m_as_reg_file = Cramfs.ChunkedDataInode(io, self, self._root)
            io.seek(_pos)
            return self._m_as_reg_file if hasattr(self, '_m_as_reg_file') else None

        @property
        def perm_u(self):
            if hasattr(self, '_m_perm_u'):
                return self._m_perm_u if hasattr(self, '_m_perm_u') else None

            self._m_perm_u = ((self.mode >> 6) & 7)
            return self._m_perm_u if hasattr(self, '_m_perm_u') else None

        @property
        def as_symlink(self):
            if hasattr(self, '_m_as_symlink'):
                return self._m_as_symlink if hasattr(self, '_m_as_symlink') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.offset)
            self._m_as_symlink = Cramfs.ChunkedDataInode(io, self, self._root)
            io.seek(_pos)
            return self._m_as_symlink if hasattr(self, '_m_as_symlink') else None

        @property
        def perm_o(self):
            if hasattr(self, '_m_perm_o'):
                return self._m_perm_o if hasattr(self, '_m_perm_o') else None

            self._m_perm_o = (self.mode & 7)
            return self._m_perm_o if hasattr(self, '_m_perm_o') else None

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size if hasattr(self, '_m_size') else None

            self._m_size = (self.size_gid & 16777215)
            return self._m_size if hasattr(self, '_m_size') else None

        @property
        def gid(self):
            if hasattr(self, '_m_gid'):
                return self._m_gid if hasattr(self, '_m_gid') else None

            self._m_gid = (self.size_gid >> 24)
            return self._m_gid if hasattr(self, '_m_gid') else None

        @property
        def perm_g(self):
            if hasattr(self, '_m_perm_g'):
                return self._m_perm_g if hasattr(self, '_m_perm_g') else None

            self._m_perm_g = ((self.mode >> 3) & 7)
            return self._m_perm_g if hasattr(self, '_m_perm_g') else None

        @property
        def namelen(self):
            if hasattr(self, '_m_namelen'):
                return self._m_namelen if hasattr(self, '_m_namelen') else None

            self._m_namelen = ((self.namelen_offset & 63) << 2)
            return self._m_namelen if hasattr(self, '_m_namelen') else None

        @property
        def as_dir(self):
            if hasattr(self, '_m_as_dir'):
                return self._m_as_dir if hasattr(self, '_m_as_dir') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.offset)
            self._raw__m_as_dir = io.read_bytes(self.size)
            _io__raw__m_as_dir = KaitaiStream(BytesIO(self._raw__m_as_dir))
            self._m_as_dir = Cramfs.DirInode(_io__raw__m_as_dir, self, self._root)
            io.seek(_pos)
            return self._m_as_dir if hasattr(self, '_m_as_dir') else None

        @property
        def type(self):
            if hasattr(self, '_m_type'):
                return self._m_type if hasattr(self, '_m_type') else None

            self._m_type = KaitaiStream.resolve_enum(Cramfs.Inode.FileType, ((self.mode >> 12) & 15))
            return self._m_type if hasattr(self, '_m_type') else None

        @property
        def offset(self):
            if hasattr(self, '_m_offset'):
                return self._m_offset if hasattr(self, '_m_offset') else None

            self._m_offset = (((self.namelen_offset >> 6) & 67108863) << 2)
            return self._m_offset if hasattr(self, '_m_offset') else None


    class DirInode(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            if self._io.size() > 0:
                self.children = []
                i = 0
                while not self._io.is_eof():
                    self.children.append(Cramfs.Inode(self._io, self, self._root))
                    i += 1




    class Info(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.crc = self._io.read_u4le()
            self.edition = self._io.read_u4le()
            self.blocks = self._io.read_u4le()
            self.files = self._io.read_u4le()


    @property
    def page_size(self):
        if hasattr(self, '_m_page_size'):
            return self._m_page_size if hasattr(self, '_m_page_size') else None

        self._m_page_size = 4096
        return self._m_page_size if hasattr(self, '_m_page_size') else None


