# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

from . import bytes_with_io
class CompressedResource(KaitaiStruct):
    """Compressed Macintosh resource data,
    as stored in resources with the "compressed" attribute.
    
    Resource decompression is not documented by Apple.
    It is mostly used internally in System 7,
    some of Apple's own applications (such as ResEdit),
    and also by some third-party applications.
    Later versions of Classic Mac OS make less use of resource compression,
    but still support it fully for backwards compatibility.
    Carbon in Mac OS X no longer supports resource compression in any way.
    
    The data of all compressed resources starts with a common header,
    followed by the compressed data.
    The data is decompressed using code in a `'dcmp'` resource.
    Some decompressors used by Apple are included in the System file,
    but applications can also include custom decompressors.
    The header of the compressed data indicates the ID of the `'dcmp'` resource used to decompress the data,
    along with some parameters for the decompressor.
    
    .. seealso::
       Source - http://www.alysis.us/arctechnology.htm
    
    
    .. seealso::
       Source - http://preserve.mactech.com/articles/mactech/Vol.09/09.01/ResCompression/index.html
    
    
    .. seealso::
       Source - https://github.com/dgelessus/python-rsrcfork/tree/master/rsrcfork/compress
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.header = CompressedResource.Header(self._io, self, self._root)
        self.compressed_data = self._io.read_bytes_full()

    class Header(KaitaiStruct):
        """Compressed resource data header,
        as stored at the start of all compressed resources.
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.common_part = CompressedResource.Header.CommonPart(self._io, self, self._root)
            self._raw_type_specific_part_raw_with_io = self._io.read_bytes((self.common_part.len_header - 12))
            _io__raw_type_specific_part_raw_with_io = KaitaiStream(BytesIO(self._raw_type_specific_part_raw_with_io))
            self.type_specific_part_raw_with_io = bytes_with_io.BytesWithIo(_io__raw_type_specific_part_raw_with_io)

        class CommonPart(KaitaiStruct):
            """The common part of a compressed resource data header.
            The format of this part is the same for all compressed resources.
            """
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.magic = self._io.read_bytes(4)
                if not self.magic == b"\xA8\x9F\x65\x72":
                    raise kaitaistruct.ValidationNotEqualError(b"\xA8\x9F\x65\x72", self.magic, self._io, u"/types/header/types/common_part/seq/0")
                self.len_header = self._io.read_u2be()
                if not self.len_header == 18:
                    raise kaitaistruct.ValidationNotEqualError(18, self.len_header, self._io, u"/types/header/types/common_part/seq/1")
                self.header_type = self._io.read_u1()
                self.unknown = self._io.read_u1()
                if not self.unknown == 1:
                    raise kaitaistruct.ValidationNotEqualError(1, self.unknown, self._io, u"/types/header/types/common_part/seq/3")
                self.len_decompressed = self._io.read_u4be()


        class TypeSpecificPartType8(KaitaiStruct):
            """The type-specific part of a compressed resource header with header type `8`.
            """
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.working_buffer_fractional_size = self._io.read_u1()
                self.expansion_buffer_size = self._io.read_u1()
                self.decompressor_id = self._io.read_s2be()
                self.reserved = self._io.read_u2be()
                if not self.reserved == 0:
                    raise kaitaistruct.ValidationNotEqualError(0, self.reserved, self._io, u"/types/header/types/type_specific_part_type_8/seq/3")


        class TypeSpecificPartType9(KaitaiStruct):
            """The type-specific part of a compressed resource header with header type `9`.
            """
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.decompressor_id = self._io.read_s2be()
                self._raw_decompressor_specific_parameters_with_io = self._io.read_bytes(4)
                _io__raw_decompressor_specific_parameters_with_io = KaitaiStream(BytesIO(self._raw_decompressor_specific_parameters_with_io))
                self.decompressor_specific_parameters_with_io = bytes_with_io.BytesWithIo(_io__raw_decompressor_specific_parameters_with_io)

            @property
            def decompressor_specific_parameters(self):
                """Decompressor-specific parameters.
                The exact structure and meaning of this field is different for each decompressor.
                
                This field always has the same length,
                but decompressors don't always use the entirety of the field,
                so depending on the decompressor some parts of this field may be meaningless.
                """
                if hasattr(self, '_m_decompressor_specific_parameters'):
                    return self._m_decompressor_specific_parameters if hasattr(self, '_m_decompressor_specific_parameters') else None

                self._m_decompressor_specific_parameters = self.decompressor_specific_parameters_with_io.data
                return self._m_decompressor_specific_parameters if hasattr(self, '_m_decompressor_specific_parameters') else None


        @property
        def type_specific_part_raw(self):
            """The type-specific part of the header,
            as a raw byte array.
            """
            if hasattr(self, '_m_type_specific_part_raw'):
                return self._m_type_specific_part_raw if hasattr(self, '_m_type_specific_part_raw') else None

            self._m_type_specific_part_raw = self.type_specific_part_raw_with_io.data
            return self._m_type_specific_part_raw if hasattr(self, '_m_type_specific_part_raw') else None

        @property
        def type_specific_part(self):
            """The type-specific part of the header,
            parsed according to the type from the common part.
            """
            if hasattr(self, '_m_type_specific_part'):
                return self._m_type_specific_part if hasattr(self, '_m_type_specific_part') else None

            io = self.type_specific_part_raw_with_io._io
            _pos = io.pos()
            io.seek(0)
            _on = self.common_part.header_type
            if _on == 8:
                self._m_type_specific_part = CompressedResource.Header.TypeSpecificPartType8(io, self, self._root)
            elif _on == 9:
                self._m_type_specific_part = CompressedResource.Header.TypeSpecificPartType9(io, self, self._root)
            io.seek(_pos)
            return self._m_type_specific_part if hasattr(self, '_m_type_specific_part') else None



