# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class BlenderBlend(KaitaiStruct):
    """Blender is an open source suite for 3D modelling, sculpting,
    animation, compositing, rendering, preparation of assets for its own
    game engine and exporting to others, etc. `.blend` is its own binary
    format that saves whole state of suite: current scene, animations,
    all software settings, extensions, etc.
    
    Internally, .blend format is a hybrid semi-self-descriptive
    format. On top level, it contains a simple header and a sequence of
    file blocks, which more or less follow typical [TLV
    pattern](https://en.wikipedia.org/wiki/Type-length-value). Pre-last
    block would be a structure with code `DNA1`, which is a essentially
    a machine-readable schema of all other structures used in this file.
    """

    class PtrSize(Enum):
        bits_64 = 45
        bits_32 = 95

    class Endian(Enum):
        be = 86
        le = 118
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.hdr = BlenderBlend.Header(self._io, self, self._root)
        self.blocks = []
        i = 0
        while not self._io.is_eof():
            self.blocks.append(BlenderBlend.FileBlock(self._io, self, self._root))
            i += 1


    class DnaStruct(KaitaiStruct):
        """DNA struct contains a `type` (type name), which is specified as
        an index in types table, and sequence of fields.
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.idx_type = self._io.read_u2le()
            self.num_fields = self._io.read_u2le()
            self.fields = [None] * (self.num_fields)
            for i in range(self.num_fields):
                self.fields[i] = BlenderBlend.DnaField(self._io, self, self._root)


        @property
        def type(self):
            if hasattr(self, '_m_type'):
                return self._m_type if hasattr(self, '_m_type') else None

            self._m_type = self._parent.types[self.idx_type]
            return self._m_type if hasattr(self, '_m_type') else None


    class FileBlock(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.code = (self._io.read_bytes(4)).decode(u"ASCII")
            self.len_body = self._io.read_u4le()
            self.mem_addr = self._io.read_bytes(self._root.hdr.psize)
            self.sdna_index = self._io.read_u4le()
            self.count = self._io.read_u4le()
            _on = self.code
            if _on == u"DNA1":
                self._raw_body = self._io.read_bytes(self.len_body)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = BlenderBlend.Dna1Body(_io__raw_body, self, self._root)
            else:
                self.body = self._io.read_bytes(self.len_body)

        @property
        def sdna_struct(self):
            if hasattr(self, '_m_sdna_struct'):
                return self._m_sdna_struct if hasattr(self, '_m_sdna_struct') else None

            if self.sdna_index != 0:
                self._m_sdna_struct = self._root.sdna_structs[self.sdna_index]

            return self._m_sdna_struct if hasattr(self, '_m_sdna_struct') else None


    class Dna1Body(KaitaiStruct):
        """DNA1, also known as "Structure DNA", is a special block in
        .blend file, which contains machine-readable specifications of
        all other structures used in this .blend file.
        
        Effectively, this block contains:
        
        * a sequence of "names" (strings which represent field names)
        * a sequence of "types" (strings which represent type name)
        * a sequence of "type lengths"
        * a sequence of "structs" (which describe contents of every
          structure, referring to types and names by index)
        
        .. seealso::
           Source - https://en.blender.org/index.php/Dev:Source/Architecture/File_Format#Structure_DNA
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.id = self._io.read_bytes(4)
            if not self.id == b"\x53\x44\x4E\x41":
                raise kaitaistruct.ValidationNotEqualError(b"\x53\x44\x4E\x41", self.id, self._io, u"/types/dna1_body/seq/0")
            self.name_magic = self._io.read_bytes(4)
            if not self.name_magic == b"\x4E\x41\x4D\x45":
                raise kaitaistruct.ValidationNotEqualError(b"\x4E\x41\x4D\x45", self.name_magic, self._io, u"/types/dna1_body/seq/1")
            self.num_names = self._io.read_u4le()
            self.names = [None] * (self.num_names)
            for i in range(self.num_names):
                self.names[i] = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")

            self.padding_1 = self._io.read_bytes(((4 - self._io.pos()) % 4))
            self.type_magic = self._io.read_bytes(4)
            if not self.type_magic == b"\x54\x59\x50\x45":
                raise kaitaistruct.ValidationNotEqualError(b"\x54\x59\x50\x45", self.type_magic, self._io, u"/types/dna1_body/seq/5")
            self.num_types = self._io.read_u4le()
            self.types = [None] * (self.num_types)
            for i in range(self.num_types):
                self.types[i] = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")

            self.padding_2 = self._io.read_bytes(((4 - self._io.pos()) % 4))
            self.tlen_magic = self._io.read_bytes(4)
            if not self.tlen_magic == b"\x54\x4C\x45\x4E":
                raise kaitaistruct.ValidationNotEqualError(b"\x54\x4C\x45\x4E", self.tlen_magic, self._io, u"/types/dna1_body/seq/9")
            self.lengths = [None] * (self.num_types)
            for i in range(self.num_types):
                self.lengths[i] = self._io.read_u2le()

            self.padding_3 = self._io.read_bytes(((4 - self._io.pos()) % 4))
            self.strc_magic = self._io.read_bytes(4)
            if not self.strc_magic == b"\x53\x54\x52\x43":
                raise kaitaistruct.ValidationNotEqualError(b"\x53\x54\x52\x43", self.strc_magic, self._io, u"/types/dna1_body/seq/12")
            self.num_structs = self._io.read_u4le()
            self.structs = [None] * (self.num_structs)
            for i in range(self.num_structs):
                self.structs[i] = BlenderBlend.DnaStruct(self._io, self, self._root)



    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(7)
            if not self.magic == b"\x42\x4C\x45\x4E\x44\x45\x52":
                raise kaitaistruct.ValidationNotEqualError(b"\x42\x4C\x45\x4E\x44\x45\x52", self.magic, self._io, u"/types/header/seq/0")
            self.ptr_size_id = KaitaiStream.resolve_enum(BlenderBlend.PtrSize, self._io.read_u1())
            self.endian = KaitaiStream.resolve_enum(BlenderBlend.Endian, self._io.read_u1())
            self.version = (self._io.read_bytes(3)).decode(u"ASCII")

        @property
        def psize(self):
            """Number of bytes that a pointer occupies."""
            if hasattr(self, '_m_psize'):
                return self._m_psize if hasattr(self, '_m_psize') else None

            self._m_psize = (8 if self.ptr_size_id == BlenderBlend.PtrSize.bits_64 else 4)
            return self._m_psize if hasattr(self, '_m_psize') else None


    class DnaField(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.idx_type = self._io.read_u2le()
            self.idx_name = self._io.read_u2le()

        @property
        def type(self):
            if hasattr(self, '_m_type'):
                return self._m_type if hasattr(self, '_m_type') else None

            self._m_type = self._parent._parent.types[self.idx_type]
            return self._m_type if hasattr(self, '_m_type') else None

        @property
        def name(self):
            if hasattr(self, '_m_name'):
                return self._m_name if hasattr(self, '_m_name') else None

            self._m_name = self._parent._parent.names[self.idx_name]
            return self._m_name if hasattr(self, '_m_name') else None


    @property
    def sdna_structs(self):
        if hasattr(self, '_m_sdna_structs'):
            return self._m_sdna_structs if hasattr(self, '_m_sdna_structs') else None

        self._m_sdna_structs = self.blocks[(len(self.blocks) - 2)].body.structs
        return self._m_sdna_structs if hasattr(self, '_m_sdna_structs') else None


