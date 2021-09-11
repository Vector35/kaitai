# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Id3v24(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.tag = Id3v24.Tag(self._io, self, self._root)

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
            self.byte0 = Id3v24.U1beSynchsafe(self._io, self, self._root)
            self.byte1 = Id3v24.U1beSynchsafe(self._io, self, self._root)

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
            self.header = Id3v24.Header(self._io, self, self._root)
            if self.header.flags.flag_headerex:
                self.header_ex = Id3v24.HeaderEx(self._io, self, self._root)

            self.frames = []
            i = 0
            while True:
                _ = Id3v24.Frame(self._io, self, self._root)
                self.frames.append(_)
                if  (((self._io.pos() + _.size.value) > self.header.size.value) or (_.is_invalid)) :
                    break
                i += 1
            if not (self.header.flags.flag_footer):
                self.padding = Id3v24.Padding(self._io, self, self._root)

            if self.header.flags.flag_footer:
                self.footer = Id3v24.Footer(self._io, self, self._root)



    class U4beSynchsafe(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.short0 = Id3v24.U2beSynchsafe(self._io, self, self._root)
            self.short1 = Id3v24.U2beSynchsafe(self._io, self, self._root)

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
            self.size = Id3v24.U4beSynchsafe(self._io, self, self._root)
            self.flags_status = Id3v24.Frame.FlagsStatus(self._io, self, self._root)
            self.flags_format = Id3v24.Frame.FlagsFormat(self._io, self, self._root)
            self.data = self._io.read_bytes(self.size.value)

        class FlagsStatus(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.reserved1 = self._io.read_bits_int_be(1) != 0
                self.flag_discard_alter_tag = self._io.read_bits_int_be(1) != 0
                self.flag_discard_alter_file = self._io.read_bits_int_be(1) != 0
                self.flag_read_only = self._io.read_bits_int_be(1) != 0
                self.reserved2 = self._io.read_bits_int_be(4)


        class FlagsFormat(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.reserved1 = self._io.read_bits_int_be(1) != 0
                self.flag_grouping = self._io.read_bits_int_be(1) != 0
                self.reserved2 = self._io.read_bits_int_be(2)
                self.flag_compressed = self._io.read_bits_int_be(1) != 0
                self.flag_encrypted = self._io.read_bits_int_be(1) != 0
                self.flag_unsynchronisated = self._io.read_bits_int_be(1) != 0
                self.flag_indicator = self._io.read_bits_int_be(1) != 0


        @property
        def is_invalid(self):
            if hasattr(self, '_m_is_invalid'):
                return self._m_is_invalid if hasattr(self, '_m_is_invalid') else None

            self._m_is_invalid = self.id == u"\000\000\000\000"
            return self._m_is_invalid if hasattr(self, '_m_is_invalid') else None


    class HeaderEx(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.size = Id3v24.U4beSynchsafe(self._io, self, self._root)
            self.flags_ex = Id3v24.HeaderEx.FlagsEx(self._io, self, self._root)
            self.data = self._io.read_bytes((self.size.value - 5))

        class FlagsEx(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.reserved1 = self._io.read_bits_int_be(1) != 0
                self.flag_update = self._io.read_bits_int_be(1) != 0
                self.flag_crc = self._io.read_bits_int_be(1) != 0
                self.flag_restrictions = self._io.read_bits_int_be(1) != 0
                self.reserved2 = self._io.read_bits_int_be(4)



    class Header(KaitaiStruct):
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
            self.flags = Id3v24.Header.Flags(self._io, self, self._root)
            self.size = Id3v24.U4beSynchsafe(self._io, self, self._root)

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
                self.flag_footer = self._io.read_bits_int_be(1) != 0
                self.reserved = self._io.read_bits_int_be(4)



    class Padding(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.padding = self._io.read_bytes((self._root.tag.header.size.value - self._io.pos()))


    class Footer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(3)
            if not self.magic == b"\x33\x44\x49":
                raise kaitaistruct.ValidationNotEqualError(b"\x33\x44\x49", self.magic, self._io, u"/types/footer/seq/0")
            self.version_major = self._io.read_u1()
            self.version_revision = self._io.read_u1()
            self.flags = Id3v24.Footer.Flags(self._io, self, self._root)
            self.size = Id3v24.U4beSynchsafe(self._io, self, self._root)

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
                self.flag_footer = self._io.read_bits_int_be(1) != 0
                self.reserved = self._io.read_bits_int_be(4)




