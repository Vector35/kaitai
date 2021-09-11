# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class MicrosoftCfb(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.header = MicrosoftCfb.CfbHeader(self._io, self, self._root)

    class CfbHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.signature = self._io.read_bytes(8)
            if not self.signature == b"\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1":
                raise kaitaistruct.ValidationNotEqualError(b"\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1", self.signature, self._io, u"/types/cfb_header/seq/0")
            self.clsid = self._io.read_bytes(16)
            if not self.clsid == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", self.clsid, self._io, u"/types/cfb_header/seq/1")
            self.version_minor = self._io.read_u2le()
            self.version_major = self._io.read_u2le()
            self.byte_order = self._io.read_bytes(2)
            if not self.byte_order == b"\xFE\xFF":
                raise kaitaistruct.ValidationNotEqualError(b"\xFE\xFF", self.byte_order, self._io, u"/types/cfb_header/seq/4")
            self.sector_shift = self._io.read_u2le()
            self.mini_sector_shift = self._io.read_u2le()
            self.reserved1 = self._io.read_bytes(6)
            self.size_dir = self._io.read_s4le()
            self.size_fat = self._io.read_s4le()
            self.ofs_dir = self._io.read_s4le()
            self.transaction_seq = self._io.read_s4le()
            self.mini_stream_cutoff_size = self._io.read_s4le()
            self.ofs_mini_fat = self._io.read_s4le()
            self.size_mini_fat = self._io.read_s4le()
            self.ofs_difat = self._io.read_s4le()
            self.size_difat = self._io.read_s4le()
            self.difat = [None] * (109)
            for i in range(109):
                self.difat[i] = self._io.read_s4le()



    class FatEntries(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self.entries.append(self._io.read_s4le())
                i += 1



    class DirEntry(KaitaiStruct):

        class ObjType(Enum):
            unknown = 0
            storage = 1
            stream = 2
            root_storage = 5

        class RbColor(Enum):
            red = 0
            black = 1
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = (self._io.read_bytes(64)).decode(u"UTF-16LE")
            self.name_len = self._io.read_u2le()
            self.object_type = KaitaiStream.resolve_enum(MicrosoftCfb.DirEntry.ObjType, self._io.read_u1())
            self.color_flag = KaitaiStream.resolve_enum(MicrosoftCfb.DirEntry.RbColor, self._io.read_u1())
            self.left_sibling_id = self._io.read_s4le()
            self.right_sibling_id = self._io.read_s4le()
            self.child_id = self._io.read_s4le()
            self.clsid = self._io.read_bytes(16)
            self.state = self._io.read_u4le()
            self.time_create = self._io.read_u8le()
            self.time_mod = self._io.read_u8le()
            self.ofs = self._io.read_s4le()
            self.size = self._io.read_u8le()

        @property
        def mini_stream(self):
            if hasattr(self, '_m_mini_stream'):
                return self._m_mini_stream if hasattr(self, '_m_mini_stream') else None

            if self.object_type == MicrosoftCfb.DirEntry.ObjType.root_storage:
                io = self._root._io
                _pos = io.pos()
                io.seek(((self.ofs + 1) * self._root.sector_size))
                self._m_mini_stream = io.read_bytes(self.size)
                io.seek(_pos)

            return self._m_mini_stream if hasattr(self, '_m_mini_stream') else None

        @property
        def child(self):
            if hasattr(self, '_m_child'):
                return self._m_child if hasattr(self, '_m_child') else None

            if self.child_id != -1:
                io = self._root._io
                _pos = io.pos()
                io.seek((((self._root.header.ofs_dir + 1) * self._root.sector_size) + (self.child_id * 128)))
                self._m_child = MicrosoftCfb.DirEntry(io, self, self._root)
                io.seek(_pos)

            return self._m_child if hasattr(self, '_m_child') else None

        @property
        def left_sibling(self):
            if hasattr(self, '_m_left_sibling'):
                return self._m_left_sibling if hasattr(self, '_m_left_sibling') else None

            if self.left_sibling_id != -1:
                io = self._root._io
                _pos = io.pos()
                io.seek((((self._root.header.ofs_dir + 1) * self._root.sector_size) + (self.left_sibling_id * 128)))
                self._m_left_sibling = MicrosoftCfb.DirEntry(io, self, self._root)
                io.seek(_pos)

            return self._m_left_sibling if hasattr(self, '_m_left_sibling') else None

        @property
        def right_sibling(self):
            if hasattr(self, '_m_right_sibling'):
                return self._m_right_sibling if hasattr(self, '_m_right_sibling') else None

            if self.right_sibling_id != -1:
                io = self._root._io
                _pos = io.pos()
                io.seek((((self._root.header.ofs_dir + 1) * self._root.sector_size) + (self.right_sibling_id * 128)))
                self._m_right_sibling = MicrosoftCfb.DirEntry(io, self, self._root)
                io.seek(_pos)

            return self._m_right_sibling if hasattr(self, '_m_right_sibling') else None


    @property
    def sector_size(self):
        if hasattr(self, '_m_sector_size'):
            return self._m_sector_size if hasattr(self, '_m_sector_size') else None

        self._m_sector_size = (1 << self.header.sector_shift)
        return self._m_sector_size if hasattr(self, '_m_sector_size') else None

    @property
    def fat(self):
        if hasattr(self, '_m_fat'):
            return self._m_fat if hasattr(self, '_m_fat') else None

        _pos = self._io.pos()
        self._io.seek(self.sector_size)
        self._raw__m_fat = self._io.read_bytes((self.header.size_fat * self.sector_size))
        _io__raw__m_fat = KaitaiStream(BytesIO(self._raw__m_fat))
        self._m_fat = MicrosoftCfb.FatEntries(_io__raw__m_fat, self, self._root)
        self._io.seek(_pos)
        return self._m_fat if hasattr(self, '_m_fat') else None

    @property
    def dir(self):
        if hasattr(self, '_m_dir'):
            return self._m_dir if hasattr(self, '_m_dir') else None

        _pos = self._io.pos()
        self._io.seek(((self.header.ofs_dir + 1) * self.sector_size))
        self._m_dir = MicrosoftCfb.DirEntry(self._io, self, self._root)
        self._io.seek(_pos)
        return self._m_dir if hasattr(self, '_m_dir') else None


