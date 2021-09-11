# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Bson(KaitaiStruct):
    """BSON, short for Binary JSON, is a binary-encoded serialization of JSON-like documents. Like JSON, BSON supports the embedding of documents and arrays within other documents and arrays. BSON also contains extensions that allow representation of data types that are not part of the JSON spec. For example, BSON has a Date type and a BinData type. BSON can be compared to binary interchange formats, like Protocol Buffers. BSON is more "schemaless" than Protocol Buffers, which can give it an advantage in flexibility but also a slight disadvantage in space efficiency (BSON has overhead for field names within the serialized data). BSON was designed to have the following three characteristics:
      * Lightweight. Keeping spatial overhead to a minimum is important for any data representation format, especially when used over the network.
      * Traversable. BSON is designed to be traversed easily. This is a vital property in its role as the primary data representation for MongoDB.
      * Efficient. Encoding data to BSON and decoding from BSON can be performed very quickly in most languages due to the use of C data types.
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.len = self._io.read_s4le()
        self._raw_fields = self._io.read_bytes((self.len - 5))
        _io__raw_fields = KaitaiStream(BytesIO(self._raw_fields))
        self.fields = Bson.ElementsList(_io__raw_fields, self, self._root)
        self.terminator = self._io.read_bytes(1)
        if not self.terminator == b"\x00":
            raise kaitaistruct.ValidationNotEqualError(b"\x00", self.terminator, self._io, u"/seq/2")

    class Timestamp(KaitaiStruct):
        """Special internal type used by MongoDB replication and sharding. First 4 bytes are an increment, second 4 are a timestamp."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.increment = self._io.read_u4le()
            self.timestamp = self._io.read_u4le()


    class BinData(KaitaiStruct):
        """The BSON "binary" or "BinData" datatype is used to represent arrays of bytes. It is somewhat analogous to the Java notion of a ByteArray. BSON binary values have a subtype. This is used to indicate what kind of data is in the byte array. Subtypes from zero to 127 are predefined or reserved. Subtypes from 128-255 are user-defined."""

        class Subtype(Enum):
            generic = 0
            function = 1
            byte_array_deprecated = 2
            uuid_deprecated = 3
            uuid = 4
            md5 = 5
            custom = 128
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len = self._io.read_s4le()
            self.subtype = KaitaiStream.resolve_enum(Bson.BinData.Subtype, self._io.read_u1())
            _on = self.subtype
            if _on == Bson.BinData.Subtype.byte_array_deprecated:
                self._raw_content = self._io.read_bytes(self.len)
                _io__raw_content = KaitaiStream(BytesIO(self._raw_content))
                self.content = Bson.BinData.ByteArrayDeprecated(_io__raw_content, self, self._root)
            else:
                self.content = self._io.read_bytes(self.len)

        class ByteArrayDeprecated(KaitaiStruct):
            """The BSON "binary" or "BinData" datatype is used to represent arrays of bytes. It is somewhat analogous to the Java notion of a ByteArray. BSON binary values have a subtype. This is used to indicate what kind of data is in the byte array. Subtypes from zero to 127 are predefined or reserved. Subtypes from 128-255 are user-defined."""
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.len = self._io.read_s4le()
                self.content = self._io.read_bytes(self.len)



    class ElementsList(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.elements = []
            i = 0
            while not self._io.is_eof():
                self.elements.append(Bson.Element(self._io, self, self._root))
                i += 1



    class Cstring(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.str = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")


    class String(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len = self._io.read_s4le()
            self.str = (self._io.read_bytes((self.len - 1))).decode(u"UTF-8")
            self.terminator = self._io.read_bytes(1)
            if not self.terminator == b"\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00", self.terminator, self._io, u"/types/string/seq/2")


    class Element(KaitaiStruct):

        class BsonType(Enum):
            min_key = -1
            end_of_object = 0
            number_double = 1
            string = 2
            document = 3
            array = 4
            bin_data = 5
            undefined = 6
            object_id = 7
            boolean = 8
            utc_datetime = 9
            jst_null = 10
            reg_ex = 11
            db_pointer = 12
            javascript = 13
            symbol = 14
            code_with_scope = 15
            number_int = 16
            timestamp = 17
            number_long = 18
            number_decimal = 19
            max_key = 127
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.type_byte = KaitaiStream.resolve_enum(Bson.Element.BsonType, self._io.read_u1())
            self.name = Bson.Cstring(self._io, self, self._root)
            _on = self.type_byte
            if _on == Bson.Element.BsonType.code_with_scope:
                self.content = Bson.CodeWithScope(self._io, self, self._root)
            elif _on == Bson.Element.BsonType.reg_ex:
                self.content = Bson.RegEx(self._io, self, self._root)
            elif _on == Bson.Element.BsonType.number_double:
                self.content = self._io.read_f8le()
            elif _on == Bson.Element.BsonType.symbol:
                self.content = Bson.String(self._io, self, self._root)
            elif _on == Bson.Element.BsonType.timestamp:
                self.content = Bson.Timestamp(self._io, self, self._root)
            elif _on == Bson.Element.BsonType.number_int:
                self.content = self._io.read_s4le()
            elif _on == Bson.Element.BsonType.document:
                self.content = Bson(self._io)
            elif _on == Bson.Element.BsonType.object_id:
                self.content = Bson.ObjectId(self._io, self, self._root)
            elif _on == Bson.Element.BsonType.javascript:
                self.content = Bson.String(self._io, self, self._root)
            elif _on == Bson.Element.BsonType.utc_datetime:
                self.content = self._io.read_s8le()
            elif _on == Bson.Element.BsonType.boolean:
                self.content = self._io.read_u1()
            elif _on == Bson.Element.BsonType.number_long:
                self.content = self._io.read_s8le()
            elif _on == Bson.Element.BsonType.bin_data:
                self.content = Bson.BinData(self._io, self, self._root)
            elif _on == Bson.Element.BsonType.string:
                self.content = Bson.String(self._io, self, self._root)
            elif _on == Bson.Element.BsonType.db_pointer:
                self.content = Bson.DbPointer(self._io, self, self._root)
            elif _on == Bson.Element.BsonType.array:
                self.content = Bson(self._io)
            elif _on == Bson.Element.BsonType.number_decimal:
                self.content = Bson.F16(self._io, self, self._root)


    class DbPointer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.namespace = Bson.String(self._io, self, self._root)
            self.id = Bson.ObjectId(self._io, self, self._root)


    class U3(KaitaiStruct):
        """Implements unsigned 24-bit (3 byte) integer.
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.b1 = self._io.read_u1()
            self.b2 = self._io.read_u1()
            self.b3 = self._io.read_u1()

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value if hasattr(self, '_m_value') else None

            self._m_value = ((self.b1 | (self.b2 << 8)) | (self.b3 << 16))
            return self._m_value if hasattr(self, '_m_value') else None


    class CodeWithScope(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.id = self._io.read_s4le()
            self.source = Bson.String(self._io, self, self._root)
            self.scope = Bson(self._io)


    class F16(KaitaiStruct):
        """128-bit IEEE 754-2008 decimal floating point."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.str = self._io.read_bits_int_be(1) != 0
            self.exponent = self._io.read_bits_int_be(15)
            self.significand_hi = self._io.read_bits_int_be(49)
            self._io.align_to_byte()
            self.significand_lo = self._io.read_u8le()


    class ObjectId(KaitaiStruct):
        """https://docs.mongodb.com/manual/reference/method/ObjectId/."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.epoch_time = self._io.read_u4le()
            self.machine_id = Bson.U3(self._io, self, self._root)
            self.process_id = self._io.read_u2le()
            self.counter = Bson.U3(self._io, self, self._root)


    class RegEx(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.pattern = Bson.Cstring(self._io, self, self._root)
            self.options = Bson.Cstring(self._io, self, self._root)



