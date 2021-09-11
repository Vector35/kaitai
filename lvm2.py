# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Lvm2(KaitaiStruct):
    """### Building a test file
    
    ```
    dd if=/dev/zero of=image.img bs=512 count=$(( 4 * 1024 * 2 ))
    sudo losetup /dev/loop1 image.img
    sudo pvcreate /dev/loop1
    sudo vgcreate vg_test /dev/loop1
    sudo lvcreate --name lv_test1 vg_test
    sudo losetup -d /dev/loop1
    ```
    
    .. seealso::
       Source - https://github.com/libyal/libvslvm/blob/master/documentation/Logical%20Volume%20Manager%20(LVM)%20format.asciidoc
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.pv = Lvm2.PhysicalVolume(self._io, self, self._root)

    class PhysicalVolume(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.empty_sector = self._io.read_bytes(self._root.sector_size)
            self.label = Lvm2.PhysicalVolume.Label(self._io, self, self._root)

        class Label(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.label_header = Lvm2.PhysicalVolume.Label.LabelHeader(self._io, self, self._root)
                self.volume_header = Lvm2.PhysicalVolume.Label.VolumeHeader(self._io, self, self._root)

            class LabelHeader(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.signature = self._io.read_bytes(8)
                    if not self.signature == b"\x4C\x41\x42\x45\x4C\x4F\x4E\x45":
                        raise kaitaistruct.ValidationNotEqualError(b"\x4C\x41\x42\x45\x4C\x4F\x4E\x45", self.signature, self._io, u"/types/physical_volume/types/label/types/label_header/seq/0")
                    self.sector_number = self._io.read_u8le()
                    self.checksum = self._io.read_u4le()
                    self.label_header_ = Lvm2.PhysicalVolume.Label.LabelHeader.LabelHeader(self._io, self, self._root)

                class LabelHeader(KaitaiStruct):
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self._read()

                    def _read(self):
                        self.data_offset = self._io.read_u4le()
                        self.type_indicator = self._io.read_bytes(8)
                        if not self.type_indicator == b"\x4C\x56\x4D\x32\x20\x30\x30\x31":
                            raise kaitaistruct.ValidationNotEqualError(b"\x4C\x56\x4D\x32\x20\x30\x30\x31", self.type_indicator, self._io, u"/types/physical_volume/types/label/types/label_header/types/label_header_/seq/1")



            class VolumeHeader(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.id = (self._io.read_bytes(32)).decode(u"ascii")
                    self.size = self._io.read_u8le()
                    self.data_area_descriptors = []
                    i = 0
                    while True:
                        _ = Lvm2.PhysicalVolume.Label.VolumeHeader.DataAreaDescriptor(self._io, self, self._root)
                        self.data_area_descriptors.append(_)
                        if  ((_.size != 0) and (_.offset != 0)) :
                            break
                        i += 1
                    self.metadata_area_descriptors = []
                    i = 0
                    while True:
                        _ = Lvm2.PhysicalVolume.Label.VolumeHeader.MetadataAreaDescriptor(self._io, self, self._root)
                        self.metadata_area_descriptors.append(_)
                        if  ((_.size != 0) and (_.offset != 0)) :
                            break
                        i += 1

                class DataAreaDescriptor(KaitaiStruct):
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self._read()

                    def _read(self):
                        self.offset = self._io.read_u8le()
                        self.size = self._io.read_u8le()

                    @property
                    def data(self):
                        if hasattr(self, '_m_data'):
                            return self._m_data if hasattr(self, '_m_data') else None

                        if self.size != 0:
                            _pos = self._io.pos()
                            self._io.seek(self.offset)
                            self._m_data = (self._io.read_bytes(self.size)).decode(u"ascii")
                            self._io.seek(_pos)

                        return self._m_data if hasattr(self, '_m_data') else None


                class MetadataAreaDescriptor(KaitaiStruct):
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self._read()

                    def _read(self):
                        self.offset = self._io.read_u8le()
                        self.size = self._io.read_u8le()

                    @property
                    def data(self):
                        if hasattr(self, '_m_data'):
                            return self._m_data if hasattr(self, '_m_data') else None

                        if self.size != 0:
                            _pos = self._io.pos()
                            self._io.seek(self.offset)
                            self._raw__m_data = self._io.read_bytes(self.size)
                            _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                            self._m_data = Lvm2.PhysicalVolume.Label.VolumeHeader.MetadataArea(_io__raw__m_data, self, self._root)
                            self._io.seek(_pos)

                        return self._m_data if hasattr(self, '_m_data') else None


                class MetadataArea(KaitaiStruct):
                    """According to `[REDHAT]` the metadata area is a circular buffer. New metadata is appended to the old metadata and then the pointer to the start of it is updated. The metadata area, therefore, can contain copies of older versions of the metadata."""
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self._read()

                    def _read(self):
                        self.header = Lvm2.PhysicalVolume.Label.VolumeHeader.MetadataArea.MetadataAreaHeader(self._io, self, self._root)

                    class MetadataAreaHeader(KaitaiStruct):
                        def __init__(self, _io, _parent=None, _root=None):
                            self._io = _io
                            self._parent = _parent
                            self._root = _root if _root else self
                            self._read()

                        def _read(self):
                            self.checksum = Lvm2.PhysicalVolume.Label.VolumeHeader.MetadataArea.MetadataAreaHeader(self._io, self, self._root)
                            self.signature = self._io.read_bytes(16)
                            if not self.signature == b"\x20\x4C\x56\x4D\x32\x20\x78\x5B\x35\x41\x25\x72\x30\x4E\x2A\x3E":
                                raise kaitaistruct.ValidationNotEqualError(b"\x20\x4C\x56\x4D\x32\x20\x78\x5B\x35\x41\x25\x72\x30\x4E\x2A\x3E", self.signature, self._io, u"/types/physical_volume/types/label/types/volume_header/types/metadata_area/types/metadata_area_header/seq/1")
                            self.version = self._io.read_u4le()
                            self.metadata_area_offset = self._io.read_u8le()
                            self.metadata_area_size = self._io.read_u8le()
                            self.raw_location_descriptors = []
                            i = 0
                            while True:
                                _ = Lvm2.PhysicalVolume.Label.VolumeHeader.MetadataArea.MetadataAreaHeader.RawLocationDescriptor(self._io, self, self._root)
                                self.raw_location_descriptors.append(_)
                                if  ((_.offset != 0) and (_.size != 0) and (_.checksum != 0)) :
                                    break
                                i += 1

                        class RawLocationDescriptor(KaitaiStruct):
                            """The data area size can be 0. It is assumed it represents the remaining  available data."""

                            class RawLocationDescriptorFlags(Enum):
                                raw_location_ignored = 1
                            def __init__(self, _io, _parent=None, _root=None):
                                self._io = _io
                                self._parent = _parent
                                self._root = _root if _root else self
                                self._read()

                            def _read(self):
                                self.offset = self._io.read_u8le()
                                self.size = self._io.read_u8le()
                                self.checksum = self._io.read_u4le()
                                self.flags = KaitaiStream.resolve_enum(Lvm2.PhysicalVolume.Label.VolumeHeader.MetadataArea.MetadataAreaHeader.RawLocationDescriptor.RawLocationDescriptorFlags, self._io.read_u4le())


                        @property
                        def metadata(self):
                            if hasattr(self, '_m_metadata'):
                                return self._m_metadata if hasattr(self, '_m_metadata') else None

                            _pos = self._io.pos()
                            self._io.seek(self.metadata_area_offset)
                            self._m_metadata = self._io.read_bytes(self.metadata_area_size)
                            self._io.seek(_pos)
                            return self._m_metadata if hasattr(self, '_m_metadata') else None






    @property
    def sector_size(self):
        if hasattr(self, '_m_sector_size'):
            return self._m_sector_size if hasattr(self, '_m_sector_size') else None

        self._m_sector_size = 512
        return self._m_sector_size if hasattr(self, '_m_sector_size') else None


