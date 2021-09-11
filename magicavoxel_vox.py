# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class MagicavoxelVox(KaitaiStruct):
    """
    .. seealso::
       MagicaVoxel Homepage - https://ephtracy.github.io/
    
    
    .. seealso::
       Format Description - https://github.com/ephtracy/voxel-model/blob/master/MagicaVoxel-file-format-vox.txt
    """

    class ChunkType(Enum):
        main = 1296124238
        matt = 1296127060
        pack = 1346454347
        rgba = 1380401729
        size = 1397316165
        xyzi = 1482250825

    class MaterialType(Enum):
        diffuse = 0
        metal = 1
        glass = 2
        emissive = 3

    class PropertyBitsType(Enum):
        plastic = 1
        roughness = 2
        specular = 4
        ior = 8
        attenuation = 16
        power = 32
        glow = 64
        is_total_power = 128
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(4)
        if not self.magic == b"\x56\x4F\x58\x20":
            raise kaitaistruct.ValidationNotEqualError(b"\x56\x4F\x58\x20", self.magic, self._io, u"/seq/0")
        self.version = self._io.read_u4le()
        self.main = MagicavoxelVox.Chunk(self._io, self, self._root)

    class Chunk(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.chunk_id = KaitaiStream.resolve_enum(MagicavoxelVox.ChunkType, self._io.read_u4be())
            self.num_bytes_of_chunk_content = self._io.read_u4le()
            self.num_bytes_of_children_chunks = self._io.read_u4le()
            if self.num_bytes_of_chunk_content != 0:
                _on = self.chunk_id
                if _on == MagicavoxelVox.ChunkType.size:
                    self._raw_chunk_content = self._io.read_bytes(self.num_bytes_of_chunk_content)
                    _io__raw_chunk_content = KaitaiStream(BytesIO(self._raw_chunk_content))
                    self.chunk_content = MagicavoxelVox.Size(_io__raw_chunk_content, self, self._root)
                elif _on == MagicavoxelVox.ChunkType.matt:
                    self._raw_chunk_content = self._io.read_bytes(self.num_bytes_of_chunk_content)
                    _io__raw_chunk_content = KaitaiStream(BytesIO(self._raw_chunk_content))
                    self.chunk_content = MagicavoxelVox.Matt(_io__raw_chunk_content, self, self._root)
                elif _on == MagicavoxelVox.ChunkType.rgba:
                    self._raw_chunk_content = self._io.read_bytes(self.num_bytes_of_chunk_content)
                    _io__raw_chunk_content = KaitaiStream(BytesIO(self._raw_chunk_content))
                    self.chunk_content = MagicavoxelVox.Rgba(_io__raw_chunk_content, self, self._root)
                elif _on == MagicavoxelVox.ChunkType.xyzi:
                    self._raw_chunk_content = self._io.read_bytes(self.num_bytes_of_chunk_content)
                    _io__raw_chunk_content = KaitaiStream(BytesIO(self._raw_chunk_content))
                    self.chunk_content = MagicavoxelVox.Xyzi(_io__raw_chunk_content, self, self._root)
                elif _on == MagicavoxelVox.ChunkType.pack:
                    self._raw_chunk_content = self._io.read_bytes(self.num_bytes_of_chunk_content)
                    _io__raw_chunk_content = KaitaiStream(BytesIO(self._raw_chunk_content))
                    self.chunk_content = MagicavoxelVox.Pack(_io__raw_chunk_content, self, self._root)
                else:
                    self.chunk_content = self._io.read_bytes(self.num_bytes_of_chunk_content)

            if self.num_bytes_of_children_chunks != 0:
                self.children_chunks = []
                i = 0
                while not self._io.is_eof():
                    self.children_chunks.append(MagicavoxelVox.Chunk(self._io, self, self._root))
                    i += 1




    class Size(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.size_x = self._io.read_u4le()
            self.size_y = self._io.read_u4le()
            self.size_z = self._io.read_u4le()


    class Rgba(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.colors = [None] * (256)
            for i in range(256):
                self.colors[i] = MagicavoxelVox.Color(self._io, self, self._root)



    class Pack(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_models = self._io.read_u4le()


    class Matt(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.id = self._io.read_u4le()
            self.material_type = KaitaiStream.resolve_enum(MagicavoxelVox.MaterialType, self._io.read_u4le())
            self.material_weight = self._io.read_f4le()
            self.property_bits = self._io.read_u4le()
            if self.has_plastic:
                self.plastic = self._io.read_f4le()

            if self.has_roughness:
                self.roughness = self._io.read_f4le()

            if self.has_specular:
                self.specular = self._io.read_f4le()

            if self.has_ior:
                self.ior = self._io.read_f4le()

            if self.has_attenuation:
                self.attenuation = self._io.read_f4le()

            if self.has_power:
                self.power = self._io.read_f4le()

            if self.has_glow:
                self.glow = self._io.read_f4le()

            if self.has_is_total_power:
                self.is_total_power = self._io.read_f4le()


        @property
        def has_is_total_power(self):
            if hasattr(self, '_m_has_is_total_power'):
                return self._m_has_is_total_power if hasattr(self, '_m_has_is_total_power') else None

            self._m_has_is_total_power = (self.property_bits & 128) != 0
            return self._m_has_is_total_power if hasattr(self, '_m_has_is_total_power') else None

        @property
        def has_plastic(self):
            if hasattr(self, '_m_has_plastic'):
                return self._m_has_plastic if hasattr(self, '_m_has_plastic') else None

            self._m_has_plastic = (self.property_bits & 1) != 0
            return self._m_has_plastic if hasattr(self, '_m_has_plastic') else None

        @property
        def has_attenuation(self):
            if hasattr(self, '_m_has_attenuation'):
                return self._m_has_attenuation if hasattr(self, '_m_has_attenuation') else None

            self._m_has_attenuation = (self.property_bits & 16) != 0
            return self._m_has_attenuation if hasattr(self, '_m_has_attenuation') else None

        @property
        def has_power(self):
            if hasattr(self, '_m_has_power'):
                return self._m_has_power if hasattr(self, '_m_has_power') else None

            self._m_has_power = (self.property_bits & 32) != 0
            return self._m_has_power if hasattr(self, '_m_has_power') else None

        @property
        def has_roughness(self):
            if hasattr(self, '_m_has_roughness'):
                return self._m_has_roughness if hasattr(self, '_m_has_roughness') else None

            self._m_has_roughness = (self.property_bits & 2) != 0
            return self._m_has_roughness if hasattr(self, '_m_has_roughness') else None

        @property
        def has_specular(self):
            if hasattr(self, '_m_has_specular'):
                return self._m_has_specular if hasattr(self, '_m_has_specular') else None

            self._m_has_specular = (self.property_bits & 4) != 0
            return self._m_has_specular if hasattr(self, '_m_has_specular') else None

        @property
        def has_ior(self):
            if hasattr(self, '_m_has_ior'):
                return self._m_has_ior if hasattr(self, '_m_has_ior') else None

            self._m_has_ior = (self.property_bits & 8) != 0
            return self._m_has_ior if hasattr(self, '_m_has_ior') else None

        @property
        def has_glow(self):
            if hasattr(self, '_m_has_glow'):
                return self._m_has_glow if hasattr(self, '_m_has_glow') else None

            self._m_has_glow = (self.property_bits & 64) != 0
            return self._m_has_glow if hasattr(self, '_m_has_glow') else None


    class Xyzi(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_voxels = self._io.read_u4le()
            self.voxels = [None] * (self.num_voxels)
            for i in range(self.num_voxels):
                self.voxels[i] = MagicavoxelVox.Voxel(self._io, self, self._root)



    class Color(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.r = self._io.read_u1()
            self.g = self._io.read_u1()
            self.b = self._io.read_u1()
            self.a = self._io.read_u1()


    class Voxel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_u1()
            self.y = self._io.read_u1()
            self.z = self._io.read_u1()
            self.color_index = self._io.read_u1()



