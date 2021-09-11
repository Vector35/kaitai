# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class DoomWad(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = (self._io.read_bytes(4)).decode(u"ASCII")
        self.num_index_entries = self._io.read_s4le()
        self.index_offset = self._io.read_s4le()

    class Sectors(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self.entries.append(DoomWad.Sector(self._io, self, self._root))
                i += 1



    class Vertex(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_s2le()
            self.y = self._io.read_s2le()


    class Texture12(KaitaiStruct):
        """Used for TEXTURE1 and TEXTURE2 lumps, which designate how to
        combine wall patches to make wall textures. This essentially
        provides a very simple form of image compression, allowing
        certain elements ("patches") to be reused / recombined on
        different textures for more variety in the game.
        
        .. seealso::
           Source - http://doom.wikia.com/wiki/TEXTURE1
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_textures = self._io.read_s4le()
            self.textures = [None] * (self.num_textures)
            for i in range(self.num_textures):
                self.textures[i] = DoomWad.Texture12.TextureIndex(self._io, self, self._root)


        class TextureIndex(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.offset = self._io.read_s4le()

            @property
            def body(self):
                if hasattr(self, '_m_body'):
                    return self._m_body if hasattr(self, '_m_body') else None

                _pos = self._io.pos()
                self._io.seek(self.offset)
                self._m_body = DoomWad.Texture12.TextureBody(self._io, self, self._root)
                self._io.seek(_pos)
                return self._m_body if hasattr(self, '_m_body') else None


        class TextureBody(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.name = (KaitaiStream.bytes_strip_right(self._io.read_bytes(8), 0)).decode(u"ASCII")
                self.masked = self._io.read_u4le()
                self.width = self._io.read_u2le()
                self.height = self._io.read_u2le()
                self.column_directory = self._io.read_u4le()
                self.num_patches = self._io.read_u2le()
                self.patches = [None] * (self.num_patches)
                for i in range(self.num_patches):
                    self.patches[i] = DoomWad.Texture12.Patch(self._io, self, self._root)



        class Patch(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.origin_x = self._io.read_s2le()
                self.origin_y = self._io.read_s2le()
                self.patch_id = self._io.read_u2le()
                self.step_dir = self._io.read_u2le()
                self.colormap = self._io.read_u2le()



    class Linedef(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.vertex_start_idx = self._io.read_u2le()
            self.vertex_end_idx = self._io.read_u2le()
            self.flags = self._io.read_u2le()
            self.line_type = self._io.read_u2le()
            self.sector_tag = self._io.read_u2le()
            self.sidedef_right_idx = self._io.read_u2le()
            self.sidedef_left_idx = self._io.read_u2le()


    class Pnames(KaitaiStruct):
        """
        .. seealso::
           Source - http://doom.wikia.com/wiki/PNAMES
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_patches = self._io.read_u4le()
            self.names = [None] * (self.num_patches)
            for i in range(self.num_patches):
                self.names[i] = (KaitaiStream.bytes_strip_right(self._io.read_bytes(8), 0)).decode(u"ASCII")



    class Thing(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_s2le()
            self.y = self._io.read_s2le()
            self.angle = self._io.read_u2le()
            self.type = self._io.read_u2le()
            self.flags = self._io.read_u2le()


    class Sector(KaitaiStruct):

        class SpecialSector(Enum):
            normal = 0
            d_light_flicker = 1
            d_light_strobe_fast = 2
            d_light_strobe_slow = 3
            d_light_strobe_hurt = 4
            d_damage_hellslime = 5
            d_damage_nukage = 7
            d_light_glow = 8
            secret = 9
            d_sector_door_close_in_30 = 10
            d_damage_end = 11
            d_light_strobe_slow_sync = 12
            d_light_strobe_fast_sync = 13
            d_sector_door_raise_in_5_mins = 14
            d_friction_low = 15
            d_damage_super_hellslime = 16
            d_light_fire_flicker = 17
            d_damage_lava_wimpy = 18
            d_damage_lava_hefty = 19
            d_scroll_east_lava_damage = 20
            light_phased = 21
            light_sequence_start = 22
            light_sequence_special1 = 23
            light_sequence_special2 = 24
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.floor_z = self._io.read_s2le()
            self.ceil_z = self._io.read_s2le()
            self.floor_flat = (self._io.read_bytes(8)).decode(u"ASCII")
            self.ceil_flat = (self._io.read_bytes(8)).decode(u"ASCII")
            self.light = self._io.read_s2le()
            self.special_type = KaitaiStream.resolve_enum(DoomWad.Sector.SpecialSector, self._io.read_u2le())
            self.tag = self._io.read_u2le()


    class Vertexes(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self.entries.append(DoomWad.Vertex(self._io, self, self._root))
                i += 1



    class Sidedef(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.offset_x = self._io.read_s2le()
            self.offset_y = self._io.read_s2le()
            self.upper_texture_name = (self._io.read_bytes(8)).decode(u"ASCII")
            self.lower_texture_name = (self._io.read_bytes(8)).decode(u"ASCII")
            self.normal_texture_name = (self._io.read_bytes(8)).decode(u"ASCII")
            self.sector_id = self._io.read_s2le()


    class Things(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self.entries.append(DoomWad.Thing(self._io, self, self._root))
                i += 1



    class Linedefs(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self.entries.append(DoomWad.Linedef(self._io, self, self._root))
                i += 1



    class IndexEntry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.offset = self._io.read_s4le()
            self.size = self._io.read_s4le()
            self.name = (KaitaiStream.bytes_strip_right(self._io.read_bytes(8), 0)).decode(u"ASCII")

        @property
        def contents(self):
            if hasattr(self, '_m_contents'):
                return self._m_contents if hasattr(self, '_m_contents') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.offset)
            _on = self.name
            if _on == u"SECTORS":
                self._raw__m_contents = io.read_bytes(self.size)
                _io__raw__m_contents = KaitaiStream(BytesIO(self._raw__m_contents))
                self._m_contents = DoomWad.Sectors(_io__raw__m_contents, self, self._root)
            elif _on == u"TEXTURE1":
                self._raw__m_contents = io.read_bytes(self.size)
                _io__raw__m_contents = KaitaiStream(BytesIO(self._raw__m_contents))
                self._m_contents = DoomWad.Texture12(_io__raw__m_contents, self, self._root)
            elif _on == u"VERTEXES":
                self._raw__m_contents = io.read_bytes(self.size)
                _io__raw__m_contents = KaitaiStream(BytesIO(self._raw__m_contents))
                self._m_contents = DoomWad.Vertexes(_io__raw__m_contents, self, self._root)
            elif _on == u"BLOCKMAP":
                self._raw__m_contents = io.read_bytes(self.size)
                _io__raw__m_contents = KaitaiStream(BytesIO(self._raw__m_contents))
                self._m_contents = DoomWad.Blockmap(_io__raw__m_contents, self, self._root)
            elif _on == u"PNAMES":
                self._raw__m_contents = io.read_bytes(self.size)
                _io__raw__m_contents = KaitaiStream(BytesIO(self._raw__m_contents))
                self._m_contents = DoomWad.Pnames(_io__raw__m_contents, self, self._root)
            elif _on == u"TEXTURE2":
                self._raw__m_contents = io.read_bytes(self.size)
                _io__raw__m_contents = KaitaiStream(BytesIO(self._raw__m_contents))
                self._m_contents = DoomWad.Texture12(_io__raw__m_contents, self, self._root)
            elif _on == u"THINGS":
                self._raw__m_contents = io.read_bytes(self.size)
                _io__raw__m_contents = KaitaiStream(BytesIO(self._raw__m_contents))
                self._m_contents = DoomWad.Things(_io__raw__m_contents, self, self._root)
            elif _on == u"LINEDEFS":
                self._raw__m_contents = io.read_bytes(self.size)
                _io__raw__m_contents = KaitaiStream(BytesIO(self._raw__m_contents))
                self._m_contents = DoomWad.Linedefs(_io__raw__m_contents, self, self._root)
            elif _on == u"SIDEDEFS":
                self._raw__m_contents = io.read_bytes(self.size)
                _io__raw__m_contents = KaitaiStream(BytesIO(self._raw__m_contents))
                self._m_contents = DoomWad.Sidedefs(_io__raw__m_contents, self, self._root)
            else:
                self._m_contents = io.read_bytes(self.size)
            io.seek(_pos)
            return self._m_contents if hasattr(self, '_m_contents') else None


    class Sidedefs(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self.entries.append(DoomWad.Sidedef(self._io, self, self._root))
                i += 1



    class Blockmap(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.origin_x = self._io.read_s2le()
            self.origin_y = self._io.read_s2le()
            self.num_cols = self._io.read_s2le()
            self.num_rows = self._io.read_s2le()
            self.linedefs_in_block = [None] * ((self.num_cols * self.num_rows))
            for i in range((self.num_cols * self.num_rows)):
                self.linedefs_in_block[i] = DoomWad.Blockmap.Blocklist(self._io, self, self._root)


        class Blocklist(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.offset = self._io.read_u2le()

            @property
            def linedefs(self):
                """List of linedefs found in this block."""
                if hasattr(self, '_m_linedefs'):
                    return self._m_linedefs if hasattr(self, '_m_linedefs') else None

                _pos = self._io.pos()
                self._io.seek((self.offset * 2))
                self._m_linedefs = []
                i = 0
                while True:
                    _ = self._io.read_s2le()
                    self._m_linedefs.append(_)
                    if _ == -1:
                        break
                    i += 1
                self._io.seek(_pos)
                return self._m_linedefs if hasattr(self, '_m_linedefs') else None



    @property
    def index(self):
        if hasattr(self, '_m_index'):
            return self._m_index if hasattr(self, '_m_index') else None

        _pos = self._io.pos()
        self._io.seek(self.index_offset)
        self._m_index = [None] * (self.num_index_entries)
        for i in range(self.num_index_entries):
            self._m_index[i] = DoomWad.IndexEntry(self._io, self, self._root)

        self._io.seek(_pos)
        return self._m_index if hasattr(self, '_m_index') else None


