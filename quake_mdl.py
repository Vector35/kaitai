# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class QuakeMdl(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.header = QuakeMdl.MdlHeader(self._io, self, self._root)
        self.skins = [None] * (self.header.num_skins)
        for i in range(self.header.num_skins):
            self.skins[i] = QuakeMdl.MdlSkin(self._io, self, self._root)

        self.texture_coordinates = [None] * (self.header.num_verts)
        for i in range(self.header.num_verts):
            self.texture_coordinates[i] = QuakeMdl.MdlTexcoord(self._io, self, self._root)

        self.triangles = [None] * (self.header.num_tris)
        for i in range(self.header.num_tris):
            self.triangles[i] = QuakeMdl.MdlTriangle(self._io, self, self._root)

        self.frames = [None] * (self.header.num_frames)
        for i in range(self.header.num_frames):
            self.frames[i] = QuakeMdl.MdlFrame(self._io, self, self._root)


    class MdlVertex(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.values = [None] * (3)
            for i in range(3):
                self.values[i] = self._io.read_u1()

            self.normal_index = self._io.read_u1()


    class MdlTexcoord(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.on_seam = self._io.read_s4le()
            self.s = self._io.read_s4le()
            self.t = self._io.read_s4le()


    class MdlHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ident = self._io.read_bytes(4)
            if not self.ident == b"\x49\x44\x50\x4F":
                raise kaitaistruct.ValidationNotEqualError(b"\x49\x44\x50\x4F", self.ident, self._io, u"/types/mdl_header/seq/0")
            self.version_must_be_6 = self._io.read_bytes(4)
            if not self.version_must_be_6 == b"\x06\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x06\x00\x00\x00", self.version_must_be_6, self._io, u"/types/mdl_header/seq/1")
            self.scale = QuakeMdl.Vec3(self._io, self, self._root)
            self.origin = QuakeMdl.Vec3(self._io, self, self._root)
            self.radius = self._io.read_f4le()
            self.eye_position = QuakeMdl.Vec3(self._io, self, self._root)
            self.num_skins = self._io.read_s4le()
            self.skin_width = self._io.read_s4le()
            self.skin_height = self._io.read_s4le()
            self.num_verts = self._io.read_s4le()
            self.num_tris = self._io.read_s4le()
            self.num_frames = self._io.read_s4le()
            self.synctype = self._io.read_s4le()
            self.flags = self._io.read_s4le()
            self.size = self._io.read_f4le()

        @property
        def version(self):
            if hasattr(self, '_m_version'):
                return self._m_version if hasattr(self, '_m_version') else None

            self._m_version = 6
            return self._m_version if hasattr(self, '_m_version') else None

        @property
        def skin_size(self):
            if hasattr(self, '_m_skin_size'):
                return self._m_skin_size if hasattr(self, '_m_skin_size') else None

            self._m_skin_size = (self.skin_width * self.skin_height)
            return self._m_skin_size if hasattr(self, '_m_skin_size') else None


    class MdlSkin(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.group = self._io.read_s4le()
            if self.group == 0:
                self.single_texture_data = self._io.read_bytes(self._root.header.skin_size)

            if self.group != 0:
                self.num_frames = self._io.read_u4le()

            if self.group != 0:
                self.frame_times = [None] * (self.num_frames)
                for i in range(self.num_frames):
                    self.frame_times[i] = self._io.read_f4le()


            if self.group != 0:
                self.group_texture_data = [None] * (self.num_frames)
                for i in range(self.num_frames):
                    self.group_texture_data[i] = self._io.read_bytes(self._root.header.skin_size)




    class MdlFrame(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.type = self._io.read_s4le()
            if self.type != 0:
                self.min = QuakeMdl.MdlVertex(self._io, self, self._root)

            if self.type != 0:
                self.max = QuakeMdl.MdlVertex(self._io, self, self._root)

            if self.type != 0:
                self.time = [None] * (self.type)
                for i in range(self.type):
                    self.time[i] = self._io.read_f4le()


            self.frames = [None] * (self.num_simple_frames)
            for i in range(self.num_simple_frames):
                self.frames[i] = QuakeMdl.MdlSimpleFrame(self._io, self, self._root)


        @property
        def num_simple_frames(self):
            if hasattr(self, '_m_num_simple_frames'):
                return self._m_num_simple_frames if hasattr(self, '_m_num_simple_frames') else None

            self._m_num_simple_frames = (1 if self.type == 0 else self.type)
            return self._m_num_simple_frames if hasattr(self, '_m_num_simple_frames') else None


    class MdlSimpleFrame(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.bbox_min = QuakeMdl.MdlVertex(self._io, self, self._root)
            self.bbox_max = QuakeMdl.MdlVertex(self._io, self, self._root)
            self.name = (KaitaiStream.bytes_terminate(KaitaiStream.bytes_strip_right(self._io.read_bytes(16), 0), 0, False)).decode(u"ASCII")
            self.vertices = [None] * (self._root.header.num_verts)
            for i in range(self._root.header.num_verts):
                self.vertices[i] = QuakeMdl.MdlVertex(self._io, self, self._root)



    class MdlTriangle(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.faces_front = self._io.read_s4le()
            self.vertices = [None] * (3)
            for i in range(3):
                self.vertices[i] = self._io.read_s4le()



    class Vec3(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_f4le()
            self.y = self._io.read_f4le()
            self.z = self._io.read_f4le()



