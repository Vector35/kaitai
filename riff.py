# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Riff(KaitaiStruct):
    """The Resource Interchange File Format (RIFF) is a generic file container format
    for storing data in tagged chunks. It is primarily used to store multimedia
    such as sound and video, though it may also be used to store any arbitrary data.
    
    The Microsoft implementation is mostly known through container formats
    like AVI, ANI and WAV, which use RIFF as their basis.
    
    .. seealso::
       Source - https://www.johnloomis.org/cpe102/asgn/asgn1/riff.html
    """

    class Fourcc(Enum):
        riff = 1179011410
        info = 1330007625
        list = 1414744396
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.chunk = Riff.Chunk(self._io, self, self._root)

    class ListChunkData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            if self.parent_chunk_data_ofs < 0:
                self.save_parent_chunk_data_ofs = self._io.read_bytes(0)

            self.parent_chunk_data = Riff.ParentChunkData(self._io, self, self._root)

        @property
        def parent_chunk_data_ofs(self):
            if hasattr(self, '_m_parent_chunk_data_ofs'):
                return self._m_parent_chunk_data_ofs if hasattr(self, '_m_parent_chunk_data_ofs') else None

            self._m_parent_chunk_data_ofs = self._io.pos()
            return self._m_parent_chunk_data_ofs if hasattr(self, '_m_parent_chunk_data_ofs') else None

        @property
        def form_type(self):
            if hasattr(self, '_m_form_type'):
                return self._m_form_type if hasattr(self, '_m_form_type') else None

            self._m_form_type = KaitaiStream.resolve_enum(Riff.Fourcc, self.parent_chunk_data.form_type)
            return self._m_form_type if hasattr(self, '_m_form_type') else None

        @property
        def form_type_readable(self):
            if hasattr(self, '_m_form_type_readable'):
                return self._m_form_type_readable if hasattr(self, '_m_form_type_readable') else None

            _pos = self._io.pos()
            self._io.seek(self.parent_chunk_data_ofs)
            self._m_form_type_readable = (self._io.read_bytes(4)).decode(u"ASCII")
            self._io.seek(_pos)
            return self._m_form_type_readable if hasattr(self, '_m_form_type_readable') else None

        @property
        def subchunks(self):
            if hasattr(self, '_m_subchunks'):
                return self._m_subchunks if hasattr(self, '_m_subchunks') else None

            io = self.parent_chunk_data.subchunks_slot._io
            _pos = io.pos()
            io.seek(0)
            self._m_subchunks = []
            i = 0
            while not io.is_eof():
                _on = self.form_type
                if _on == Riff.Fourcc.info:
                    self._m_subchunks.append(Riff.InfoSubchunk(io, self, self._root))
                else:
                    self._m_subchunks.append(Riff.ChunkType(io, self, self._root))
                i += 1

            io.seek(_pos)
            return self._m_subchunks if hasattr(self, '_m_subchunks') else None


    class Chunk(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.id = self._io.read_u4le()
            self.len = self._io.read_u4le()
            self._raw_data_slot = self._io.read_bytes(self.len)
            _io__raw_data_slot = KaitaiStream(BytesIO(self._raw_data_slot))
            self.data_slot = Riff.Chunk.Slot(_io__raw_data_slot, self, self._root)
            self.pad_byte = self._io.read_bytes((self.len % 2))

        class Slot(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                pass



    class ParentChunkData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.form_type = self._io.read_u4le()
            self._raw_subchunks_slot = self._io.read_bytes_full()
            _io__raw_subchunks_slot = KaitaiStream(BytesIO(self._raw_subchunks_slot))
            self.subchunks_slot = Riff.ParentChunkData.Slot(_io__raw_subchunks_slot, self, self._root)

        class Slot(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                pass



    class InfoSubchunk(KaitaiStruct):
        """All registered subchunks in the INFO chunk are NULL-terminated strings,
        but the unregistered might not be. By convention, the registered
        chunk IDs are in uppercase and the unregistered IDs are in lowercase.
        
        If the chunk ID of an INFO subchunk contains a lowercase
        letter, this chunk is considered as unregistered and thus we can make
        no assumptions about the type of data.
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            if self.chunk_ofs < 0:
                self.save_chunk_ofs = self._io.read_bytes(0)

            self.chunk = Riff.Chunk(self._io, self, self._root)

        @property
        def chunk_data(self):
            if hasattr(self, '_m_chunk_data'):
                return self._m_chunk_data if hasattr(self, '_m_chunk_data') else None

            io = self.chunk.data_slot._io
            _pos = io.pos()
            io.seek(0)
            _on = self.is_unregistered_tag
            if _on == False:
                self._m_chunk_data = (io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            io.seek(_pos)
            return self._m_chunk_data if hasattr(self, '_m_chunk_data') else None

        @property
        def is_unregistered_tag(self):
            """Check if chunk_id contains lowercase characters ([a-z], ASCII 97 = a, ASCII 122 = z).
            """
            if hasattr(self, '_m_is_unregistered_tag'):
                return self._m_is_unregistered_tag if hasattr(self, '_m_is_unregistered_tag') else None

            self._m_is_unregistered_tag =  (( ((KaitaiStream.byte_array_index(self.id_chars, 0) >= 97) and (KaitaiStream.byte_array_index(self.id_chars, 0) <= 122)) ) or ( ((KaitaiStream.byte_array_index(self.id_chars, 1) >= 97) and (KaitaiStream.byte_array_index(self.id_chars, 1) <= 122)) ) or ( ((KaitaiStream.byte_array_index(self.id_chars, 2) >= 97) and (KaitaiStream.byte_array_index(self.id_chars, 2) <= 122)) ) or ( ((KaitaiStream.byte_array_index(self.id_chars, 3) >= 97) and (KaitaiStream.byte_array_index(self.id_chars, 3) <= 122)) )) 
            return self._m_is_unregistered_tag if hasattr(self, '_m_is_unregistered_tag') else None

        @property
        def id_chars(self):
            if hasattr(self, '_m_id_chars'):
                return self._m_id_chars if hasattr(self, '_m_id_chars') else None

            _pos = self._io.pos()
            self._io.seek(self.chunk_ofs)
            self._m_id_chars = self._io.read_bytes(4)
            self._io.seek(_pos)
            return self._m_id_chars if hasattr(self, '_m_id_chars') else None

        @property
        def chunk_id_readable(self):
            if hasattr(self, '_m_chunk_id_readable'):
                return self._m_chunk_id_readable if hasattr(self, '_m_chunk_id_readable') else None

            self._m_chunk_id_readable = (self.id_chars).decode(u"ASCII")
            return self._m_chunk_id_readable if hasattr(self, '_m_chunk_id_readable') else None

        @property
        def chunk_ofs(self):
            if hasattr(self, '_m_chunk_ofs'):
                return self._m_chunk_ofs if hasattr(self, '_m_chunk_ofs') else None

            self._m_chunk_ofs = self._io.pos()
            return self._m_chunk_ofs if hasattr(self, '_m_chunk_ofs') else None


    class ChunkType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            if self.chunk_ofs < 0:
                self.save_chunk_ofs = self._io.read_bytes(0)

            self.chunk = Riff.Chunk(self._io, self, self._root)

        @property
        def chunk_ofs(self):
            if hasattr(self, '_m_chunk_ofs'):
                return self._m_chunk_ofs if hasattr(self, '_m_chunk_ofs') else None

            self._m_chunk_ofs = self._io.pos()
            return self._m_chunk_ofs if hasattr(self, '_m_chunk_ofs') else None

        @property
        def chunk_id(self):
            if hasattr(self, '_m_chunk_id'):
                return self._m_chunk_id if hasattr(self, '_m_chunk_id') else None

            self._m_chunk_id = KaitaiStream.resolve_enum(Riff.Fourcc, self.chunk.id)
            return self._m_chunk_id if hasattr(self, '_m_chunk_id') else None

        @property
        def chunk_id_readable(self):
            if hasattr(self, '_m_chunk_id_readable'):
                return self._m_chunk_id_readable if hasattr(self, '_m_chunk_id_readable') else None

            _pos = self._io.pos()
            self._io.seek(self.chunk_ofs)
            self._m_chunk_id_readable = (self._io.read_bytes(4)).decode(u"ASCII")
            self._io.seek(_pos)
            return self._m_chunk_id_readable if hasattr(self, '_m_chunk_id_readable') else None

        @property
        def chunk_data(self):
            if hasattr(self, '_m_chunk_data'):
                return self._m_chunk_data if hasattr(self, '_m_chunk_data') else None

            io = self.chunk.data_slot._io
            _pos = io.pos()
            io.seek(0)
            _on = self.chunk_id
            if _on == Riff.Fourcc.list:
                self._m_chunk_data = Riff.ListChunkData(io, self, self._root)
            io.seek(_pos)
            return self._m_chunk_data if hasattr(self, '_m_chunk_data') else None


    @property
    def chunk_id(self):
        if hasattr(self, '_m_chunk_id'):
            return self._m_chunk_id if hasattr(self, '_m_chunk_id') else None

        self._m_chunk_id = KaitaiStream.resolve_enum(Riff.Fourcc, self.chunk.id)
        return self._m_chunk_id if hasattr(self, '_m_chunk_id') else None

    @property
    def is_riff_chunk(self):
        if hasattr(self, '_m_is_riff_chunk'):
            return self._m_is_riff_chunk if hasattr(self, '_m_is_riff_chunk') else None

        self._m_is_riff_chunk = self.chunk_id == Riff.Fourcc.riff
        return self._m_is_riff_chunk if hasattr(self, '_m_is_riff_chunk') else None

    @property
    def parent_chunk_data(self):
        if hasattr(self, '_m_parent_chunk_data'):
            return self._m_parent_chunk_data if hasattr(self, '_m_parent_chunk_data') else None

        if self.is_riff_chunk:
            io = self.chunk.data_slot._io
            _pos = io.pos()
            io.seek(0)
            self._m_parent_chunk_data = Riff.ParentChunkData(io, self, self._root)
            io.seek(_pos)

        return self._m_parent_chunk_data if hasattr(self, '_m_parent_chunk_data') else None

    @property
    def subchunks(self):
        if hasattr(self, '_m_subchunks'):
            return self._m_subchunks if hasattr(self, '_m_subchunks') else None

        if self.is_riff_chunk:
            io = self.parent_chunk_data.subchunks_slot._io
            _pos = io.pos()
            io.seek(0)
            self._m_subchunks = []
            i = 0
            while not io.is_eof():
                self._m_subchunks.append(Riff.ChunkType(io, self, self._root))
                i += 1

            io.seek(_pos)

        return self._m_subchunks if hasattr(self, '_m_subchunks') else None


