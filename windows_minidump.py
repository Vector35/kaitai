# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class WindowsMinidump(KaitaiStruct):
    """Windows MiniDump (MDMP) file provides a concise way to store process
    core dumps, which is useful for debugging. Given its small size,
    modularity, some cross-platform features and native support in some
    debuggers, it is particularly useful for crash reporting, and is
    used for that purpose in Windows and Google Chrome projects.
    
    The file itself is a container, which contains a number of typed
    "streams", which contain some data according to its type attribute.
    
    .. seealso::
       Source - https://msdn.microsoft.com/en-us/library/ms680378(VS.85).aspx
    """

    class StreamTypes(Enum):
        unused = 0
        reserved_0 = 1
        reserved_1 = 2
        thread_list = 3
        module_list = 4
        memory_list = 5
        exception = 6
        system_info = 7
        thread_ex_list = 8
        memory_64_list = 9
        comment_a = 10
        comment_w = 11
        handle_data = 12
        function_table = 13
        unloaded_module_list = 14
        misc_info = 15
        memory_info_list = 16
        thread_info_list = 17
        handle_operation_list = 18
        token = 19
        java_script_data = 20
        system_memory_info = 21
        process_vm_vounters = 22
        ipt_trace = 23
        thread_names = 24
        ce_null = 32768
        ce_system_info = 32769
        ce_exception = 32770
        ce_module_list = 32771
        ce_process_list = 32772
        ce_thread_list = 32773
        ce_thread_context_list = 32774
        ce_thread_call_stack_list = 32775
        ce_memory_virtual_list = 32776
        ce_memory_physical_list = 32777
        ce_bucket_parameters = 32778
        ce_process_module_map = 32779
        ce_diagnosis_list = 32780
        md_crashpad_info_stream = 1129316353
        md_raw_breakpad_info = 1197932545
        md_raw_assertion_info = 1197932546
        md_linux_cpu_info = 1197932547
        md_linux_proc_status = 1197932548
        md_linux_lsb_release = 1197932549
        md_linux_cmd_line = 1197932550
        md_linux_environ = 1197932551
        md_linux_auxv = 1197932552
        md_linux_maps = 1197932553
        md_linux_dso_debug = 1197932554
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic1 = self._io.read_bytes(4)
        if not self.magic1 == b"\x4D\x44\x4D\x50":
            raise kaitaistruct.ValidationNotEqualError(b"\x4D\x44\x4D\x50", self.magic1, self._io, u"/seq/0")
        self.magic2 = self._io.read_bytes(2)
        if not self.magic2 == b"\x93\xA7":
            raise kaitaistruct.ValidationNotEqualError(b"\x93\xA7", self.magic2, self._io, u"/seq/1")
        self.version = self._io.read_u2le()
        self.num_streams = self._io.read_u4le()
        self.ofs_streams = self._io.read_u4le()
        self.checksum = self._io.read_u4le()
        self.timestamp = self._io.read_u4le()
        self.flags = self._io.read_u8le()

    class ThreadList(KaitaiStruct):
        """
        .. seealso::
           Source - https://msdn.microsoft.com/en-us/library/ms680515(v=vs.85).aspx
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_threads = self._io.read_u4le()
            self.threads = [None] * (self.num_threads)
            for i in range(self.num_threads):
                self.threads[i] = WindowsMinidump.Thread(self._io, self, self._root)



    class LocationDescriptor(KaitaiStruct):
        """
        .. seealso::
           Source - https://msdn.microsoft.com/en-us/library/ms680383(v=vs.85).aspx
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len_data = self._io.read_u4le()
            self.ofs_data = self._io.read_u4le()

        @property
        def data(self):
            if hasattr(self, '_m_data'):
                return self._m_data if hasattr(self, '_m_data') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.ofs_data)
            self._m_data = io.read_bytes(self.len_data)
            io.seek(_pos)
            return self._m_data if hasattr(self, '_m_data') else None


    class MinidumpString(KaitaiStruct):
        """Specific string serialization scheme used in MiniDump format is
        actually a simple 32-bit length-prefixed UTF-16 string.
        
        .. seealso::
           Source - https://msdn.microsoft.com/en-us/library/ms680395(v=vs.85).aspx
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len_str = self._io.read_u4le()
            self.str = (self._io.read_bytes(self.len_str)).decode(u"UTF-16LE")


    class SystemInfo(KaitaiStruct):
        """"System info" stream provides basic information about the
        hardware and operating system which produces this dump.
        
        .. seealso::
           Source - https://msdn.microsoft.com/en-us/library/ms680396(v=vs.85).aspx
        """

        class CpuArchs(Enum):
            intel = 0
            arm = 5
            ia64 = 6
            amd64 = 9
            unknown = 65535
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.cpu_arch = KaitaiStream.resolve_enum(WindowsMinidump.SystemInfo.CpuArchs, self._io.read_u2le())
            self.cpu_level = self._io.read_u2le()
            self.cpu_revision = self._io.read_u2le()
            self.num_cpus = self._io.read_u1()
            self.os_type = self._io.read_u1()
            self.os_ver_major = self._io.read_u4le()
            self.os_ver_minor = self._io.read_u4le()
            self.os_build = self._io.read_u4le()
            self.os_platform = self._io.read_u4le()
            self.ofs_service_pack = self._io.read_u4le()
            self.os_suite_mask = self._io.read_u2le()
            self.reserved2 = self._io.read_u2le()

        @property
        def service_pack(self):
            if hasattr(self, '_m_service_pack'):
                return self._m_service_pack if hasattr(self, '_m_service_pack') else None

            if self.ofs_service_pack > 0:
                io = self._root._io
                _pos = io.pos()
                io.seek(self.ofs_service_pack)
                self._m_service_pack = WindowsMinidump.MinidumpString(io, self, self._root)
                io.seek(_pos)

            return self._m_service_pack if hasattr(self, '_m_service_pack') else None


    class ExceptionRecord(KaitaiStruct):
        """
        .. seealso::
           Source - https://msdn.microsoft.com/en-us/library/ms680367(v=vs.85).aspx
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.code = self._io.read_u4le()
            self.flags = self._io.read_u4le()
            self.inner_exception = self._io.read_u8le()
            self.addr = self._io.read_u8le()
            self.num_params = self._io.read_u4le()
            self.reserved = self._io.read_u4le()
            self.params = [None] * (15)
            for i in range(15):
                self.params[i] = self._io.read_u8le()



    class MiscInfo(KaitaiStruct):
        """
        .. seealso::
           Source - https://msdn.microsoft.com/en-us/library/ms680389(v=vs.85).aspx
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len_info = self._io.read_u4le()
            self.flags1 = self._io.read_u4le()
            self.process_id = self._io.read_u4le()
            self.process_create_time = self._io.read_u4le()
            self.process_user_time = self._io.read_u4le()
            self.process_kernel_time = self._io.read_u4le()
            self.cpu_max_mhz = self._io.read_u4le()
            self.cpu_cur_mhz = self._io.read_u4le()
            self.cpu_limit_mhz = self._io.read_u4le()
            self.cpu_max_idle_state = self._io.read_u4le()
            self.cpu_cur_idle_state = self._io.read_u4le()


    class Dir(KaitaiStruct):
        """
        .. seealso::
           Source - https://msdn.microsoft.com/en-us/library/ms680365(v=vs.85).aspx
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.stream_type = KaitaiStream.resolve_enum(WindowsMinidump.StreamTypes, self._io.read_u4le())
            self.len_data = self._io.read_u4le()
            self.ofs_data = self._io.read_u4le()

        @property
        def data(self):
            if hasattr(self, '_m_data'):
                return self._m_data if hasattr(self, '_m_data') else None

            _pos = self._io.pos()
            self._io.seek(self.ofs_data)
            _on = self.stream_type
            if _on == WindowsMinidump.StreamTypes.memory_list:
                self._raw__m_data = self._io.read_bytes(self.len_data)
                _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                self._m_data = WindowsMinidump.MemoryList(_io__raw__m_data, self, self._root)
            elif _on == WindowsMinidump.StreamTypes.misc_info:
                self._raw__m_data = self._io.read_bytes(self.len_data)
                _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                self._m_data = WindowsMinidump.MiscInfo(_io__raw__m_data, self, self._root)
            elif _on == WindowsMinidump.StreamTypes.thread_list:
                self._raw__m_data = self._io.read_bytes(self.len_data)
                _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                self._m_data = WindowsMinidump.ThreadList(_io__raw__m_data, self, self._root)
            elif _on == WindowsMinidump.StreamTypes.exception:
                self._raw__m_data = self._io.read_bytes(self.len_data)
                _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                self._m_data = WindowsMinidump.ExceptionStream(_io__raw__m_data, self, self._root)
            elif _on == WindowsMinidump.StreamTypes.system_info:
                self._raw__m_data = self._io.read_bytes(self.len_data)
                _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                self._m_data = WindowsMinidump.SystemInfo(_io__raw__m_data, self, self._root)
            else:
                self._m_data = self._io.read_bytes(self.len_data)
            self._io.seek(_pos)
            return self._m_data if hasattr(self, '_m_data') else None


    class Thread(KaitaiStruct):
        """
        .. seealso::
           Source - https://msdn.microsoft.com/en-us/library/ms680517(v=vs.85).aspx
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.thread_id = self._io.read_u4le()
            self.suspend_count = self._io.read_u4le()
            self.priority_class = self._io.read_u4le()
            self.priority = self._io.read_u4le()
            self.teb = self._io.read_u8le()
            self.stack = WindowsMinidump.MemoryDescriptor(self._io, self, self._root)
            self.thread_context = WindowsMinidump.LocationDescriptor(self._io, self, self._root)


    class MemoryList(KaitaiStruct):
        """
        .. seealso::
           Source - https://msdn.microsoft.com/en-us/library/ms680387(v=vs.85).aspx
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_mem_ranges = self._io.read_u4le()
            self.mem_ranges = [None] * (self.num_mem_ranges)
            for i in range(self.num_mem_ranges):
                self.mem_ranges[i] = WindowsMinidump.MemoryDescriptor(self._io, self, self._root)



    class MemoryDescriptor(KaitaiStruct):
        """
        .. seealso::
           Source - https://msdn.microsoft.com/en-us/library/ms680384(v=vs.85).aspx
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.addr_memory_range = self._io.read_u8le()
            self.memory = WindowsMinidump.LocationDescriptor(self._io, self, self._root)


    class ExceptionStream(KaitaiStruct):
        """
        .. seealso::
           Source - https://msdn.microsoft.com/en-us/library/ms680368(v=vs.85).aspx
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.thread_id = self._io.read_u4le()
            self.reserved = self._io.read_u4le()
            self.exception_rec = WindowsMinidump.ExceptionRecord(self._io, self, self._root)
            self.thread_context = WindowsMinidump.LocationDescriptor(self._io, self, self._root)


    @property
    def streams(self):
        if hasattr(self, '_m_streams'):
            return self._m_streams if hasattr(self, '_m_streams') else None

        _pos = self._io.pos()
        self._io.seek(self.ofs_streams)
        self._m_streams = [None] * (self.num_streams)
        for i in range(self.num_streams):
            self._m_streams[i] = WindowsMinidump.Dir(self._io, self, self._root)

        self._io.seek(_pos)
        return self._m_streams if hasattr(self, '_m_streams') else None


