# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Elf(KaitaiStruct):
    """
    .. seealso::
       Source - https://sourceware.org/git/?p=glibc.git;a=blob;f=elf/elf.h;hb=HEAD
    """

    class Endian(Enum):
        le = 1
        be = 2

    class ShType(Enum):
        null_type = 0
        progbits = 1
        symtab = 2
        strtab = 3
        rela = 4
        hash = 5
        dynamic = 6
        note = 7
        nobits = 8
        rel = 9
        shlib = 10
        dynsym = 11
        init_array = 14
        fini_array = 15
        preinit_array = 16
        group = 17
        symtab_shndx = 18
        sunw_capchain = 1879048175
        sunw_capinfo = 1879048176
        sunw_symsort = 1879048177
        sunw_tlssort = 1879048178
        sunw_ldynsym = 1879048179
        sunw_dof = 1879048180
        sunw_cap = 1879048181
        sunw_signature = 1879048182
        sunw_annotate = 1879048183
        sunw_debugstr = 1879048184
        sunw_debug = 1879048185
        sunw_move = 1879048186
        sunw_comdat = 1879048187
        sunw_syminfo = 1879048188
        sunw_verdef = 1879048189
        sunw_verneed = 1879048190
        sunw_versym = 1879048191
        sparc_gotdata = 1879048192
        amd64_unwind = 1879048193
        arm_preemptmap = 1879048194
        arm_attributes = 1879048195

    class OsAbi(Enum):
        system_v = 0
        hp_ux = 1
        netbsd = 2
        gnu = 3
        solaris = 6
        aix = 7
        irix = 8
        freebsd = 9
        tru64 = 10
        modesto = 11
        openbsd = 12
        openvms = 13
        nsk = 14
        aros = 15
        fenixos = 16
        cloudabi = 17
        openvos = 18

    class Machine(Enum):
        not_set = 0
        sparc = 2
        x86 = 3
        mips = 8
        powerpc = 20
        arm = 40
        superh = 42
        ia_64 = 50
        x86_64 = 62
        aarch64 = 183
        riscv = 243
        bpf = 247

    class DynamicArrayTags(Enum):
        null = 0
        needed = 1
        pltrelsz = 2
        pltgot = 3
        hash = 4
        strtab = 5
        symtab = 6
        rela = 7
        relasz = 8
        relaent = 9
        strsz = 10
        syment = 11
        init = 12
        fini = 13
        soname = 14
        rpath = 15
        symbolic = 16
        rel = 17
        relsz = 18
        relent = 19
        pltrel = 20
        debug = 21
        textrel = 22
        jmprel = 23
        bind_now = 24
        init_array = 25
        fini_array = 26
        init_arraysz = 27
        fini_arraysz = 28
        runpath = 29
        flags = 30
        preinit_array = 32
        preinit_arraysz = 33
        maxpostags = 34
        sunw_auxiliary = 1610612749
        sunw_filter = 1610612750
        sunw_cap = 1610612752
        sunw_symtab = 1610612753
        sunw_symsz = 1610612754
        sunw_sortent = 1610612755
        sunw_symsort = 1610612756
        sunw_symsortsz = 1610612757
        sunw_tlssort = 1610612758
        sunw_tlssortsz = 1610612759
        sunw_capinfo = 1610612760
        sunw_strpad = 1610612761
        sunw_capchain = 1610612762
        sunw_ldmach = 1610612763
        sunw_capchainent = 1610612765
        sunw_capchainsz = 1610612767
        gnu_prelinked = 1879047669
        gnu_conflictsz = 1879047670
        gnu_liblistsz = 1879047671
        checksum = 1879047672
        pltpadsz = 1879047673
        moveent = 1879047674
        movesz = 1879047675
        feature_1 = 1879047676
        posflag_1 = 1879047677
        syminsz = 1879047678
        syminent = 1879047679
        gnu_hash = 1879047925
        tlsdesc_plt = 1879047926
        tlsdesc_got = 1879047927
        gnu_conflict = 1879047928
        gnu_liblist = 1879047929
        config = 1879047930
        depaudit = 1879047931
        audit = 1879047932
        pltpad = 1879047933
        movetab = 1879047934
        syminfo = 1879047935
        versym = 1879048176
        relacount = 1879048185
        relcount = 1879048186
        flags_1 = 1879048187
        verdef = 1879048188
        verdefnum = 1879048189
        verneed = 1879048190
        verneednum = 1879048191
        sparc_register = 1879048193
        auxiliary = 2147483645
        used = 2147483646
        filter = 2147483647

    class Bits(Enum):
        b32 = 1
        b64 = 2

    class PhType(Enum):
        null_type = 0
        load = 1
        dynamic = 2
        interp = 3
        note = 4
        shlib = 5
        phdr = 6
        tls = 7
        gnu_eh_frame = 1685382480
        gnu_stack = 1685382481
        gnu_relro = 1685382482
        pax_flags = 1694766464
        hios = 1879048191
        arm_exidx = 1879048193

    class ObjType(Enum):
        relocatable = 1
        executable = 2
        shared = 3
        core = 4
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(4)
        if not self.magic == b"\x7F\x45\x4C\x46":
            raise kaitaistruct.ValidationNotEqualError(b"\x7F\x45\x4C\x46", self.magic, self._io, u"/seq/0")
        self.bits = KaitaiStream.resolve_enum(Elf.Bits, self._io.read_u1())
        self.endian = KaitaiStream.resolve_enum(Elf.Endian, self._io.read_u1())
        self.ei_version = self._io.read_u1()
        self.abi = KaitaiStream.resolve_enum(Elf.OsAbi, self._io.read_u1())
        self.abi_version = self._io.read_u1()
        self.pad = self._io.read_bytes(7)
        self.header = Elf.EndianElf(self._io, self, self._root)

    class PhdrTypeFlags(KaitaiStruct):
        def __init__(self, value, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.value = value
            self._read()

        def _read(self):
            pass

        @property
        def read(self):
            if hasattr(self, '_m_read'):
                return self._m_read if hasattr(self, '_m_read') else None

            self._m_read = (self.value & 4) != 0
            return self._m_read if hasattr(self, '_m_read') else None

        @property
        def write(self):
            if hasattr(self, '_m_write'):
                return self._m_write if hasattr(self, '_m_write') else None

            self._m_write = (self.value & 2) != 0
            return self._m_write if hasattr(self, '_m_write') else None

        @property
        def execute(self):
            if hasattr(self, '_m_execute'):
                return self._m_execute if hasattr(self, '_m_execute') else None

            self._m_execute = (self.value & 1) != 0
            return self._m_execute if hasattr(self, '_m_execute') else None

        @property
        def mask_proc(self):
            if hasattr(self, '_m_mask_proc'):
                return self._m_mask_proc if hasattr(self, '_m_mask_proc') else None

            self._m_mask_proc = (self.value & 4026531840) != 0
            return self._m_mask_proc if hasattr(self, '_m_mask_proc') else None


    class SectionHeaderFlags(KaitaiStruct):
        def __init__(self, value, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.value = value
            self._read()

        def _read(self):
            pass

        @property
        def merge(self):
            """might be merged."""
            if hasattr(self, '_m_merge'):
                return self._m_merge if hasattr(self, '_m_merge') else None

            self._m_merge = (self.value & 16) != 0
            return self._m_merge if hasattr(self, '_m_merge') else None

        @property
        def mask_os(self):
            """OS-specific."""
            if hasattr(self, '_m_mask_os'):
                return self._m_mask_os if hasattr(self, '_m_mask_os') else None

            self._m_mask_os = (self.value & 267386880) != 0
            return self._m_mask_os if hasattr(self, '_m_mask_os') else None

        @property
        def exclude(self):
            """section is excluded unless referenced or allocated (Solaris)."""
            if hasattr(self, '_m_exclude'):
                return self._m_exclude if hasattr(self, '_m_exclude') else None

            self._m_exclude = (self.value & 134217728) != 0
            return self._m_exclude if hasattr(self, '_m_exclude') else None

        @property
        def mask_proc(self):
            """Processor-specific."""
            if hasattr(self, '_m_mask_proc'):
                return self._m_mask_proc if hasattr(self, '_m_mask_proc') else None

            self._m_mask_proc = (self.value & 4026531840) != 0
            return self._m_mask_proc if hasattr(self, '_m_mask_proc') else None

        @property
        def strings(self):
            """contains nul-terminated strings."""
            if hasattr(self, '_m_strings'):
                return self._m_strings if hasattr(self, '_m_strings') else None

            self._m_strings = (self.value & 32) != 0
            return self._m_strings if hasattr(self, '_m_strings') else None

        @property
        def os_non_conforming(self):
            """non-standard OS specific handling required."""
            if hasattr(self, '_m_os_non_conforming'):
                return self._m_os_non_conforming if hasattr(self, '_m_os_non_conforming') else None

            self._m_os_non_conforming = (self.value & 256) != 0
            return self._m_os_non_conforming if hasattr(self, '_m_os_non_conforming') else None

        @property
        def alloc(self):
            """occupies memory during execution."""
            if hasattr(self, '_m_alloc'):
                return self._m_alloc if hasattr(self, '_m_alloc') else None

            self._m_alloc = (self.value & 2) != 0
            return self._m_alloc if hasattr(self, '_m_alloc') else None

        @property
        def exec_instr(self):
            """executable."""
            if hasattr(self, '_m_exec_instr'):
                return self._m_exec_instr if hasattr(self, '_m_exec_instr') else None

            self._m_exec_instr = (self.value & 4) != 0
            return self._m_exec_instr if hasattr(self, '_m_exec_instr') else None

        @property
        def info_link(self):
            """'sh_info' contains SHT index."""
            if hasattr(self, '_m_info_link'):
                return self._m_info_link if hasattr(self, '_m_info_link') else None

            self._m_info_link = (self.value & 64) != 0
            return self._m_info_link if hasattr(self, '_m_info_link') else None

        @property
        def write(self):
            """writable."""
            if hasattr(self, '_m_write'):
                return self._m_write if hasattr(self, '_m_write') else None

            self._m_write = (self.value & 1) != 0
            return self._m_write if hasattr(self, '_m_write') else None

        @property
        def link_order(self):
            """preserve order after combining."""
            if hasattr(self, '_m_link_order'):
                return self._m_link_order if hasattr(self, '_m_link_order') else None

            self._m_link_order = (self.value & 128) != 0
            return self._m_link_order if hasattr(self, '_m_link_order') else None

        @property
        def ordered(self):
            """special ordering requirement (Solaris)."""
            if hasattr(self, '_m_ordered'):
                return self._m_ordered if hasattr(self, '_m_ordered') else None

            self._m_ordered = (self.value & 67108864) != 0
            return self._m_ordered if hasattr(self, '_m_ordered') else None

        @property
        def tls(self):
            """section hold thread-local data."""
            if hasattr(self, '_m_tls'):
                return self._m_tls if hasattr(self, '_m_tls') else None

            self._m_tls = (self.value & 1024) != 0
            return self._m_tls if hasattr(self, '_m_tls') else None

        @property
        def group(self):
            """section is member of a group."""
            if hasattr(self, '_m_group'):
                return self._m_group if hasattr(self, '_m_group') else None

            self._m_group = (self.value & 512) != 0
            return self._m_group if hasattr(self, '_m_group') else None


    class DtFlag1Values(KaitaiStruct):
        def __init__(self, value, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.value = value
            self._read()

        def _read(self):
            pass

        @property
        def singleton(self):
            """Singleton symbols are used."""
            if hasattr(self, '_m_singleton'):
                return self._m_singleton if hasattr(self, '_m_singleton') else None

            self._m_singleton = (self.value & 33554432) != 0
            return self._m_singleton if hasattr(self, '_m_singleton') else None

        @property
        def ignmuldef(self):
            if hasattr(self, '_m_ignmuldef'):
                return self._m_ignmuldef if hasattr(self, '_m_ignmuldef') else None

            self._m_ignmuldef = (self.value & 262144) != 0
            return self._m_ignmuldef if hasattr(self, '_m_ignmuldef') else None

        @property
        def loadfltr(self):
            """Trigger filtee loading at runtime."""
            if hasattr(self, '_m_loadfltr'):
                return self._m_loadfltr if hasattr(self, '_m_loadfltr') else None

            self._m_loadfltr = (self.value & 16) != 0
            return self._m_loadfltr if hasattr(self, '_m_loadfltr') else None

        @property
        def initfirst(self):
            """Set RTLD_INITFIRST for this object."""
            if hasattr(self, '_m_initfirst'):
                return self._m_initfirst if hasattr(self, '_m_initfirst') else None

            self._m_initfirst = (self.value & 32) != 0
            return self._m_initfirst if hasattr(self, '_m_initfirst') else None

        @property
        def symintpose(self):
            """Object has individual interposers."""
            if hasattr(self, '_m_symintpose'):
                return self._m_symintpose if hasattr(self, '_m_symintpose') else None

            self._m_symintpose = (self.value & 8388608) != 0
            return self._m_symintpose if hasattr(self, '_m_symintpose') else None

        @property
        def noreloc(self):
            if hasattr(self, '_m_noreloc'):
                return self._m_noreloc if hasattr(self, '_m_noreloc') else None

            self._m_noreloc = (self.value & 4194304) != 0
            return self._m_noreloc if hasattr(self, '_m_noreloc') else None

        @property
        def confalt(self):
            """Configuration alternative created."""
            if hasattr(self, '_m_confalt'):
                return self._m_confalt if hasattr(self, '_m_confalt') else None

            self._m_confalt = (self.value & 8192) != 0
            return self._m_confalt if hasattr(self, '_m_confalt') else None

        @property
        def dispreldne(self):
            """Disp reloc applied at build time."""
            if hasattr(self, '_m_dispreldne'):
                return self._m_dispreldne if hasattr(self, '_m_dispreldne') else None

            self._m_dispreldne = (self.value & 32768) != 0
            return self._m_dispreldne if hasattr(self, '_m_dispreldne') else None

        @property
        def rtld_global(self):
            """Set RTLD_GLOBAL for this object."""
            if hasattr(self, '_m_rtld_global'):
                return self._m_rtld_global if hasattr(self, '_m_rtld_global') else None

            self._m_rtld_global = (self.value & 2) != 0
            return self._m_rtld_global if hasattr(self, '_m_rtld_global') else None

        @property
        def nodelete(self):
            """Set RTLD_NODELETE for this object."""
            if hasattr(self, '_m_nodelete'):
                return self._m_nodelete if hasattr(self, '_m_nodelete') else None

            self._m_nodelete = (self.value & 8) != 0
            return self._m_nodelete if hasattr(self, '_m_nodelete') else None

        @property
        def trans(self):
            if hasattr(self, '_m_trans'):
                return self._m_trans if hasattr(self, '_m_trans') else None

            self._m_trans = (self.value & 512) != 0
            return self._m_trans if hasattr(self, '_m_trans') else None

        @property
        def origin(self):
            """$ORIGIN must be handled."""
            if hasattr(self, '_m_origin'):
                return self._m_origin if hasattr(self, '_m_origin') else None

            self._m_origin = (self.value & 128) != 0
            return self._m_origin if hasattr(self, '_m_origin') else None

        @property
        def now(self):
            """Set RTLD_NOW for this object."""
            if hasattr(self, '_m_now'):
                return self._m_now if hasattr(self, '_m_now') else None

            self._m_now = (self.value & 1) != 0
            return self._m_now if hasattr(self, '_m_now') else None

        @property
        def nohdr(self):
            if hasattr(self, '_m_nohdr'):
                return self._m_nohdr if hasattr(self, '_m_nohdr') else None

            self._m_nohdr = (self.value & 1048576) != 0
            return self._m_nohdr if hasattr(self, '_m_nohdr') else None

        @property
        def endfiltee(self):
            """Filtee terminates filters search."""
            if hasattr(self, '_m_endfiltee'):
                return self._m_endfiltee if hasattr(self, '_m_endfiltee') else None

            self._m_endfiltee = (self.value & 16384) != 0
            return self._m_endfiltee if hasattr(self, '_m_endfiltee') else None

        @property
        def nodirect(self):
            """Object has no-direct binding."""
            if hasattr(self, '_m_nodirect'):
                return self._m_nodirect if hasattr(self, '_m_nodirect') else None

            self._m_nodirect = (self.value & 131072) != 0
            return self._m_nodirect if hasattr(self, '_m_nodirect') else None

        @property
        def globaudit(self):
            """Global auditing required."""
            if hasattr(self, '_m_globaudit'):
                return self._m_globaudit if hasattr(self, '_m_globaudit') else None

            self._m_globaudit = (self.value & 16777216) != 0
            return self._m_globaudit if hasattr(self, '_m_globaudit') else None

        @property
        def noksyms(self):
            if hasattr(self, '_m_noksyms'):
                return self._m_noksyms if hasattr(self, '_m_noksyms') else None

            self._m_noksyms = (self.value & 524288) != 0
            return self._m_noksyms if hasattr(self, '_m_noksyms') else None

        @property
        def interpose(self):
            """Object is used to interpose."""
            if hasattr(self, '_m_interpose'):
                return self._m_interpose if hasattr(self, '_m_interpose') else None

            self._m_interpose = (self.value & 1024) != 0
            return self._m_interpose if hasattr(self, '_m_interpose') else None

        @property
        def nodump(self):
            """Object can't be dldump'ed."""
            if hasattr(self, '_m_nodump'):
                return self._m_nodump if hasattr(self, '_m_nodump') else None

            self._m_nodump = (self.value & 4096) != 0
            return self._m_nodump if hasattr(self, '_m_nodump') else None

        @property
        def disprelpnd(self):
            """Disp reloc applied at run-time."""
            if hasattr(self, '_m_disprelpnd'):
                return self._m_disprelpnd if hasattr(self, '_m_disprelpnd') else None

            self._m_disprelpnd = (self.value & 65536) != 0
            return self._m_disprelpnd if hasattr(self, '_m_disprelpnd') else None

        @property
        def noopen(self):
            """Set RTLD_NOOPEN for this object."""
            if hasattr(self, '_m_noopen'):
                return self._m_noopen if hasattr(self, '_m_noopen') else None

            self._m_noopen = (self.value & 64) != 0
            return self._m_noopen if hasattr(self, '_m_noopen') else None

        @property
        def stub(self):
            if hasattr(self, '_m_stub'):
                return self._m_stub if hasattr(self, '_m_stub') else None

            self._m_stub = (self.value & 67108864) != 0
            return self._m_stub if hasattr(self, '_m_stub') else None

        @property
        def direct(self):
            """Direct binding enabled."""
            if hasattr(self, '_m_direct'):
                return self._m_direct if hasattr(self, '_m_direct') else None

            self._m_direct = (self.value & 256) != 0
            return self._m_direct if hasattr(self, '_m_direct') else None

        @property
        def edited(self):
            """Object is modified after built."""
            if hasattr(self, '_m_edited'):
                return self._m_edited if hasattr(self, '_m_edited') else None

            self._m_edited = (self.value & 2097152) != 0
            return self._m_edited if hasattr(self, '_m_edited') else None

        @property
        def group(self):
            """Set RTLD_GROUP for this object."""
            if hasattr(self, '_m_group'):
                return self._m_group if hasattr(self, '_m_group') else None

            self._m_group = (self.value & 4) != 0
            return self._m_group if hasattr(self, '_m_group') else None

        @property
        def pie(self):
            if hasattr(self, '_m_pie'):
                return self._m_pie if hasattr(self, '_m_pie') else None

            self._m_pie = (self.value & 134217728) != 0
            return self._m_pie if hasattr(self, '_m_pie') else None

        @property
        def nodeflib(self):
            """Ignore default lib search path."""
            if hasattr(self, '_m_nodeflib'):
                return self._m_nodeflib if hasattr(self, '_m_nodeflib') else None

            self._m_nodeflib = (self.value & 2048) != 0
            return self._m_nodeflib if hasattr(self, '_m_nodeflib') else None


    class EndianElf(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            _on = self._root.endian
            if _on == Elf.Endian.le:
                self._is_le = True
            elif _on == Elf.Endian.be:
                self._is_le = False
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/endian_elf")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.e_type = KaitaiStream.resolve_enum(Elf.ObjType, self._io.read_u2le())
            self.machine = KaitaiStream.resolve_enum(Elf.Machine, self._io.read_u2le())
            self.e_version = self._io.read_u4le()
            _on = self._root.bits
            if _on == Elf.Bits.b32:
                self.entry_point = self._io.read_u4le()
            elif _on == Elf.Bits.b64:
                self.entry_point = self._io.read_u8le()
            _on = self._root.bits
            if _on == Elf.Bits.b32:
                self.program_header_offset = self._io.read_u4le()
            elif _on == Elf.Bits.b64:
                self.program_header_offset = self._io.read_u8le()
            _on = self._root.bits
            if _on == Elf.Bits.b32:
                self.section_header_offset = self._io.read_u4le()
            elif _on == Elf.Bits.b64:
                self.section_header_offset = self._io.read_u8le()
            self.flags = self._io.read_bytes(4)
            self.e_ehsize = self._io.read_u2le()
            self.program_header_entry_size = self._io.read_u2le()
            self.qty_program_header = self._io.read_u2le()
            self.section_header_entry_size = self._io.read_u2le()
            self.qty_section_header = self._io.read_u2le()
            self.section_names_idx = self._io.read_u2le()

        def _read_be(self):
            self.e_type = KaitaiStream.resolve_enum(Elf.ObjType, self._io.read_u2be())
            self.machine = KaitaiStream.resolve_enum(Elf.Machine, self._io.read_u2be())
            self.e_version = self._io.read_u4be()
            _on = self._root.bits
            if _on == Elf.Bits.b32:
                self.entry_point = self._io.read_u4be()
            elif _on == Elf.Bits.b64:
                self.entry_point = self._io.read_u8be()
            _on = self._root.bits
            if _on == Elf.Bits.b32:
                self.program_header_offset = self._io.read_u4be()
            elif _on == Elf.Bits.b64:
                self.program_header_offset = self._io.read_u8be()
            _on = self._root.bits
            if _on == Elf.Bits.b32:
                self.section_header_offset = self._io.read_u4be()
            elif _on == Elf.Bits.b64:
                self.section_header_offset = self._io.read_u8be()
            self.flags = self._io.read_bytes(4)
            self.e_ehsize = self._io.read_u2be()
            self.program_header_entry_size = self._io.read_u2be()
            self.qty_program_header = self._io.read_u2be()
            self.section_header_entry_size = self._io.read_u2be()
            self.qty_section_header = self._io.read_u2be()
            self.section_names_idx = self._io.read_u2be()

        class DynsymSectionEntry64(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._is_le = _is_le
                self._read()

            def _read(self):
                if not hasattr(self, '_is_le'):
                    raise kaitaistruct.UndecidedEndiannessError("/types/endian_elf/types/dynsym_section_entry64")
                elif self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()

            def _read_le(self):
                self.name_offset = self._io.read_u4le()
                self.info = self._io.read_u1()
                self.other = self._io.read_u1()
                self.shndx = self._io.read_u2le()
                self.value = self._io.read_u8le()
                self.size = self._io.read_u8le()

            def _read_be(self):
                self.name_offset = self._io.read_u4be()
                self.info = self._io.read_u1()
                self.other = self._io.read_u1()
                self.shndx = self._io.read_u2be()
                self.value = self._io.read_u8be()
                self.size = self._io.read_u8be()


        class ProgramHeader(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._is_le = _is_le
                self._read()

            def _read(self):
                if not hasattr(self, '_is_le'):
                    raise kaitaistruct.UndecidedEndiannessError("/types/endian_elf/types/program_header")
                elif self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()

            def _read_le(self):
                self.type = KaitaiStream.resolve_enum(Elf.PhType, self._io.read_u4le())
                if self._root.bits == Elf.Bits.b64:
                    self.flags64 = self._io.read_u4le()

                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.offset = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.offset = self._io.read_u8le()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.vaddr = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.vaddr = self._io.read_u8le()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.paddr = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.paddr = self._io.read_u8le()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.filesz = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.filesz = self._io.read_u8le()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.memsz = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.memsz = self._io.read_u8le()
                if self._root.bits == Elf.Bits.b32:
                    self.flags32 = self._io.read_u4le()

                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.align = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.align = self._io.read_u8le()

            def _read_be(self):
                self.type = KaitaiStream.resolve_enum(Elf.PhType, self._io.read_u4be())
                if self._root.bits == Elf.Bits.b64:
                    self.flags64 = self._io.read_u4be()

                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.offset = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.offset = self._io.read_u8be()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.vaddr = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.vaddr = self._io.read_u8be()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.paddr = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.paddr = self._io.read_u8be()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.filesz = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.filesz = self._io.read_u8be()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.memsz = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.memsz = self._io.read_u8be()
                if self._root.bits == Elf.Bits.b32:
                    self.flags32 = self._io.read_u4be()

                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.align = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.align = self._io.read_u8be()

            @property
            def dynamic(self):
                if hasattr(self, '_m_dynamic'):
                    return self._m_dynamic if hasattr(self, '_m_dynamic') else None

                if self.type == Elf.PhType.dynamic:
                    io = self._root._io
                    _pos = io.pos()
                    io.seek(self.offset)
                    if self._is_le:
                        self._raw__m_dynamic = io.read_bytes(self.filesz)
                        _io__raw__m_dynamic = KaitaiStream(BytesIO(self._raw__m_dynamic))
                        self._m_dynamic = Elf.EndianElf.DynamicSection(_io__raw__m_dynamic, self, self._root, self._is_le)
                    else:
                        self._raw__m_dynamic = io.read_bytes(self.filesz)
                        _io__raw__m_dynamic = KaitaiStream(BytesIO(self._raw__m_dynamic))
                        self._m_dynamic = Elf.EndianElf.DynamicSection(_io__raw__m_dynamic, self, self._root, self._is_le)
                    io.seek(_pos)

                return self._m_dynamic if hasattr(self, '_m_dynamic') else None

            @property
            def flags_obj(self):
                if hasattr(self, '_m_flags_obj'):
                    return self._m_flags_obj if hasattr(self, '_m_flags_obj') else None

                if self._is_le:
                    self._m_flags_obj = Elf.PhdrTypeFlags((self.flags64 | self.flags32), self._io, self, self._root)
                else:
                    self._m_flags_obj = Elf.PhdrTypeFlags((self.flags64 | self.flags32), self._io, self, self._root)
                return self._m_flags_obj if hasattr(self, '_m_flags_obj') else None


        class DynamicSectionEntry(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._is_le = _is_le
                self._read()

            def _read(self):
                if not hasattr(self, '_is_le'):
                    raise kaitaistruct.UndecidedEndiannessError("/types/endian_elf/types/dynamic_section_entry")
                elif self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()

            def _read_le(self):
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.tag = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.tag = self._io.read_u8le()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.value_or_ptr = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.value_or_ptr = self._io.read_u8le()

            def _read_be(self):
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.tag = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.tag = self._io.read_u8be()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.value_or_ptr = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.value_or_ptr = self._io.read_u8be()

            @property
            def tag_enum(self):
                if hasattr(self, '_m_tag_enum'):
                    return self._m_tag_enum if hasattr(self, '_m_tag_enum') else None

                self._m_tag_enum = KaitaiStream.resolve_enum(Elf.DynamicArrayTags, self.tag)
                return self._m_tag_enum if hasattr(self, '_m_tag_enum') else None

            @property
            def flag_1_values(self):
                if hasattr(self, '_m_flag_1_values'):
                    return self._m_flag_1_values if hasattr(self, '_m_flag_1_values') else None

                if self.tag_enum == Elf.DynamicArrayTags.flags_1:
                    if self._is_le:
                        self._m_flag_1_values = Elf.DtFlag1Values(self.value_or_ptr, self._io, self, self._root)
                    else:
                        self._m_flag_1_values = Elf.DtFlag1Values(self.value_or_ptr, self._io, self, self._root)

                return self._m_flag_1_values if hasattr(self, '_m_flag_1_values') else None


        class SectionHeader(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._is_le = _is_le
                self._read()

            def _read(self):
                if not hasattr(self, '_is_le'):
                    raise kaitaistruct.UndecidedEndiannessError("/types/endian_elf/types/section_header")
                elif self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()

            def _read_le(self):
                self.ofs_name = self._io.read_u4le()
                self.type = KaitaiStream.resolve_enum(Elf.ShType, self._io.read_u4le())
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.flags = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.flags = self._io.read_u8le()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.addr = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.addr = self._io.read_u8le()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.ofs_body = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.ofs_body = self._io.read_u8le()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.len_body = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.len_body = self._io.read_u8le()
                self.linked_section_idx = self._io.read_u4le()
                self.info = self._io.read_bytes(4)
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.align = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.align = self._io.read_u8le()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.entry_size = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.entry_size = self._io.read_u8le()

            def _read_be(self):
                self.ofs_name = self._io.read_u4be()
                self.type = KaitaiStream.resolve_enum(Elf.ShType, self._io.read_u4be())
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.flags = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.flags = self._io.read_u8be()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.addr = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.addr = self._io.read_u8be()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.ofs_body = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.ofs_body = self._io.read_u8be()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.len_body = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.len_body = self._io.read_u8be()
                self.linked_section_idx = self._io.read_u4be()
                self.info = self._io.read_bytes(4)
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.align = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.align = self._io.read_u8be()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.entry_size = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.entry_size = self._io.read_u8be()

            @property
            def body(self):
                if hasattr(self, '_m_body'):
                    return self._m_body if hasattr(self, '_m_body') else None

                io = self._root._io
                _pos = io.pos()
                io.seek(self.ofs_body)
                if self._is_le:
                    _on = self.type
                    if _on == Elf.ShType.strtab:
                        self._raw__m_body = io.read_bytes(self.len_body)
                        _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                        self._m_body = Elf.EndianElf.StringsStruct(_io__raw__m_body, self, self._root, self._is_le)
                    elif _on == Elf.ShType.dynamic:
                        self._raw__m_body = io.read_bytes(self.len_body)
                        _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                        self._m_body = Elf.EndianElf.DynamicSection(_io__raw__m_body, self, self._root, self._is_le)
                    elif _on == Elf.ShType.dynsym:
                        self._raw__m_body = io.read_bytes(self.len_body)
                        _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                        self._m_body = Elf.EndianElf.DynsymSection(_io__raw__m_body, self, self._root, self._is_le)
                    elif _on == Elf.ShType.dynstr:
                        self._raw__m_body = io.read_bytes(self.len_body)
                        _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                        self._m_body = Elf.EndianElf.StringsStruct(_io__raw__m_body, self, self._root, self._is_le)
                    else:
                        self._m_body = io.read_bytes(self.len_body)
                else:
                    _on = self.type
                    if _on == Elf.ShType.strtab:
                        self._raw__m_body = io.read_bytes(self.len_body)
                        _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                        self._m_body = Elf.EndianElf.StringsStruct(_io__raw__m_body, self, self._root, self._is_le)
                    elif _on == Elf.ShType.dynamic:
                        self._raw__m_body = io.read_bytes(self.len_body)
                        _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                        self._m_body = Elf.EndianElf.DynamicSection(_io__raw__m_body, self, self._root, self._is_le)
                    elif _on == Elf.ShType.dynsym:
                        self._raw__m_body = io.read_bytes(self.len_body)
                        _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                        self._m_body = Elf.EndianElf.DynsymSection(_io__raw__m_body, self, self._root, self._is_le)
                    elif _on == Elf.ShType.dynstr:
                        self._raw__m_body = io.read_bytes(self.len_body)
                        _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                        self._m_body = Elf.EndianElf.StringsStruct(_io__raw__m_body, self, self._root, self._is_le)
                    else:
                        self._m_body = io.read_bytes(self.len_body)
                io.seek(_pos)
                return self._m_body if hasattr(self, '_m_body') else None

            @property
            def name(self):
                if hasattr(self, '_m_name'):
                    return self._m_name if hasattr(self, '_m_name') else None

                io = self._root.header.strings._io
                _pos = io.pos()
                io.seek(self.ofs_name)
                if self._is_le:
                    self._m_name = (io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
                else:
                    self._m_name = (io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
                io.seek(_pos)
                return self._m_name if hasattr(self, '_m_name') else None

            @property
            def flags_obj(self):
                if hasattr(self, '_m_flags_obj'):
                    return self._m_flags_obj if hasattr(self, '_m_flags_obj') else None

                if self._is_le:
                    self._m_flags_obj = Elf.SectionHeaderFlags(self.flags, self._io, self, self._root)
                else:
                    self._m_flags_obj = Elf.SectionHeaderFlags(self.flags, self._io, self, self._root)
                return self._m_flags_obj if hasattr(self, '_m_flags_obj') else None


        class DynamicSection(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._is_le = _is_le
                self._read()

            def _read(self):
                if not hasattr(self, '_is_le'):
                    raise kaitaistruct.UndecidedEndiannessError("/types/endian_elf/types/dynamic_section")
                elif self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()

            def _read_le(self):
                self.entries = []
                i = 0
                while not self._io.is_eof():
                    self.entries.append(Elf.EndianElf.DynamicSectionEntry(self._io, self, self._root, self._is_le))
                    i += 1


            def _read_be(self):
                self.entries = []
                i = 0
                while not self._io.is_eof():
                    self.entries.append(Elf.EndianElf.DynamicSectionEntry(self._io, self, self._root, self._is_le))
                    i += 1



        class DynsymSection(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._is_le = _is_le
                self._read()

            def _read(self):
                if not hasattr(self, '_is_le'):
                    raise kaitaistruct.UndecidedEndiannessError("/types/endian_elf/types/dynsym_section")
                elif self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()

            def _read_le(self):
                self.entries = []
                i = 0
                while not self._io.is_eof():
                    _on = self._root.bits
                    if _on == Elf.Bits.b32:
                        self.entries.append(Elf.EndianElf.DynsymSectionEntry32(self._io, self, self._root, self._is_le))
                    elif _on == Elf.Bits.b64:
                        self.entries.append(Elf.EndianElf.DynsymSectionEntry64(self._io, self, self._root, self._is_le))
                    i += 1


            def _read_be(self):
                self.entries = []
                i = 0
                while not self._io.is_eof():
                    _on = self._root.bits
                    if _on == Elf.Bits.b32:
                        self.entries.append(Elf.EndianElf.DynsymSectionEntry32(self._io, self, self._root, self._is_le))
                    elif _on == Elf.Bits.b64:
                        self.entries.append(Elf.EndianElf.DynsymSectionEntry64(self._io, self, self._root, self._is_le))
                    i += 1



        class DynsymSectionEntry32(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._is_le = _is_le
                self._read()

            def _read(self):
                if not hasattr(self, '_is_le'):
                    raise kaitaistruct.UndecidedEndiannessError("/types/endian_elf/types/dynsym_section_entry32")
                elif self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()

            def _read_le(self):
                self.name_offset = self._io.read_u4le()
                self.value = self._io.read_u4le()
                self.size = self._io.read_u4le()
                self.info = self._io.read_u1()
                self.other = self._io.read_u1()
                self.shndx = self._io.read_u2le()

            def _read_be(self):
                self.name_offset = self._io.read_u4be()
                self.value = self._io.read_u4be()
                self.size = self._io.read_u4be()
                self.info = self._io.read_u1()
                self.other = self._io.read_u1()
                self.shndx = self._io.read_u2be()


        class StringsStruct(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._is_le = _is_le
                self._read()

            def _read(self):
                if not hasattr(self, '_is_le'):
                    raise kaitaistruct.UndecidedEndiannessError("/types/endian_elf/types/strings_struct")
                elif self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()

            def _read_le(self):
                self.entries = []
                i = 0
                while not self._io.is_eof():
                    self.entries.append((self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII"))
                    i += 1


            def _read_be(self):
                self.entries = []
                i = 0
                while not self._io.is_eof():
                    self.entries.append((self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII"))
                    i += 1



        @property
        def program_headers(self):
            if hasattr(self, '_m_program_headers'):
                return self._m_program_headers if hasattr(self, '_m_program_headers') else None

            _pos = self._io.pos()
            self._io.seek(self.program_header_offset)
            if self._is_le:
                self._raw__m_program_headers = [None] * (self.qty_program_header)
                self._m_program_headers = [None] * (self.qty_program_header)
                for i in range(self.qty_program_header):
                    self._raw__m_program_headers[i] = self._io.read_bytes(self.program_header_entry_size)
                    _io__raw__m_program_headers = KaitaiStream(BytesIO(self._raw__m_program_headers[i]))
                    self._m_program_headers[i] = Elf.EndianElf.ProgramHeader(_io__raw__m_program_headers, self, self._root, self._is_le)

            else:
                self._raw__m_program_headers = [None] * (self.qty_program_header)
                self._m_program_headers = [None] * (self.qty_program_header)
                for i in range(self.qty_program_header):
                    self._raw__m_program_headers[i] = self._io.read_bytes(self.program_header_entry_size)
                    _io__raw__m_program_headers = KaitaiStream(BytesIO(self._raw__m_program_headers[i]))
                    self._m_program_headers[i] = Elf.EndianElf.ProgramHeader(_io__raw__m_program_headers, self, self._root, self._is_le)

            self._io.seek(_pos)
            return self._m_program_headers if hasattr(self, '_m_program_headers') else None

        @property
        def section_headers(self):
            if hasattr(self, '_m_section_headers'):
                return self._m_section_headers if hasattr(self, '_m_section_headers') else None

            _pos = self._io.pos()
            self._io.seek(self.section_header_offset)
            if self._is_le:
                self._raw__m_section_headers = [None] * (self.qty_section_header)
                self._m_section_headers = [None] * (self.qty_section_header)
                for i in range(self.qty_section_header):
                    self._raw__m_section_headers[i] = self._io.read_bytes(self.section_header_entry_size)
                    _io__raw__m_section_headers = KaitaiStream(BytesIO(self._raw__m_section_headers[i]))
                    self._m_section_headers[i] = Elf.EndianElf.SectionHeader(_io__raw__m_section_headers, self, self._root, self._is_le)

            else:
                self._raw__m_section_headers = [None] * (self.qty_section_header)
                self._m_section_headers = [None] * (self.qty_section_header)
                for i in range(self.qty_section_header):
                    self._raw__m_section_headers[i] = self._io.read_bytes(self.section_header_entry_size)
                    _io__raw__m_section_headers = KaitaiStream(BytesIO(self._raw__m_section_headers[i]))
                    self._m_section_headers[i] = Elf.EndianElf.SectionHeader(_io__raw__m_section_headers, self, self._root, self._is_le)

            self._io.seek(_pos)
            return self._m_section_headers if hasattr(self, '_m_section_headers') else None

        @property
        def strings(self):
            if hasattr(self, '_m_strings'):
                return self._m_strings if hasattr(self, '_m_strings') else None

            _pos = self._io.pos()
            self._io.seek(self.section_headers[self.section_names_idx].ofs_body)
            if self._is_le:
                self._raw__m_strings = self._io.read_bytes(self.section_headers[self.section_names_idx].len_body)
                _io__raw__m_strings = KaitaiStream(BytesIO(self._raw__m_strings))
                self._m_strings = Elf.EndianElf.StringsStruct(_io__raw__m_strings, self, self._root, self._is_le)
            else:
                self._raw__m_strings = self._io.read_bytes(self.section_headers[self.section_names_idx].len_body)
                _io__raw__m_strings = KaitaiStream(BytesIO(self._raw__m_strings))
                self._m_strings = Elf.EndianElf.StringsStruct(_io__raw__m_strings, self, self._root, self._is_le)
            self._io.seek(_pos)
            return self._m_strings if hasattr(self, '_m_strings') else None



