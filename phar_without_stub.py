# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

from . import php_serialized_value
class PharWithoutStub(KaitaiStruct):
    """A phar (PHP archive) file. The phar format is a custom archive format
    from the PHP ecosystem that is used to package a complete PHP library
    or application into a single self-contained archive.
    All phar archives start with an executable PHP stub, which can be used to
    allow executing or including phar files as if they were regular PHP scripts.
    PHP 5.3 and later include the phar extension, which adds native support for
    reading and manipulating phar files.
    
    The phar format was originally developed as part of the PEAR library
    PHP_Archive, first released in 2005. Later, a native PHP extension
    named "phar" was developed, which was first released on PECL in 2007,
    and is included with PHP 5.3 and later. The phar extension has effectively
    superseded the PHP_Archive library, which has not been updated since 2010.
    The phar extension is also no longer released independently on PECL;
    it is now developed and released as part of PHP itself.
    
    Because of current limitations in Kaitai Struct
    (seekaitai-io/kaitai_struct#158 and kaitai-io/kaitai_struct#538),
    the executable PHP stub that precedes the rest of the archive is not handled
    by this spec. Before parsing a phar using this spec, the stub must be
    removed manually.
    
    A phar's stub is terminated by the special token `__HALT_COMPILER();`
    (which may be followed by at most one space, the PHP tag end `?>`,
    and an optional line terminator). The stub termination sequence is
    immediately followed by the remaining parts of the phar format,
    as described in this spec.
    
    The phar stub usually contains code that loads the phar and runs
    a contained PHP file, but this is not required. A minimal valid phar stub
    is `<?php __HALT_COMPILER();` - such a stub makes it impossible to execute
    the phar directly, but still allows loading or manipulating it using the
    phar extension.
    
    Note: The phar format does not specify any encoding for text fields
    (stub, alias name, and all file names), so these fields may contain arbitrary
    binary data. The actual text encoding used in a specific phar file usually
    depends on the application that created the phar, and on the
    standard encoding of the system on which the phar was created.
    
    .. seealso::
       Source - https://www.php.net/manual/en/phar.fileformat.php
    
    
    .. seealso::
       Source - https://github.com/php/php-src/tree/master/ext/phar
    
    
    .. seealso::
       Source - https://svn.php.net/viewvc/pecl/phar/
    
    
    .. seealso::
       Source - https://svn.php.net/viewvc/pear/packages/PHP_Archive/
    """

    class SignatureType(Enum):
        md5 = 1
        sha1 = 2
        sha256 = 4
        sha512 = 8
        openssl = 16
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.manifest = PharWithoutStub.Manifest(self._io, self, self._root)
        self.files = [None] * (self.manifest.num_files)
        for i in range(self.manifest.num_files):
            self.files[i] = self._io.read_bytes(self.manifest.file_entries[i].len_data_compressed)

        if self.manifest.flags.has_signature:
            self._raw_signature = self._io.read_bytes_full()
            _io__raw_signature = KaitaiStream(BytesIO(self._raw_signature))
            self.signature = PharWithoutStub.Signature(_io__raw_signature, self, self._root)


    class SerializedValue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bytes_full()

        @property
        def parsed(self):
            """The serialized value, parsed as a structure."""
            if hasattr(self, '_m_parsed'):
                return self._m_parsed if hasattr(self, '_m_parsed') else None

            _pos = self._io.pos()
            self._io.seek(0)
            self._m_parsed = php_serialized_value.PhpSerializedValue(self._io)
            self._io.seek(_pos)
            return self._m_parsed if hasattr(self, '_m_parsed') else None


    class Signature(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.data = self._io.read_bytes(((self._io.size() - self._io.pos()) - 8))
            self.type = KaitaiStream.resolve_enum(PharWithoutStub.SignatureType, self._io.read_u4le())
            self.magic = self._io.read_bytes(4)
            if not self.magic == b"\x47\x42\x4D\x42":
                raise kaitaistruct.ValidationNotEqualError(b"\x47\x42\x4D\x42", self.magic, self._io, u"/types/signature/seq/2")


    class FileFlags(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_u4le()

        @property
        def permissions(self):
            """The file's permission bits."""
            if hasattr(self, '_m_permissions'):
                return self._m_permissions if hasattr(self, '_m_permissions') else None

            self._m_permissions = (self.value & 511)
            return self._m_permissions if hasattr(self, '_m_permissions') else None

        @property
        def zlib_compressed(self):
            """Whether this file's data is stored using zlib compression."""
            if hasattr(self, '_m_zlib_compressed'):
                return self._m_zlib_compressed if hasattr(self, '_m_zlib_compressed') else None

            self._m_zlib_compressed = (self.value & 4096) != 0
            return self._m_zlib_compressed if hasattr(self, '_m_zlib_compressed') else None

        @property
        def bzip2_compressed(self):
            """Whether this file's data is stored using bzip2 compression."""
            if hasattr(self, '_m_bzip2_compressed'):
                return self._m_bzip2_compressed if hasattr(self, '_m_bzip2_compressed') else None

            self._m_bzip2_compressed = (self.value & 8192) != 0
            return self._m_bzip2_compressed if hasattr(self, '_m_bzip2_compressed') else None


    class ApiVersion(KaitaiStruct):
        """A phar API version number. This version number is meant to indicate
        which features are used in a specific phar, so that tools reading
        the phar can easily check that they support all necessary features.
        
        The following API versions exist so far:
        
        * 0.5, 0.6, 0.7, 0.7.1: The first official API versions. At this point,
          the phar format was only used by the PHP_Archive library, and the
          API version numbers were identical to the PHP_Archive versions that
          supported them. Development of the native phar extension started around
          API version 0.7. These API versions could only be queried using the
          `PHP_Archive::APIversion()` method, but were not stored physically
          in archives. These API versions are not supported by this spec.
        * 0.8.0: Used by PHP_Archive 0.8.0 (released 2006-07-18) and
          later development versions of the phar extension. This is the first
          version number to be physically stored in archives. This API version
          is not supported by this spec.
        * 0.9.0: Used by later development/early beta versions of the
          phar extension. Also temporarily used by PHP_Archive 0.9.0
          (released 2006-12-15), but reverted back to API version 0.8.0 in
          PHP_Archive 0.9.1 (released 2007-01-05).
        * 1.0.0: Supported since PHP_Archive 0.10.0 (released 2007-05-29)
          and phar extension 1.0.0 (released 2007-03-28). This is the first
          stable, forwards-compatible and documented version of the format.
        * 1.1.0: Supported since PHP_Archive 0.12.0 (released 2015-07-06)
          and phar extension 1.1.0 (released 2007-04-12). Adds SHA-256 and
          SHA-512 signature types.
        * 1.1.1: Supported since phar extension 2.0.0 (released 2009-07-29 and
          included with PHP 5.3 and later). (PHP_Archive 0.12.0 also supports
          all features from API verison 1.1.1, but it reports API version 1.1.0.)
          Adds the OpenSSL signature type and support for storing
          empty directories.
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.release = self._io.read_bits_int_be(4)
            self.major = self._io.read_bits_int_be(4)
            self.minor = self._io.read_bits_int_be(4)
            self.unused = self._io.read_bits_int_be(4)


    class GlobalFlags(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_u4le()

        @property
        def any_zlib_compressed(self):
            """Whether any of the files in this phar are stored using
            zlib compression.
            """
            if hasattr(self, '_m_any_zlib_compressed'):
                return self._m_any_zlib_compressed if hasattr(self, '_m_any_zlib_compressed') else None

            self._m_any_zlib_compressed = (self.value & 4096) != 0
            return self._m_any_zlib_compressed if hasattr(self, '_m_any_zlib_compressed') else None

        @property
        def any_bzip2_compressed(self):
            """Whether any of the files in this phar are stored using
            bzip2 compression.
            """
            if hasattr(self, '_m_any_bzip2_compressed'):
                return self._m_any_bzip2_compressed if hasattr(self, '_m_any_bzip2_compressed') else None

            self._m_any_bzip2_compressed = (self.value & 8192) != 0
            return self._m_any_bzip2_compressed if hasattr(self, '_m_any_bzip2_compressed') else None

        @property
        def has_signature(self):
            """Whether this phar contains a signature."""
            if hasattr(self, '_m_has_signature'):
                return self._m_has_signature if hasattr(self, '_m_has_signature') else None

            self._m_has_signature = (self.value & 65536) != 0
            return self._m_has_signature if hasattr(self, '_m_has_signature') else None


    class Manifest(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len_manifest = self._io.read_u4le()
            self.num_files = self._io.read_u4le()
            self.api_version = PharWithoutStub.ApiVersion(self._io, self, self._root)
            self.flags = PharWithoutStub.GlobalFlags(self._io, self, self._root)
            self.len_alias = self._io.read_u4le()
            self.alias = self._io.read_bytes(self.len_alias)
            self.len_metadata = self._io.read_u4le()
            if self.len_metadata != 0:
                self._raw_metadata = self._io.read_bytes(self.len_metadata)
                _io__raw_metadata = KaitaiStream(BytesIO(self._raw_metadata))
                self.metadata = PharWithoutStub.SerializedValue(_io__raw_metadata, self, self._root)

            self.file_entries = [None] * (self.num_files)
            for i in range(self.num_files):
                self.file_entries[i] = PharWithoutStub.FileEntry(self._io, self, self._root)



    class FileEntry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len_filename = self._io.read_u4le()
            self.filename = self._io.read_bytes(self.len_filename)
            self.len_data_uncompressed = self._io.read_u4le()
            self.timestamp = self._io.read_u4le()
            self.len_data_compressed = self._io.read_u4le()
            self.crc32 = self._io.read_u4le()
            self.flags = PharWithoutStub.FileFlags(self._io, self, self._root)
            self.len_metadata = self._io.read_u4le()
            if self.len_metadata != 0:
                self._raw_metadata = self._io.read_bytes(self.len_metadata)
                _io__raw_metadata = KaitaiStream(BytesIO(self._raw_metadata))
                self.metadata = PharWithoutStub.SerializedValue(_io__raw_metadata, self, self._root)




