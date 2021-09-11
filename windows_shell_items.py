# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class WindowsShellItems(KaitaiStruct):
    """Windows Shell Items (AKA "shellbags") is an undocumented set of
    structures used internally within Windows to identify paths in
    Windows Folder Hierarchy. It is widely used in Windows Shell (and
    most visible in File Explorer), both as in-memory and in-file
    structures. Some formats embed them, namely:
    
    * Windows Shell link files (.lnk) Windows registry
    * Windows registry "ShellBags" keys
    
    The format is mostly undocumented, and is known to vary between
    various Windows versions.
    
    .. seealso::
       Source - https://github.com/libyal/libfwsi/blob/master/documentation/Windows%20Shell%20Item%20format.asciidoc
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.items = []
        i = 0
        while True:
            _ = WindowsShellItems.ShellItem(self._io, self, self._root)
            self.items.append(_)
            if _.len_data == 0:
                break
            i += 1

    class ShellItemData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.code = self._io.read_u1()
            _on = self.code
            if _on == 31:
                self.body1 = WindowsShellItems.RootFolderBody(self._io, self, self._root)
            _on = (self.code & 112)
            if _on == 32:
                self.body2 = WindowsShellItems.VolumeBody(self._io, self, self._root)
            elif _on == 48:
                self.body2 = WindowsShellItems.FileEntryBody(self._io, self, self._root)


    class ShellItem(KaitaiStruct):
        """
        .. seealso::
           Section 2.2.2 - https://winprotocoldoc.blob.core.windows.net/productionwindowsarchives/MS-SHLLINK/[MS-SHLLINK].pdf
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len_data = self._io.read_u2le()
            if self.len_data >= 2:
                self._raw_data = self._io.read_bytes((self.len_data - 2))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = WindowsShellItems.ShellItemData(_io__raw_data, self, self._root)



    class RootFolderBody(KaitaiStruct):
        """
        .. seealso::
           Source - https://github.com/libyal/libfwsi/blob/master/documentation/Windows%20Shell%20Item%20format.asciidoc#32-root-folder-shell-item
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.sort_index = self._io.read_u1()
            self.shell_folder_id = self._io.read_bytes(16)


    class VolumeBody(KaitaiStruct):
        """
        .. seealso::
           Source - https://github.com/libyal/libfwsi/blob/master/documentation/Windows%20Shell%20Item%20format.asciidoc#33-volume-shell-item
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.flags = self._io.read_u1()


    class FileEntryBody(KaitaiStruct):
        """
        .. seealso::
           Source - https://github.com/libyal/libfwsi/blob/master/documentation/Windows%20Shell%20Item%20format.asciidoc#34-file-entry-shell-item
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._unnamed0 = self._io.read_u1()
            self.file_size = self._io.read_u4le()
            self.last_mod_time = self._io.read_u4le()
            self.file_attrs = self._io.read_u2le()

        @property
        def is_dir(self):
            if hasattr(self, '_m_is_dir'):
                return self._m_is_dir if hasattr(self, '_m_is_dir') else None

            self._m_is_dir = (self._parent.code & 1) != 0
            return self._m_is_dir if hasattr(self, '_m_is_dir') else None

        @property
        def is_file(self):
            if hasattr(self, '_m_is_file'):
                return self._m_is_file if hasattr(self, '_m_is_file') else None

            self._m_is_file = (self._parent.code & 2) != 0
            return self._m_is_file if hasattr(self, '_m_is_file') else None



