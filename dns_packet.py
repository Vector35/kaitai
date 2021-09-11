# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class DnsPacket(KaitaiStruct):
    """(No support for Auth-Name + Add-Name for simplicity)
    """

    class ClassType(Enum):
        in_class = 1
        cs = 2
        ch = 3
        hs = 4

    class TypeType(Enum):
        a = 1
        ns = 2
        md = 3
        mf = 4
        cname = 5
        soa = 6
        mb = 7
        mg = 8
        mr = 9
        null = 10
        wks = 11
        ptr = 12
        hinfo = 13
        minfo = 14
        mx = 15
        txt = 16
        aaaa = 28
        srv = 33
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.transaction_id = self._io.read_u2be()
        self.flags = DnsPacket.PacketFlags(self._io, self, self._root)
        if self.flags.is_opcode_valid:
            self.qdcount = self._io.read_u2be()

        if self.flags.is_opcode_valid:
            self.ancount = self._io.read_u2be()

        if self.flags.is_opcode_valid:
            self.nscount = self._io.read_u2be()

        if self.flags.is_opcode_valid:
            self.arcount = self._io.read_u2be()

        if self.flags.is_opcode_valid:
            self.queries = [None] * (self.qdcount)
            for i in range(self.qdcount):
                self.queries[i] = DnsPacket.Query(self._io, self, self._root)


        if self.flags.is_opcode_valid:
            self.answers = [None] * (self.ancount)
            for i in range(self.ancount):
                self.answers[i] = DnsPacket.Answer(self._io, self, self._root)


        if self.flags.is_opcode_valid:
            self.authorities = [None] * (self.nscount)
            for i in range(self.nscount):
                self.authorities[i] = DnsPacket.Answer(self._io, self, self._root)


        if self.flags.is_opcode_valid:
            self.additionals = [None] * (self.arcount)
            for i in range(self.arcount):
                self.additionals[i] = DnsPacket.Answer(self._io, self, self._root)



    class MxInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.preference = self._io.read_u2be()
            self.mx = DnsPacket.DomainName(self._io, self, self._root)


    class PointerStruct(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_u1()

        @property
        def contents(self):
            if hasattr(self, '_m_contents'):
                return self._m_contents if hasattr(self, '_m_contents') else None

            io = self._root._io
            _pos = io.pos()
            io.seek((self.value + ((self._parent.length - 192) << 8)))
            self._m_contents = DnsPacket.DomainName(io, self, self._root)
            io.seek(_pos)
            return self._m_contents if hasattr(self, '_m_contents') else None


    class Label(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.length = self._io.read_u1()
            if self.is_pointer:
                self.pointer = DnsPacket.PointerStruct(self._io, self, self._root)

            if not (self.is_pointer):
                self.name = (self._io.read_bytes(self.length)).decode(u"utf-8")


        @property
        def is_pointer(self):
            if hasattr(self, '_m_is_pointer'):
                return self._m_is_pointer if hasattr(self, '_m_is_pointer') else None

            self._m_is_pointer = self.length >= 192
            return self._m_is_pointer if hasattr(self, '_m_is_pointer') else None


    class Query(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = DnsPacket.DomainName(self._io, self, self._root)
            self.type = KaitaiStream.resolve_enum(DnsPacket.TypeType, self._io.read_u2be())
            self.query_class = KaitaiStream.resolve_enum(DnsPacket.ClassType, self._io.read_u2be())


    class DomainName(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = []
            i = 0
            while True:
                _ = DnsPacket.Label(self._io, self, self._root)
                self.name.append(_)
                if  ((_.length == 0) or (_.length >= 192)) :
                    break
                i += 1


    class AddressV6(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ip_v6 = self._io.read_bytes(16)


    class Service(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.priority = self._io.read_u2be()
            self.weight = self._io.read_u2be()
            self.port = self._io.read_u2be()
            self.target = DnsPacket.DomainName(self._io, self, self._root)


    class Txt(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.length = self._io.read_u1()
            self.text = (self._io.read_bytes(self.length)).decode(u"utf-8")


    class TxtBody(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.data = []
            i = 0
            while not self._io.is_eof():
                self.data.append(DnsPacket.Txt(self._io, self, self._root))
                i += 1



    class Address(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ip = self._io.read_bytes(4)


    class Answer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = DnsPacket.DomainName(self._io, self, self._root)
            self.type = KaitaiStream.resolve_enum(DnsPacket.TypeType, self._io.read_u2be())
            self.answer_class = KaitaiStream.resolve_enum(DnsPacket.ClassType, self._io.read_u2be())
            self.ttl = self._io.read_s4be()
            self.rdlength = self._io.read_u2be()
            _on = self.type
            if _on == DnsPacket.TypeType.srv:
                self._raw_payload = self._io.read_bytes(self.rdlength)
                _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
                self.payload = DnsPacket.Service(_io__raw_payload, self, self._root)
            elif _on == DnsPacket.TypeType.a:
                self._raw_payload = self._io.read_bytes(self.rdlength)
                _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
                self.payload = DnsPacket.Address(_io__raw_payload, self, self._root)
            elif _on == DnsPacket.TypeType.cname:
                self._raw_payload = self._io.read_bytes(self.rdlength)
                _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
                self.payload = DnsPacket.DomainName(_io__raw_payload, self, self._root)
            elif _on == DnsPacket.TypeType.ns:
                self._raw_payload = self._io.read_bytes(self.rdlength)
                _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
                self.payload = DnsPacket.DomainName(_io__raw_payload, self, self._root)
            elif _on == DnsPacket.TypeType.soa:
                self._raw_payload = self._io.read_bytes(self.rdlength)
                _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
                self.payload = DnsPacket.AuthorityInfo(_io__raw_payload, self, self._root)
            elif _on == DnsPacket.TypeType.mx:
                self._raw_payload = self._io.read_bytes(self.rdlength)
                _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
                self.payload = DnsPacket.MxInfo(_io__raw_payload, self, self._root)
            elif _on == DnsPacket.TypeType.txt:
                self._raw_payload = self._io.read_bytes(self.rdlength)
                _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
                self.payload = DnsPacket.TxtBody(_io__raw_payload, self, self._root)
            elif _on == DnsPacket.TypeType.ptr:
                self._raw_payload = self._io.read_bytes(self.rdlength)
                _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
                self.payload = DnsPacket.DomainName(_io__raw_payload, self, self._root)
            elif _on == DnsPacket.TypeType.aaaa:
                self._raw_payload = self._io.read_bytes(self.rdlength)
                _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
                self.payload = DnsPacket.AddressV6(_io__raw_payload, self, self._root)
            else:
                self.payload = self._io.read_bytes(self.rdlength)


    class PacketFlags(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.flag = self._io.read_u2be()

        @property
        def qr(self):
            if hasattr(self, '_m_qr'):
                return self._m_qr if hasattr(self, '_m_qr') else None

            self._m_qr = ((self.flag & 32768) >> 15)
            return self._m_qr if hasattr(self, '_m_qr') else None

        @property
        def ra(self):
            if hasattr(self, '_m_ra'):
                return self._m_ra if hasattr(self, '_m_ra') else None

            self._m_ra = ((self.flag & 128) >> 7)
            return self._m_ra if hasattr(self, '_m_ra') else None

        @property
        def tc(self):
            if hasattr(self, '_m_tc'):
                return self._m_tc if hasattr(self, '_m_tc') else None

            self._m_tc = ((self.flag & 512) >> 9)
            return self._m_tc if hasattr(self, '_m_tc') else None

        @property
        def is_opcode_valid(self):
            if hasattr(self, '_m_is_opcode_valid'):
                return self._m_is_opcode_valid if hasattr(self, '_m_is_opcode_valid') else None

            self._m_is_opcode_valid =  ((self.opcode == 0) or (self.opcode == 1) or (self.opcode == 2)) 
            return self._m_is_opcode_valid if hasattr(self, '_m_is_opcode_valid') else None

        @property
        def rcode(self):
            if hasattr(self, '_m_rcode'):
                return self._m_rcode if hasattr(self, '_m_rcode') else None

            self._m_rcode = ((self.flag & 15) >> 0)
            return self._m_rcode if hasattr(self, '_m_rcode') else None

        @property
        def opcode(self):
            if hasattr(self, '_m_opcode'):
                return self._m_opcode if hasattr(self, '_m_opcode') else None

            self._m_opcode = ((self.flag & 30720) >> 11)
            return self._m_opcode if hasattr(self, '_m_opcode') else None

        @property
        def aa(self):
            if hasattr(self, '_m_aa'):
                return self._m_aa if hasattr(self, '_m_aa') else None

            self._m_aa = ((self.flag & 1024) >> 10)
            return self._m_aa if hasattr(self, '_m_aa') else None

        @property
        def z(self):
            if hasattr(self, '_m_z'):
                return self._m_z if hasattr(self, '_m_z') else None

            self._m_z = ((self.flag & 64) >> 6)
            return self._m_z if hasattr(self, '_m_z') else None

        @property
        def rd(self):
            if hasattr(self, '_m_rd'):
                return self._m_rd if hasattr(self, '_m_rd') else None

            self._m_rd = ((self.flag & 256) >> 8)
            return self._m_rd if hasattr(self, '_m_rd') else None

        @property
        def cd(self):
            if hasattr(self, '_m_cd'):
                return self._m_cd if hasattr(self, '_m_cd') else None

            self._m_cd = ((self.flag & 16) >> 4)
            return self._m_cd if hasattr(self, '_m_cd') else None

        @property
        def ad(self):
            if hasattr(self, '_m_ad'):
                return self._m_ad if hasattr(self, '_m_ad') else None

            self._m_ad = ((self.flag & 32) >> 5)
            return self._m_ad if hasattr(self, '_m_ad') else None


    class AuthorityInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.primary_ns = DnsPacket.DomainName(self._io, self, self._root)
            self.resoponsible_mailbox = DnsPacket.DomainName(self._io, self, self._root)
            self.serial = self._io.read_u4be()
            self.refresh_interval = self._io.read_u4be()
            self.retry_interval = self._io.read_u4be()
            self.expire_limit = self._io.read_u4be()
            self.min_ttl = self._io.read_u4be()



