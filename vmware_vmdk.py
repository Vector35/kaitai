# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class VmwareVmdk(KaitaiStruct):
    """
    .. seealso::
       Source - https://github.com/libyal/libvmdk/blob/master/documentation/VMWare%20Virtual%20Disk%20Format%20(VMDK).asciidoc#41-file-header
    """

    class CompressionMethods(Enum):
        none = 0
        deflate = 1
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(4)
        if not self.magic == b"\x4B\x44\x4D\x56":
            raise kaitaistruct.ValidationNotEqualError(b"\x4B\x44\x4D\x56", self.magic, self._io, u"/seq/0")
        self.version = self._io.read_s4le()
        self.flags = VmwareVmdk.HeaderFlags(self._io, self, self._root)
        self.size_max = self._io.read_s8le()
        self.size_grain = self._io.read_s8le()
        self.start_descriptor = self._io.read_s8le()
        self.size_descriptor = self._io.read_s8le()
        self.num_grain_table_entries = self._io.read_s4le()
        self.start_secondary_grain = self._io.read_s8le()
        self.start_primary_grain = self._io.read_s8le()
        self.size_metadata = self._io.read_s8le()
        self.is_dirty = self._io.read_u1()
        self.stuff = self._io.read_bytes(4)
        self.compression_method = KaitaiStream.resolve_enum(VmwareVmdk.CompressionMethods, self._io.read_u2le())

    class HeaderFlags(KaitaiStruct):
        """
        .. seealso::
           Source - https://github.com/libyal/libvmdk/blob/master/documentation/VMWare%20Virtual%20Disk%20Format%20(VMDK).asciidoc#411-flags
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.reserved1 = self._io.read_bits_int_be(5)
            self.zeroed_grain_table_entry = self._io.read_bits_int_be(1) != 0
            self.use_secondary_grain_dir = self._io.read_bits_int_be(1) != 0
            self.valid_new_line_detection_test = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.reserved2 = self._io.read_u1()
            self.reserved3 = self._io.read_bits_int_be(6)
            self.has_metadata = self._io.read_bits_int_be(1) != 0
            self.has_compressed_grain = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.reserved4 = self._io.read_u1()


    @property
    def len_sector(self):
        if hasattr(self, '_m_len_sector'):
            return self._m_len_sector if hasattr(self, '_m_len_sector') else None

        self._m_len_sector = 512
        return self._m_len_sector if hasattr(self, '_m_len_sector') else None

    @property
    def descriptor(self):
        if hasattr(self, '_m_descriptor'):
            return self._m_descriptor if hasattr(self, '_m_descriptor') else None

        _pos = self._io.pos()
        self._io.seek((self.start_descriptor * self._root.len_sector))
        self._m_descriptor = self._io.read_bytes((self.size_descriptor * self._root.len_sector))
        self._io.seek(_pos)
        return self._m_descriptor if hasattr(self, '_m_descriptor') else None

    @property
    def grain_primary(self):
        if hasattr(self, '_m_grain_primary'):
            return self._m_grain_primary if hasattr(self, '_m_grain_primary') else None

        _pos = self._io.pos()
        self._io.seek((self.start_primary_grain * self._root.len_sector))
        self._m_grain_primary = self._io.read_bytes((self.size_grain * self._root.len_sector))
        self._io.seek(_pos)
        return self._m_grain_primary if hasattr(self, '_m_grain_primary') else None

    @property
    def grain_secondary(self):
        if hasattr(self, '_m_grain_secondary'):
            return self._m_grain_secondary if hasattr(self, '_m_grain_secondary') else None

        _pos = self._io.pos()
        self._io.seek((self.start_secondary_grain * self._root.len_sector))
        self._m_grain_secondary = self._io.read_bytes((self.size_grain * self._root.len_sector))
        self._io.seek(_pos)
        return self._m_grain_secondary if hasattr(self, '_m_grain_secondary') else None


