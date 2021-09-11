# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Lzh(KaitaiStruct):
    """LHA (LHarc, LZH) is a file format used by a popular freeware
    eponymous archiver, created in 1988 by Haruyasu Yoshizaki. Over the
    years, many ports and implementations were developed, sporting many
    extensions to original 1988 LZH.
    
    File format is pretty simple and essentially consists of a stream of
    records.
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.entries = []
        i = 0
        while not self._io.is_eof():
            self.entries.append(Lzh.Record(self._io, self, self._root))
            i += 1


    class Record(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.header_len = self._io.read_u1()
            if self.header_len > 0:
                self.file_record = Lzh.FileRecord(self._io, self, self._root)



    class FileRecord(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw_header = self._io.read_bytes((self._parent.header_len - 1))
            _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
            self.header = Lzh.Header(_io__raw_header, self, self._root)
            if self.header.header1.lha_level == 0:
                self.file_uncompr_crc16 = self._io.read_u2le()

            self.body = self._io.read_bytes(self.header.header1.file_size_compr)


    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.header1 = Lzh.Header1(self._io, self, self._root)
            if self.header1.lha_level == 0:
                self.filename_len = self._io.read_u1()

            if self.header1.lha_level == 0:
                self.filename = (self._io.read_bytes(self.filename_len)).decode(u"ASCII")

            if self.header1.lha_level == 2:
                self.file_uncompr_crc16 = self._io.read_u2le()

            if self.header1.lha_level == 2:
                self.os = self._io.read_u1()

            if self.header1.lha_level == 2:
                self.ext_header_size = self._io.read_u2le()



    class Header1(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.header_checksum = self._io.read_u1()
            self.method_id = (self._io.read_bytes(5)).decode(u"ASCII")
            self.file_size_compr = self._io.read_u4le()
            self.file_size_uncompr = self._io.read_u4le()
            self.file_timestamp = self._io.read_u4le()
            self.attr = self._io.read_u1()
            self.lha_level = self._io.read_u1()



