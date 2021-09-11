# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class RubyMarshal(KaitaiStruct):
    """Ruby's Marshal module allows serialization and deserialization of
    many standard and arbitrary Ruby objects in a compact binary
    format. It is relatively fast, available in stdlibs standard and
    allows conservation of language-specific properties (such as symbols
    or encoding-aware strings).
    
    Feature-wise, it is comparable to other language-specific
    implementations, such as:
    
    * Java's
      [Serializable](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html)
    * .NET
      [BinaryFormatter](https://docs.microsoft.com/en-us/dotnet/api/system.runtime.serialization.formatters.binary.binaryformatter)
    * Python's
      [marshal](https://docs.python.org/3/library/marshal.html),
      [pickle](https://docs.python.org/3/library/pickle.html) and
      [shelve](https://docs.python.org/3/library/shelve.html)
    
    From internal perspective, serialized stream consists of a simple
    magic header and a record.
    
    .. seealso::
       Source - https://docs.ruby-lang.org/en/2.4.0/marshal_rdoc.html#label-Stream+Format
    """

    class Codes(Enum):
        ruby_string = 34
        const_nil = 48
        ruby_symbol = 58
        ruby_symbol_link = 59
        const_false = 70
        instance_var = 73
        ruby_struct = 83
        const_true = 84
        ruby_array = 91
        packed_int = 105
        bignum = 108
        ruby_hash = 123
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.version = self._io.read_bytes(2)
        if not self.version == b"\x04\x08":
            raise kaitaistruct.ValidationNotEqualError(b"\x04\x08", self.version, self._io, u"/seq/0")
        self.records = RubyMarshal.Record(self._io, self, self._root)

    class RubyArray(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_elements = RubyMarshal.PackedInt(self._io, self, self._root)
            self.elements = [None] * (self.num_elements.value)
            for i in range(self.num_elements.value):
                self.elements[i] = RubyMarshal.Record(self._io, self, self._root)



    class Bignum(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.ruby-lang.org/en/2.4.0/marshal_rdoc.html#label-Bignum
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.sign = self._io.read_u1()
            self.len_div_2 = RubyMarshal.PackedInt(self._io, self, self._root)
            self.body = self._io.read_bytes((self.len_div_2.value * 2))


    class RubyStruct(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.ruby-lang.org/en/2.4.0/marshal_rdoc.html#label-Struct
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = RubyMarshal.Record(self._io, self, self._root)
            self.num_members = RubyMarshal.PackedInt(self._io, self, self._root)
            self.members = [None] * (self.num_members.value)
            for i in range(self.num_members.value):
                self.members[i] = RubyMarshal.Pair(self._io, self, self._root)



    class RubySymbol(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.ruby-lang.org/en/2.4.0/marshal_rdoc.html#label-Symbols+and+Byte+Sequence
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len = RubyMarshal.PackedInt(self._io, self, self._root)
            self.name = (self._io.read_bytes(self.len.value)).decode(u"UTF-8")


    class PackedInt(KaitaiStruct):
        """Ruby uses sophisticated system to pack integers: first `code`
        byte either determines packing scheme or carries encoded
        immediate value (thus allowing smaller values from -123 to 122
        (inclusive) to take only one byte. There are 11 encoding schemes
        in total:
        
        * 0 is encoded specially (as 0)
        * 1..122 are encoded as immediate value with a shift
        * 123..255 are encoded with code of 0x01 and 1 extra byte
        * 0x100..0xffff are encoded with code of 0x02 and 2 extra bytes
        * 0x10000..0xffffff are encoded with code of 0x03 and 3 extra
          bytes
        * 0x1000000..0xffffffff are encoded with code of 0x04 and 4
          extra bytes
        * -123..-1 are encoded as immediate value with another shift
        * -256..-124 are encoded with code of 0xff and 1 extra byte
        * -0x10000..-257 are encoded with code of 0xfe and 2 extra bytes
        * -0x1000000..0x10001 are encoded with code of 0xfd and 3 extra
           bytes
        * -0x40000000..-0x1000001 are encoded with code of 0xfc and 4
           extra bytes
        
        Values beyond that are serialized as bignum (even if they
        technically might be not Bignum class in Ruby implementation,
        i.e. if they fit into 64 bits on a 64-bit platform).
        
        .. seealso::
           Source - https://docs.ruby-lang.org/en/2.4.0/marshal_rdoc.html#label-Fixnum+and+long
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.code = self._io.read_u1()
            _on = self.code
            if _on == 4:
                self.encoded = self._io.read_u4le()
            elif _on == 1:
                self.encoded = self._io.read_u1()
            elif _on == 252:
                self.encoded = self._io.read_u4le()
            elif _on == 253:
                self.encoded = self._io.read_u2le()
            elif _on == 3:
                self.encoded = self._io.read_u2le()
            elif _on == 2:
                self.encoded = self._io.read_u2le()
            elif _on == 255:
                self.encoded = self._io.read_u1()
            elif _on == 254:
                self.encoded = self._io.read_u2le()
            _on = self.code
            if _on == 3:
                self.encoded2 = self._io.read_u1()
            elif _on == 253:
                self.encoded2 = self._io.read_u1()

        @property
        def is_immediate(self):
            if hasattr(self, '_m_is_immediate'):
                return self._m_is_immediate if hasattr(self, '_m_is_immediate') else None

            self._m_is_immediate =  ((self.code > 4) and (self.code < 252)) 
            return self._m_is_immediate if hasattr(self, '_m_is_immediate') else None

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value if hasattr(self, '_m_value') else None

            self._m_value = (((self.code - 5) if self.code < 128 else (4 - (~(self.code) & 127))) if self.is_immediate else (0 if self.code == 0 else ((self.encoded - 256) if self.code == 255 else ((self.encoded - 65536) if self.code == 254 else ((((self.encoded2 << 16) | self.encoded) - 16777216) if self.code == 253 else (((self.encoded2 << 16) | self.encoded) if self.code == 3 else self.encoded))))))
            return self._m_value if hasattr(self, '_m_value') else None


    class Pair(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.key = RubyMarshal.Record(self._io, self, self._root)
            self.value = RubyMarshal.Record(self._io, self, self._root)


    class InstanceVar(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.ruby-lang.org/en/2.4.0/marshal_rdoc.html#label-Instance+Variables
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.obj = RubyMarshal.Record(self._io, self, self._root)
            self.num_vars = RubyMarshal.PackedInt(self._io, self, self._root)
            self.vars = [None] * (self.num_vars.value)
            for i in range(self.num_vars.value):
                self.vars[i] = RubyMarshal.Pair(self._io, self, self._root)



    class Record(KaitaiStruct):
        """Each record starts with a single byte that determines its type
        (`code`) and contents. If necessary, additional info as parsed
        as `body`, to be determined by `code`.
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.code = KaitaiStream.resolve_enum(RubyMarshal.Codes, self._io.read_u1())
            _on = self.code
            if _on == RubyMarshal.Codes.packed_int:
                self.body = RubyMarshal.PackedInt(self._io, self, self._root)
            elif _on == RubyMarshal.Codes.bignum:
                self.body = RubyMarshal.Bignum(self._io, self, self._root)
            elif _on == RubyMarshal.Codes.ruby_array:
                self.body = RubyMarshal.RubyArray(self._io, self, self._root)
            elif _on == RubyMarshal.Codes.ruby_symbol_link:
                self.body = RubyMarshal.PackedInt(self._io, self, self._root)
            elif _on == RubyMarshal.Codes.ruby_struct:
                self.body = RubyMarshal.RubyStruct(self._io, self, self._root)
            elif _on == RubyMarshal.Codes.ruby_string:
                self.body = RubyMarshal.RubyString(self._io, self, self._root)
            elif _on == RubyMarshal.Codes.instance_var:
                self.body = RubyMarshal.InstanceVar(self._io, self, self._root)
            elif _on == RubyMarshal.Codes.ruby_hash:
                self.body = RubyMarshal.RubyHash(self._io, self, self._root)
            elif _on == RubyMarshal.Codes.ruby_symbol:
                self.body = RubyMarshal.RubySymbol(self._io, self, self._root)


    class RubyHash(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.ruby-lang.org/en/2.4.0/marshal_rdoc.html#label-Hash+and+Hash+with+Default+Value
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_pairs = RubyMarshal.PackedInt(self._io, self, self._root)
            self.pairs = [None] * (self.num_pairs.value)
            for i in range(self.num_pairs.value):
                self.pairs[i] = RubyMarshal.Pair(self._io, self, self._root)



    class RubyString(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.ruby-lang.org/en/2.4.0/marshal_rdoc.html#label-String
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len = RubyMarshal.PackedInt(self._io, self, self._root)
            self.body = self._io.read_bytes(self.len.value)



