# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

from . import bytes_with_io
class ResourceFork(KaitaiStruct):
    """The data format of Macintosh resource forks,
    used on Classic Mac OS and Mac OS X/macOS to store additional structured data along with a file's main data (the data fork).
    The kinds of data stored in resource forks include:
    
    * Document resources:
      images, sounds, etc. used by a document
    * Application resources:
      graphics, GUI layouts, localizable strings,
      and even code used by an application, a library, or system files
    * Common metadata:
      custom icons and version metadata that could be displayed by the Finder
    * Application-specific metadata:
      because resource forks follow a common format,
      other applications can store new metadata in them,
      even if the original application does not recognize or understand it
    
    Macintosh file systems (MFS, HFS, HFS+, APFS) support resource forks natively,
    which allows storing resources along with any file.
    Non-Macintosh file systems and protocols have little or no support for resource forks,
    so the resource fork data must be stored in some other way when using such file systems or protocols.
    Various file formats and tools exist for this purpose,
    such as BinHex, MacBinary, AppleSingle, AppleDouble, or QuickTime RezWack.
    In some cases,
    resource forks are stored as plain data in separate files with a .rsrc extension,
    even on Mac systems that natively support resource forks.
    
    On modern Mac OS X/macOS systems,
    resource forks are used far less commonly than on classic Mac OS systems,
    because of compatibility issues with other systems and historical limitations in the format.
    Modern macOS APIs and libraries do not use resource forks,
    and the legacy Carbon API that still used them has been deprecated since OS X 10.8.
    Despite this,
    even current macOS systems still use resource forks for certain purposes,
    such as custom file icons.
    
    .. seealso::
       Inside Macintosh, More Macintosh Toolbox, Resource Manager, Resource Manager Reference, Resource File Format - https://developer.apple.com/library/archive/documentation/mac/pdf/MoreMacintoshToolbox.pdf#page=151
    
    
    .. seealso::
       Inside Macintosh, Volume I, The Resource Manager, Format of a Resource File - http://www.pagetable.com/?p=50
    
    
    .. seealso::
       Source - https://github.com/kreativekorp/ksfl/wiki/Macintosh-Resource-File-Format
    
    
    .. seealso::
       Source - https://github.com/dgelessus/mac_file_format_docs/blob/master/README.md#resource-forks
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.header = ResourceFork.FileHeader(self._io, self, self._root)
        self.system_data = self._io.read_bytes(112)
        self.application_data = self._io.read_bytes(128)

    class FileHeader(KaitaiStruct):
        """Resource file header,
        containing the offsets and lengths of the resource data area and resource map.
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ofs_data_blocks = self._io.read_u4be()
            self.ofs_resource_map = self._io.read_u4be()
            self.len_data_blocks = self._io.read_u4be()
            self.len_resource_map = self._io.read_u4be()


    class DataBlock(KaitaiStruct):
        """A resource data block,
        as stored in the resource data area.
        
        Each data block stores the data contained in a resource,
        along with its length.
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len_data = self._io.read_u4be()
            self.data = self._io.read_bytes(self.len_data)


    class ResourceMap(KaitaiStruct):
        """Resource map,
        containing information about the resources in the file and where they are located in the data area.
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.reserved_file_header_copy = ResourceFork.FileHeader(self._io, self, self._root)
            self.reserved_next_resource_map_handle = self._io.read_u4be()
            self.reserved_file_reference_number = self._io.read_u2be()
            self._raw_file_attributes = self._io.read_bytes(2)
            _io__raw_file_attributes = KaitaiStream(BytesIO(self._raw_file_attributes))
            self.file_attributes = ResourceFork.ResourceMap.FileAttributes(_io__raw_file_attributes, self, self._root)
            self.ofs_type_list = self._io.read_u2be()
            self.ofs_names = self._io.read_u2be()

        class FileAttributes(KaitaiStruct):
            """A resource file's attributes,
            as stored in the resource map.
            
            These attributes are sometimes also referred to as resource map attributes,
            because of where they are stored in the file.
            """
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.resources_locked = self._io.read_bits_int_be(1) != 0
                self.reserved0 = self._io.read_bits_int_be(6)
                self.printer_driver_multifinder_compatible = self._io.read_bits_int_be(1) != 0
                self.no_write_changes = self._io.read_bits_int_be(1) != 0
                self.needs_compact = self._io.read_bits_int_be(1) != 0
                self.map_needs_write = self._io.read_bits_int_be(1) != 0
                self.reserved1 = self._io.read_bits_int_be(5)

            @property
            def as_int(self):
                """The attributes as a packed integer,
                as they are stored in the file.
                """
                if hasattr(self, '_m_as_int'):
                    return self._m_as_int if hasattr(self, '_m_as_int') else None

                _pos = self._io.pos()
                self._io.seek(0)
                self._m_as_int = self._io.read_u2be()
                self._io.seek(_pos)
                return self._m_as_int if hasattr(self, '_m_as_int') else None


        class TypeListAndReferenceLists(KaitaiStruct):
            """Resource type list and storage area for resource reference lists in the resource map.
            
            The two parts are combined into a single type here for technical reasons:
            the start of the resource reference list area is not stored explicitly in the file,
            instead it always starts directly after the resource type list.
            The simplest way to implement this is by placing both types into a single `seq`.
            """
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.type_list = ResourceFork.ResourceMap.TypeListAndReferenceLists.TypeList(self._io, self, self._root)
                self.reference_lists = self._io.read_bytes_full()

            class TypeList(KaitaiStruct):
                """Resource type list in the resource map."""
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.num_types_m1 = self._io.read_u2be()
                    self.entries = [None] * (self.num_types)
                    for i in range(self.num_types):
                        self.entries[i] = ResourceFork.ResourceMap.TypeListAndReferenceLists.TypeList.TypeListEntry(self._io, self, self._root)


                class TypeListEntry(KaitaiStruct):
                    """A single entry in the resource type list.
                    
                    Each entry corresponds to exactly one resource reference list.
                    """
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self._read()

                    def _read(self):
                        self.type = self._io.read_bytes(4)
                        self.num_references_m1 = self._io.read_u2be()
                        self.ofs_reference_list = self._io.read_u2be()

                    @property
                    def num_references(self):
                        """The number of resources in the reference list for this type."""
                        if hasattr(self, '_m_num_references'):
                            return self._m_num_references if hasattr(self, '_m_num_references') else None

                        self._m_num_references = ((self.num_references_m1 + 1) % 65536)
                        return self._m_num_references if hasattr(self, '_m_num_references') else None

                    @property
                    def reference_list(self):
                        """The resource reference list for this resource type.
                        """
                        if hasattr(self, '_m_reference_list'):
                            return self._m_reference_list if hasattr(self, '_m_reference_list') else None

                        io = self._parent._parent._io
                        _pos = io.pos()
                        io.seek(self.ofs_reference_list)
                        self._m_reference_list = ResourceFork.ResourceMap.TypeListAndReferenceLists.ReferenceList(self.num_references, io, self, self._root)
                        io.seek(_pos)
                        return self._m_reference_list if hasattr(self, '_m_reference_list') else None


                @property
                def num_types(self):
                    """The number of resource types in this list."""
                    if hasattr(self, '_m_num_types'):
                        return self._m_num_types if hasattr(self, '_m_num_types') else None

                    self._m_num_types = ((self.num_types_m1 + 1) % 65536)
                    return self._m_num_types if hasattr(self, '_m_num_types') else None


            class ReferenceList(KaitaiStruct):
                """A resource reference list,
                as stored in the reference list area.
                
                Each reference list has exactly one matching entry in the resource type list,
                and describes all resources of a single type in the file.
                """
                def __init__(self, num_references, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self.num_references = num_references
                    self._read()

                def _read(self):
                    self.references = [None] * (self.num_references)
                    for i in range(self.num_references):
                        self.references[i] = ResourceFork.ResourceMap.TypeListAndReferenceLists.ReferenceList.Reference(self._io, self, self._root)


                class Reference(KaitaiStruct):
                    """A single resource reference in a resource reference list."""
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self._read()

                    def _read(self):
                        self.id = self._io.read_s2be()
                        self.ofs_name = self._io.read_u2be()
                        self._raw_attributes = self._io.read_bytes(1)
                        _io__raw_attributes = KaitaiStream(BytesIO(self._raw_attributes))
                        self.attributes = ResourceFork.ResourceMap.TypeListAndReferenceLists.ReferenceList.Reference.Attributes(_io__raw_attributes, self, self._root)
                        self.ofs_data_block = self._io.read_bits_int_be(24)
                        self._io.align_to_byte()
                        self.reserved_handle = self._io.read_u4be()

                    class Attributes(KaitaiStruct):
                        """A resource's attributes,
                        as stored in a resource reference.
                        """
                        def __init__(self, _io, _parent=None, _root=None):
                            self._io = _io
                            self._parent = _parent
                            self._root = _root if _root else self
                            self._read()

                        def _read(self):
                            self.system_reference = self._io.read_bits_int_be(1) != 0
                            self.load_into_system_heap = self._io.read_bits_int_be(1) != 0
                            self.purgeable = self._io.read_bits_int_be(1) != 0
                            self.locked = self._io.read_bits_int_be(1) != 0
                            self.protected = self._io.read_bits_int_be(1) != 0
                            self.preload = self._io.read_bits_int_be(1) != 0
                            self.needs_write = self._io.read_bits_int_be(1) != 0
                            self.compressed = self._io.read_bits_int_be(1) != 0

                        @property
                        def as_int(self):
                            """The attributes as a packed integer,
                            as they are stored in the file.
                            """
                            if hasattr(self, '_m_as_int'):
                                return self._m_as_int if hasattr(self, '_m_as_int') else None

                            _pos = self._io.pos()
                            self._io.seek(0)
                            self._m_as_int = self._io.read_u1()
                            self._io.seek(_pos)
                            return self._m_as_int if hasattr(self, '_m_as_int') else None


                    @property
                    def name(self):
                        """The name (if any) of the resource described by this reference.
                        """
                        if hasattr(self, '_m_name'):
                            return self._m_name if hasattr(self, '_m_name') else None

                        if self.ofs_name != 65535:
                            io = self._root.resource_map.names_with_io._io
                            _pos = io.pos()
                            io.seek(self.ofs_name)
                            self._m_name = ResourceFork.ResourceMap.Name(io, self, self._root)
                            io.seek(_pos)

                        return self._m_name if hasattr(self, '_m_name') else None

                    @property
                    def data_block(self):
                        """The data block containing the data for the resource described by this reference.
                        """
                        if hasattr(self, '_m_data_block'):
                            return self._m_data_block if hasattr(self, '_m_data_block') else None

                        io = self._root.data_blocks_with_io._io
                        _pos = io.pos()
                        io.seek(self.ofs_data_block)
                        self._m_data_block = ResourceFork.DataBlock(io, self, self._root)
                        io.seek(_pos)
                        return self._m_data_block if hasattr(self, '_m_data_block') else None




        class Name(KaitaiStruct):
            """A resource name,
            as stored in the resource name storage area in the resource map.
            
            The resource names are not required to appear in any particular order.
            There may be unused space between and around resource names,
            but in practice they are often contiguous.
            """
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.len_value = self._io.read_u1()
                self.value = self._io.read_bytes(self.len_value)


        @property
        def type_list_and_reference_lists(self):
            """The resource map's resource type list, followed by the resource reference list area."""
            if hasattr(self, '_m_type_list_and_reference_lists'):
                return self._m_type_list_and_reference_lists if hasattr(self, '_m_type_list_and_reference_lists') else None

            _pos = self._io.pos()
            self._io.seek(self.ofs_type_list)
            self._raw__m_type_list_and_reference_lists = self._io.read_bytes((self.ofs_names - self.ofs_type_list))
            _io__raw__m_type_list_and_reference_lists = KaitaiStream(BytesIO(self._raw__m_type_list_and_reference_lists))
            self._m_type_list_and_reference_lists = ResourceFork.ResourceMap.TypeListAndReferenceLists(_io__raw__m_type_list_and_reference_lists, self, self._root)
            self._io.seek(_pos)
            return self._m_type_list_and_reference_lists if hasattr(self, '_m_type_list_and_reference_lists') else None

        @property
        def names_with_io(self):
            """Use `names` instead,
            unless you need access to this instance's `_io`.
            """
            if hasattr(self, '_m_names_with_io'):
                return self._m_names_with_io if hasattr(self, '_m_names_with_io') else None

            _pos = self._io.pos()
            self._io.seek(self.ofs_names)
            self._raw__m_names_with_io = self._io.read_bytes_full()
            _io__raw__m_names_with_io = KaitaiStream(BytesIO(self._raw__m_names_with_io))
            self._m_names_with_io = bytes_with_io.BytesWithIo(_io__raw__m_names_with_io)
            self._io.seek(_pos)
            return self._m_names_with_io if hasattr(self, '_m_names_with_io') else None

        @property
        def names(self):
            """Storage area for the names of all resources."""
            if hasattr(self, '_m_names'):
                return self._m_names if hasattr(self, '_m_names') else None

            self._m_names = self.names_with_io.data
            return self._m_names if hasattr(self, '_m_names') else None


    @property
    def data_blocks_with_io(self):
        """Use `data_blocks` instead,
        unless you need access to this instance's `_io`.
        """
        if hasattr(self, '_m_data_blocks_with_io'):
            return self._m_data_blocks_with_io if hasattr(self, '_m_data_blocks_with_io') else None

        _pos = self._io.pos()
        self._io.seek(self.header.ofs_data_blocks)
        self._raw__m_data_blocks_with_io = self._io.read_bytes(self.header.len_data_blocks)
        _io__raw__m_data_blocks_with_io = KaitaiStream(BytesIO(self._raw__m_data_blocks_with_io))
        self._m_data_blocks_with_io = bytes_with_io.BytesWithIo(_io__raw__m_data_blocks_with_io)
        self._io.seek(_pos)
        return self._m_data_blocks_with_io if hasattr(self, '_m_data_blocks_with_io') else None

    @property
    def data_blocks(self):
        """Storage area for the data blocks of all resources.
        
        These data blocks are not required to appear in any particular order,
        and there may be unused space between and around them.
        
        In practice,
        the data blocks in newly created resource files are usually contiguous.
        When existing resources are shortened,
        the Mac OS resource manager leaves unused space where the now removed resource data was,
        as this is quicker than moving the following resource data into the newly freed space.
        Such unused space may be cleaned up later when the resource manager "compacts" the resource file,
        which happens when resources are removed entirely,
        or when resources are added or grown so that more space is needed in the data area.
        """
        if hasattr(self, '_m_data_blocks'):
            return self._m_data_blocks if hasattr(self, '_m_data_blocks') else None

        self._m_data_blocks = self.data_blocks_with_io.data
        return self._m_data_blocks if hasattr(self, '_m_data_blocks') else None

    @property
    def resource_map(self):
        """The resource file's resource map."""
        if hasattr(self, '_m_resource_map'):
            return self._m_resource_map if hasattr(self, '_m_resource_map') else None

        _pos = self._io.pos()
        self._io.seek(self.header.ofs_resource_map)
        self._raw__m_resource_map = self._io.read_bytes(self.header.len_resource_map)
        _io__raw__m_resource_map = KaitaiStream(BytesIO(self._raw__m_resource_map))
        self._m_resource_map = ResourceFork.ResourceMap(_io__raw__m_resource_map, self, self._root)
        self._io.seek(_pos)
        return self._m_resource_map if hasattr(self, '_m_resource_map') else None


