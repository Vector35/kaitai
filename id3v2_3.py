# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Id3v23(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.tag = Id3v23.Tag(self._io, self, self._root)

    class U1beSynchsafe(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.padding = self._io.read_bits_int_be(1) != 0
            self.value = self._io.read_bits_int_be(7)


    class U2beSynchsafe(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.byte0 = Id3v23.U1beSynchsafe(self._io, self, self._root)
            self.byte1 = Id3v23.U1beSynchsafe(self._io, self, self._root)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value if hasattr(self, '_m_value') else None

            self._m_value = ((self.byte0.value << 7) | self.byte1.value)
            return self._m_value if hasattr(self, '_m_value') else None


    class Tag(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.header = Id3v23.Header(self._io, self, self._root)
            if self.header.flags.flag_headerex:
                self.header_ex = Id3v23.HeaderEx(self._io, self, self._root)

            self.frames = []
            i = 0
            while True:
                _ = Id3v23.Frame(self._io, self, self._root)
                self.frames.append(_)
                if  (((self._io.pos() + _.size) > self.header.size.value) or (_.is_invalid)) :
                    break
                i += 1
            if self.header.flags.flag_headerex:
                self.padding = self._io.read_bytes((self.header_ex.padding_size - self._io.pos()))



    class U4beSynchsafe(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.short0 = Id3v23.U2beSynchsafe(self._io, self, self._root)
            self.short1 = Id3v23.U2beSynchsafe(self._io, self, self._root)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value if hasattr(self, '_m_value') else None

            self._m_value = ((self.short0.value << 14) | self.short1.value)
            return self._m_value if hasattr(self, '_m_value') else None


    class Frame(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.id = (self._io.read_bytes(4)).decode(u"ASCII")
            self.size = self._io.read_u4be()
            self.flags = Id3v23.Frame.Flags(self._io, self, self._root)
            self.data = self._io.read_bytes(self.size)

        class Flags(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.flag_discard_alter_tag = self._io.read_bits_int_be(1) != 0
                self.flag_discard_alter_file = self._io.read_bits_int_be(1) != 0
                self.flag_read_only = self._io.read_bits_int_be(1) != 0
                self.reserved1 = self._io.read_bits_int_be(5)
                self.flag_compressed = self._io.read_bits_int_be(1) != 0
                self.flag_encrypted = self._io.read_bits_int_be(1) != 0
                self.flag_grouping = self._io.read_bits_int_be(1) != 0
                self.reserved2 = self._io.read_bits_int_be(5)


        @property
        def is_invalid(self):
            if hasattr(self, '_m_is_invalid'):
                return self._m_is_invalid if hasattr(self, '_m_is_invalid') else None

            self._m_is_invalid = self.id == u"\000\000\000\000"
            return self._m_is_invalid if hasattr(self, '_m_is_invalid') else None


    class HeaderEx(KaitaiStruct):
        """ID3v2 extended header.
        
        .. seealso::
           Section 3.2. ID3v2 extended header
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.size = self._io.read_u4be()
            self.flags_ex = Id3v23.HeaderEx.FlagsEx(self._io, self, self._root)
            self.padding_size = self._io.read_u4be()
            if self.flags_ex.flag_crc:
                self.crc = self._io.read_u4be()


        class FlagsEx(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.flag_crc = self._io.read_bits_int_be(1) != 0
                self.reserved = self._io.read_bits_int_be(15)



    class Header(KaitaiStruct):
        """ID3v2 fixed header.
        
        .. seealso::
           Section 3.1. ID3v2 header
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(3)
            if not self.magic == b"\x49\x44\x33":
                raise kaitaistruct.ValidationNotEqualError(b"\x49\x44\x33", self.magic, self._io, u"/types/header/seq/0")
            self.version_major = self._io.read_u1()
            self.version_revision = self._io.read_u1()
            self.flags = Id3v23.Header.Flags(self._io, self, self._root)
            self.size = Id3v23.U4beSynchsafe(self._io, self, self._root)

        class Flags(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.flag_unsynchronization = self._io.read_bits_int_be(1) != 0
                self.flag_headerex = self._io.read_bits_int_be(1) != 0
                self.flag_experimental = self._io.read_bits_int_be(1) != 0
                self.reserved = self._io.read_bits_int_be(5)




