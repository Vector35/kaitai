# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class WindowsResourceFile(KaitaiStruct):
    """Windows resource file (.res) are binary bundles of
    "resources". Resource has some sort of ID (numerical or string),
    type (predefined or user-defined), and raw value. Resource files can
    be seen standalone (as .res file), or embedded inside PE executable
    (.exe, .dll) files.
    
    Typical use cases include:
    
    * providing information about the application (such as title, copyrights, etc)
    * embedding icon(s) to be displayed in file managers into .exe
    * adding non-code data into the binary, such as menus, dialog forms,
      cursor images, fonts, various misc bitmaps, and locale-aware
      strings
    
    Windows provides special API to access "resources" from a binary.
    
    Normally, resources files are created with `rc` compiler: it takes a
    .rc file (so called "resource-definition script") + all the raw
    resource binary files for input, and outputs .res file. That .res
    file can be linked into an .exe / .dll afterwards using a linker.
    
    Internally, resource file is just a sequence of individual resource
    definitions. RC tool ensures that first resource (#0) is always
    empty.
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.resources = []
        i = 0
        while not self._io.is_eof():
            self.resources.append(WindowsResourceFile.Resource(self._io, self, self._root))
            i += 1


    class Resource(KaitaiStruct):
        """Each resource has a `type` and a `name`, which can be used to
        identify it, and a `value`. Both `type` and `name` can be a
        number or a string.
        
        .. seealso::
           Source - https://msdn.microsoft.com/en-us/library/windows/desktop/ms648027.aspx
        """

        class PredefTypes(Enum):
            cursor = 1
            bitmap = 2
            icon = 3
            menu = 4
            dialog = 5
            string = 6
            fontdir = 7
            font = 8
            accelerator = 9
            rcdata = 10
            messagetable = 11
            group_cursor = 12
            group_icon = 14
            version = 16
            dlginclude = 17
            plugplay = 19
            vxd = 20
            anicursor = 21
            aniicon = 22
            html = 23
            manifest = 24
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value_size = self._io.read_u4le()
            self.header_size = self._io.read_u4le()
            self.type = WindowsResourceFile.UnicodeOrId(self._io, self, self._root)
            self.name = WindowsResourceFile.UnicodeOrId(self._io, self, self._root)
            self.padding1 = self._io.read_bytes(((4 - self._io.pos()) % 4))
            self.format_version = self._io.read_u4le()
            self.flags = self._io.read_u2le()
            self.language = self._io.read_u2le()
            self.value_version = self._io.read_u4le()
            self.characteristics = self._io.read_u4le()
            self.value = self._io.read_bytes(self.value_size)
            self.padding2 = self._io.read_bytes(((4 - self._io.pos()) % 4))

        @property
        def type_as_predef(self):
            """Numeric type IDs in range of [0..0xff] are reserved for
            system usage in Windows, and there are some predefined,
            well-known values in that range. This instance allows to get
            it as enum value, if applicable.
            """
            if hasattr(self, '_m_type_as_predef'):
                return self._m_type_as_predef if hasattr(self, '_m_type_as_predef') else None

            if  ((not (self.type.is_string)) and (self.type.as_numeric <= 255)) :
                self._m_type_as_predef = KaitaiStream.resolve_enum(WindowsResourceFile.Resource.PredefTypes, self.type.as_numeric)

            return self._m_type_as_predef if hasattr(self, '_m_type_as_predef') else None


    class UnicodeOrId(KaitaiStruct):
        """Resources use a special serialization of names and types: they
        can be either a number or a string.
        
        Use `is_string` to check which kind we've got here, and then use
        `as_numeric` or `as_string` to get relevant value.
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            if self.save_pos1 >= 0:
                self.first = self._io.read_u2le()

            if not (self.is_string):
                self.as_numeric = self._io.read_u2le()

            if self.is_string:
                self.rest = []
                i = 0
                while True:
                    _ = self._io.read_u2le()
                    self.rest.append(_)
                    if _ == 0:
                        break
                    i += 1

            if  ((self.is_string) and (self.save_pos2 >= 0)) :
                self.noop = self._io.read_bytes(0)


        @property
        def save_pos1(self):
            if hasattr(self, '_m_save_pos1'):
                return self._m_save_pos1 if hasattr(self, '_m_save_pos1') else None

            self._m_save_pos1 = self._io.pos()
            return self._m_save_pos1 if hasattr(self, '_m_save_pos1') else None

        @property
        def save_pos2(self):
            if hasattr(self, '_m_save_pos2'):
                return self._m_save_pos2 if hasattr(self, '_m_save_pos2') else None

            self._m_save_pos2 = self._io.pos()
            return self._m_save_pos2 if hasattr(self, '_m_save_pos2') else None

        @property
        def is_string(self):
            if hasattr(self, '_m_is_string'):
                return self._m_is_string if hasattr(self, '_m_is_string') else None

            self._m_is_string = self.first != 65535
            return self._m_is_string if hasattr(self, '_m_is_string') else None

        @property
        def as_string(self):
            if hasattr(self, '_m_as_string'):
                return self._m_as_string if hasattr(self, '_m_as_string') else None

            if self.is_string:
                _pos = self._io.pos()
                self._io.seek(self.save_pos1)
                self._m_as_string = (self._io.read_bytes(((self.save_pos2 - self.save_pos1) - 2))).decode(u"UTF-16LE")
                self._io.seek(_pos)

            return self._m_as_string if hasattr(self, '_m_as_string') else None



