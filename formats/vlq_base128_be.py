# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class VlqBase128Be(KaitaiStruct):
    """A variable-length unsigned integer using base128 encoding. 1-byte groups
    consist of 1-bit flag of continuation and 7-bit value chunk, and are ordered
    "most significant group first", i.e. in "big-endian" manner.
    
    This particular encoding is specified and used in:
    
    * Standard MIDI file format
    * ASN.1 BER encoding
    * RAR 5.0 file format
    
    More information on this encoding is available at
    <https://en.wikipedia.org/wiki/Variable-length_quantity>
    
    This particular implementation supports serialized values to up 8 bytes long.
    """
    SEQ_FIELDS = ["groups"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['groups']['start'] = self._io.pos()
        self.groups = []
        i = 0
        while True:
            if not 'arr' in self._debug['groups']:
                self._debug['groups']['arr'] = []
            self._debug['groups']['arr'].append({'start': self._io.pos()})
            _t_groups = VlqBase128Be.Group(self._io, self, self._root)
            _t_groups._read()
            _ = _t_groups
            self.groups.append(_)
            self._debug['groups']['arr'][len(self.groups) - 1]['end'] = self._io.pos()
            if not (_.has_next):
                break
            i += 1
        self._debug['groups']['end'] = self._io.pos()

    class Group(KaitaiStruct):
        """One byte group, clearly divided into 7-bit "value" chunk and 1-bit "continuation" flag.
        """
        SEQ_FIELDS = ["has_next", "value"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)

        def _read(self):
            self._debug['has_next']['start'] = self._io.pos()
            self.has_next = self._io.read_bits_int_be(1) != 0
            self._debug['has_next']['end'] = self._io.pos()
            self._debug['value']['start'] = self._io.pos()
            self.value = self._io.read_bits_int_be(7)
            self._debug['value']['end'] = self._io.pos()


    @property
    def last(self):
        if hasattr(self, '_m_last'):
            return self._m_last

        self._m_last = (len(self.groups) - 1)
        return getattr(self, '_m_last', None)

    @property
    def value(self):
        """Resulting value as normal integer."""
        if hasattr(self, '_m_value'):
            return self._m_value

        self._m_value = (((((((self.groups[self.last].value + ((self.groups[(self.last - 1)].value << 7) if self.last >= 1 else 0)) + ((self.groups[(self.last - 2)].value << 14) if self.last >= 2 else 0)) + ((self.groups[(self.last - 3)].value << 21) if self.last >= 3 else 0)) + ((self.groups[(self.last - 4)].value << 28) if self.last >= 4 else 0)) + ((self.groups[(self.last - 5)].value << 35) if self.last >= 5 else 0)) + ((self.groups[(self.last - 6)].value << 42) if self.last >= 6 else 0)) + ((self.groups[(self.last - 7)].value << 49) if self.last >= 7 else 0))
        return getattr(self, '_m_value', None)


