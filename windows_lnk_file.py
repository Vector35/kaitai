# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

from . import windows_shell_items
class WindowsLnkFile(KaitaiStruct):
    """Windows .lnk files (AKA "shell link" file) are most frequently used
    in Windows shell to create "shortcuts" to another files, usually for
    purposes of running a program from some other directory, sometimes
    with certain preconfigured arguments and some other options.
    
    .. seealso::
       Source - https://winprotocoldoc.blob.core.windows.net/productionwindowsarchives/MS-SHLLINK/[MS-SHLLINK].pdf
    """

    class WindowState(Enum):
        normal = 1
        maximized = 3
        min_no_active = 7

    class DriveTypes(Enum):
        unknown = 0
        no_root_dir = 1
        removable = 2
        fixed = 3
        remote = 4
        cdrom = 5
        ramdisk = 6
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.header = WindowsLnkFile.FileHeader(self._io, self, self._root)
        if self.header.flags.has_link_target_id_list:
            self.target_id_list = WindowsLnkFile.LinkTargetIdList(self._io, self, self._root)

        if self.header.flags.has_link_info:
            self.info = WindowsLnkFile.LinkInfo(self._io, self, self._root)

        if self.header.flags.has_name:
            self.name = WindowsLnkFile.StringData(self._io, self, self._root)

        if self.header.flags.has_rel_path:
            self.rel_path = WindowsLnkFile.StringData(self._io, self, self._root)

        if self.header.flags.has_work_dir:
            self.work_dir = WindowsLnkFile.StringData(self._io, self, self._root)

        if self.header.flags.has_arguments:
            self.arguments = WindowsLnkFile.StringData(self._io, self, self._root)

        if self.header.flags.has_icon_location:
            self.icon_location = WindowsLnkFile.StringData(self._io, self, self._root)


    class LinkTargetIdList(KaitaiStruct):
        """
        .. seealso::
           Section 2.2 - https://winprotocoldoc.blob.core.windows.net/productionwindowsarchives/MS-SHLLINK/[MS-SHLLINK].pdf
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len_id_list = self._io.read_u2le()
            self._raw_id_list = self._io.read_bytes(self.len_id_list)
            _io__raw_id_list = KaitaiStream(BytesIO(self._raw_id_list))
            self.id_list = windows_shell_items.WindowsShellItems(_io__raw_id_list)


    class StringData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.chars_str = self._io.read_u2le()
            self.str = (self._io.read_bytes((self.chars_str * 2))).decode(u"UTF-16LE")


    class LinkInfo(KaitaiStruct):
        """
        .. seealso::
           Section 2.3 - https://winprotocoldoc.blob.core.windows.net/productionwindowsarchives/MS-SHLLINK/[MS-SHLLINK].pdf
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len_all = self._io.read_u4le()
            self._raw_all = self._io.read_bytes((self.len_all - 4))
            _io__raw_all = KaitaiStream(BytesIO(self._raw_all))
            self.all = WindowsLnkFile.LinkInfo.All(_io__raw_all, self, self._root)

        class VolumeIdBody(KaitaiStruct):
            """
            .. seealso::
               Section 2.3.1 - https://winprotocoldoc.blob.core.windows.net/productionwindowsarchives/MS-SHLLINK/[MS-SHLLINK].pdf
            """
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.drive_type = KaitaiStream.resolve_enum(WindowsLnkFile.DriveTypes, self._io.read_u4le())
                self.drive_serial_number = self._io.read_u4le()
                self.ofs_volume_label = self._io.read_u4le()
                if self.is_unicode:
                    self.ofs_volume_label_unicode = self._io.read_u4le()


            @property
            def is_unicode(self):
                if hasattr(self, '_m_is_unicode'):
                    return self._m_is_unicode if hasattr(self, '_m_is_unicode') else None

                self._m_is_unicode = self.ofs_volume_label == 20
                return self._m_is_unicode if hasattr(self, '_m_is_unicode') else None

            @property
            def volume_label_ansi(self):
                if hasattr(self, '_m_volume_label_ansi'):
                    return self._m_volume_label_ansi if hasattr(self, '_m_volume_label_ansi') else None

                if not (self.is_unicode):
                    _pos = self._io.pos()
                    self._io.seek((self.ofs_volume_label - 4))
                    self._m_volume_label_ansi = (self._io.read_bytes_term(0, False, True, True)).decode(u"cp437")
                    self._io.seek(_pos)

                return self._m_volume_label_ansi if hasattr(self, '_m_volume_label_ansi') else None


        class All(KaitaiStruct):
            """
            .. seealso::
               Section 2.3 - https://winprotocoldoc.blob.core.windows.net/productionwindowsarchives/MS-SHLLINK/[MS-SHLLINK].pdf
            """
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.len_header = self._io.read_u4le()
                self._raw_header = self._io.read_bytes((self.len_header - 8))
                _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
                self.header = WindowsLnkFile.LinkInfo.Header(_io__raw_header, self, self._root)

            @property
            def volume_id(self):
                if hasattr(self, '_m_volume_id'):
                    return self._m_volume_id if hasattr(self, '_m_volume_id') else None

                if self.header.flags.has_volume_id_and_local_base_path:
                    _pos = self._io.pos()
                    self._io.seek((self.header.ofs_volume_id - 4))
                    self._m_volume_id = WindowsLnkFile.LinkInfo.VolumeIdSpec(self._io, self, self._root)
                    self._io.seek(_pos)

                return self._m_volume_id if hasattr(self, '_m_volume_id') else None

            @property
            def local_base_path(self):
                if hasattr(self, '_m_local_base_path'):
                    return self._m_local_base_path if hasattr(self, '_m_local_base_path') else None

                if self.header.flags.has_volume_id_and_local_base_path:
                    _pos = self._io.pos()
                    self._io.seek((self.header.ofs_local_base_path - 4))
                    self._m_local_base_path = self._io.read_bytes_term(0, False, True, True)
                    self._io.seek(_pos)

                return self._m_local_base_path if hasattr(self, '_m_local_base_path') else None


        class VolumeIdSpec(KaitaiStruct):
            """
            .. seealso::
               Section 2.3.1 - https://winprotocoldoc.blob.core.windows.net/productionwindowsarchives/MS-SHLLINK/[MS-SHLLINK].pdf
            """
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.len_all = self._io.read_u4le()
                self._raw_body = self._io.read_bytes((self.len_all - 4))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = WindowsLnkFile.LinkInfo.VolumeIdBody(_io__raw_body, self, self._root)


        class LinkInfoFlags(KaitaiStruct):
            """
            .. seealso::
               Section 2.3 - https://winprotocoldoc.blob.core.windows.net/productionwindowsarchives/MS-SHLLINK/[MS-SHLLINK].pdf
            """
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.reserved1 = self._io.read_bits_int_be(6)
                self.has_common_net_rel_link = self._io.read_bits_int_be(1) != 0
                self.has_volume_id_and_local_base_path = self._io.read_bits_int_be(1) != 0
                self.reserved2 = self._io.read_bits_int_be(24)


        class Header(KaitaiStruct):
            """
            .. seealso::
               Section 2.3 - https://winprotocoldoc.blob.core.windows.net/productionwindowsarchives/MS-SHLLINK/[MS-SHLLINK].pdf
            """
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.flags = WindowsLnkFile.LinkInfo.LinkInfoFlags(self._io, self, self._root)
                self.ofs_volume_id = self._io.read_u4le()
                self.ofs_local_base_path = self._io.read_u4le()
                self.ofs_common_net_rel_link = self._io.read_u4le()
                self.ofs_common_path_suffix = self._io.read_u4le()
                if not (self._io.is_eof()):
                    self.ofs_local_base_path_unicode = self._io.read_u4le()

                if not (self._io.is_eof()):
                    self.ofs_common_path_suffix_unicode = self._io.read_u4le()




    class LinkFlags(KaitaiStruct):
        """
        .. seealso::
           Section 2.1.1 - https://winprotocoldoc.blob.core.windows.net/productionwindowsarchives/MS-SHLLINK/[MS-SHLLINK].pdf
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.is_unicode = self._io.read_bits_int_be(1) != 0
            self.has_icon_location = self._io.read_bits_int_be(1) != 0
            self.has_arguments = self._io.read_bits_int_be(1) != 0
            self.has_work_dir = self._io.read_bits_int_be(1) != 0
            self.has_rel_path = self._io.read_bits_int_be(1) != 0
            self.has_name = self._io.read_bits_int_be(1) != 0
            self.has_link_info = self._io.read_bits_int_be(1) != 0
            self.has_link_target_id_list = self._io.read_bits_int_be(1) != 0
            self._unnamed8 = self._io.read_bits_int_be(16)
            self.reserved = self._io.read_bits_int_be(5)
            self.keep_local_id_list_for_unc_target = self._io.read_bits_int_be(1) != 0
            self._unnamed11 = self._io.read_bits_int_be(2)


    class FileHeader(KaitaiStruct):
        """
        .. seealso::
           Section 2.1 - https://winprotocoldoc.blob.core.windows.net/productionwindowsarchives/MS-SHLLINK/[MS-SHLLINK].pdf
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len_header = self._io.read_bytes(4)
            if not self.len_header == b"\x4C\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x4C\x00\x00\x00", self.len_header, self._io, u"/types/file_header/seq/0")
            self.link_clsid = self._io.read_bytes(16)
            if not self.link_clsid == b"\x01\x14\x02\x00\x00\x00\x00\x00\xC0\x00\x00\x00\x00\x00\x00\x46":
                raise kaitaistruct.ValidationNotEqualError(b"\x01\x14\x02\x00\x00\x00\x00\x00\xC0\x00\x00\x00\x00\x00\x00\x46", self.link_clsid, self._io, u"/types/file_header/seq/1")
            self._raw_flags = self._io.read_bytes(4)
            _io__raw_flags = KaitaiStream(BytesIO(self._raw_flags))
            self.flags = WindowsLnkFile.LinkFlags(_io__raw_flags, self, self._root)
            self.file_attrs = self._io.read_u4le()
            self.time_creation = self._io.read_u8le()
            self.time_access = self._io.read_u8le()
            self.time_write = self._io.read_u8le()
            self.target_file_size = self._io.read_u4le()
            self.icon_index = self._io.read_s4le()
            self.show_command = KaitaiStream.resolve_enum(WindowsLnkFile.WindowState, self._io.read_u4le())
            self.hotkey = self._io.read_u2le()
            self.reserved = self._io.read_bytes(10)
            if not self.reserved == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", self.reserved, self._io, u"/types/file_header/seq/11")



