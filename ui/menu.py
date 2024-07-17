import sys

from binaryninjaui import ContextMenuManager, Menu, UIActionHandler, UIAction
import binaryninjaui

from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette
from PySide6.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QGroupBox, QTreeWidget, QTreeWidgetItem, QLineEdit, QHeaderView, QLabel, QMenu, QHBoxLayout


class KaitaiOptionsWidget(QLabel):
    def __init__(self, parent):
        QLabel.__init__(self, parent)

        self.kv = parent

        self.setBackgroundRole(QPalette.Highlight)
        self.setForegroundRole(QPalette.WindowText)
        self.setText(" Kaitai Formats ▾ ")

        # see api/ui/menus.h
        self.contextMenuManager = ContextMenuManager(self)

        self.menu = Menu()
        self.action_handler = UIActionHandler()
        self.registerActions()
        self.addActions()
        self.bindActions()

    def registerActions(self):
        # add all action handlers
        UIAction.registerAction("archive\\cpio_old_le")
        UIAction.registerAction("archive\\gzip")
        UIAction.registerAction("archive\\lzh")
        UIAction.registerAction("archive\\rar")
        UIAction.registerAction("archive\\zip")
        UIAction.registerAction("cad\\monomakh_sapr_chg")
        UIAction.registerAction("common\\bcd")
        UIAction.registerAction("database\\dbf")
        UIAction.registerAction("database\\gettext_mo")
        UIAction.registerAction("database\\sqlite3")
        UIAction.registerAction("database\\tsm")
        UIAction.registerAction("executable\\dex")
        UIAction.registerAction("executable\\dos_mz")
        UIAction.registerAction("executable\\elf")
        UIAction.registerAction("executable\\java_class")
        UIAction.registerAction("executable\\mach_o")
        UIAction.registerAction("executable\\microsoft_pe")
        UIAction.registerAction("executable\\python_pyc_27")
        UIAction.registerAction("executable\\swf")
        UIAction.registerAction("filesystem\\apm_partition_table")
        UIAction.registerAction("filesystem\\apple_single_double")
        UIAction.registerAction("filesystem\\cramfs")
        UIAction.registerAction("filesystem\\ext2")
        UIAction.registerAction("filesystem\\gpt_partition_table")
        UIAction.registerAction("filesystem\\iso9660")
        UIAction.registerAction("filesystem\\luks")
        UIAction.registerAction("filesystem\\lvm2")
        UIAction.registerAction("filesystem\\mbr_partition_table")
        UIAction.registerAction("filesystem\\tr_dos_image")
        UIAction.registerAction("filesystem\\vdi")
        UIAction.registerAction("filesystem\\vfat")
        UIAction.registerAction("filesystem\\vmware_vmdk")
        UIAction.registerAction("firmware\\andes_firmware")
        UIAction.registerAction("firmware\\ines")
        UIAction.registerAction("firmware\\uimage")
        UIAction.registerAction("font\\ttf")
        UIAction.registerAction("game\\allegro_dat")
        UIAction.registerAction("game\\doom_wad")
        UIAction.registerAction("game\\dune_2_pak")
        UIAction.registerAction("game\\fallout_dat")
        UIAction.registerAction("game\\ftl_dat")
        UIAction.registerAction("game\\gran_turismo_vol")
        UIAction.registerAction("game\\heaps_pak")
        UIAction.registerAction("game\\heroes_of_might_and_magic_agg")
        UIAction.registerAction("game\\heroes_of_might_and_magic_bmp")
        UIAction.registerAction("game\\quake_mdl")
        UIAction.registerAction("game\\quake_pak")
        UIAction.registerAction("game\\renderware_binary_stream")
        UIAction.registerAction("game\\saints_row_2_vpp_pc")
        UIAction.registerAction("game\\warcraft_2_pud")
        UIAction.registerAction("geospatial\\shapefile_index")
        UIAction.registerAction("geospatial\\shapefile_main")
        UIAction.registerAction("hardware\\edid")
        UIAction.registerAction("hardware\\mifare\\mifare_classic")
        UIAction.registerAction("image\\bmp")
        UIAction.registerAction("image\\dicom")
        UIAction.registerAction("image\\exif")
        UIAction.registerAction("image\\exif_be")
        UIAction.registerAction("image\\exif_le")
        UIAction.registerAction("image\\gif")
        UIAction.registerAction("image\\icc_4")
        UIAction.registerAction("image\\ico")
        UIAction.registerAction("image\\jpeg")
        UIAction.registerAction("image\\pcx")
        UIAction.registerAction("image\\pcx_dcx")
        UIAction.registerAction("image\\png")
        UIAction.registerAction("image\\psx_tim")
        UIAction.registerAction("image\\tga")
        UIAction.registerAction("image\\wmf")
        UIAction.registerAction("image\\xwd")
        UIAction.registerAction("log\\aix_utmp")
        UIAction.registerAction("log\\glibc_utmp")
        UIAction.registerAction("log\\systemd_journal")
        UIAction.registerAction("log\\windows_evt_log")
        UIAction.registerAction("machine_code\\code_6502")
        UIAction.registerAction("media\\avi")
        UIAction.registerAction("media\\blender_blend")
        UIAction.registerAction("media\\creative_voice_file")
        UIAction.registerAction("media\\genmidi_op2")
        UIAction.registerAction("media\\id3v1_1")
        UIAction.registerAction("media\\id3v2_3")
        UIAction.registerAction("media\\id3v2_4")
        UIAction.registerAction("media\\magicavoxel_vox")
        UIAction.registerAction("media\\ogg")
        UIAction.registerAction("media\\quicktime_mov")
        UIAction.registerAction("media\\standard_midi_file")
        UIAction.registerAction("media\\stl")
        UIAction.registerAction("media\\tracker_modules\\fasttracker_xm_module")
        UIAction.registerAction("media\\tracker_modules\\s3m")
        UIAction.registerAction("media\\vp8_ivf")
        UIAction.registerAction("media\\wav")
        UIAction.registerAction("network\\bitcoin_transaction")
        UIAction.registerAction("network\\dns_packet")
        UIAction.registerAction("network\\hccap")
        UIAction.registerAction("network\\hccapx")
        UIAction.registerAction("network\\icmp_packet")

        UIAction.registerAction("network\\ethernet_frame")
        UIAction.registerAction("network\\ipv4_packet")
        UIAction.registerAction("network\\ipv6_packet")
        UIAction.registerAction("network\\microsoft_network_monitor_v2")
        UIAction.registerAction("network\\packet_ppi")
        UIAction.registerAction("network\\pcap")
        UIAction.registerAction("network\\protocol_body")

        UIAction.registerAction("network\\rtcp_payload")
        UIAction.registerAction("network\\rtp_packet")
        UIAction.registerAction("network\\tcp_segment")
        UIAction.registerAction("network\\tls_client_hello")
        UIAction.registerAction("network\\udp_datagram")
        UIAction.registerAction("network\\windows_systemtime")
        UIAction.registerAction("scientific\\nt_mdt\\nt_mdt")
        UIAction.registerAction("scientific\\nt_mdt\\nt_mdt_pal")
        UIAction.registerAction("scientific\\spectroscopy\\avantes_roh60")
        UIAction.registerAction("scientific\\spectroscopy\\specpr")
        UIAction.registerAction("security\\openpgp_message")
        UIAction.registerAction("security\\ssh_public_key")
        UIAction.registerAction("serialization\\asn1\\asn1_der")
        UIAction.registerAction("serialization\\bson")
        UIAction.registerAction("serialization\\google_protobuf")
        UIAction.registerAction("serialization\\microsoft_cfb")
        UIAction.registerAction("serialization\\msgpack")
        UIAction.registerAction("serialization\\ruby_marshal")
        UIAction.registerAction("windows\\regf")
        UIAction.registerAction("windows\\windows_lnk_file")
        UIAction.registerAction("windows\\windows_minidump")
        UIAction.registerAction("windows\\windows_resource_file")
        UIAction.registerAction("windows\\windows_shell_items")
        UIAction.registerAction("windows\\windows_systemtime")

    def addActions(self):
        self.menu.addAction("archive\\cpio_old_le", "formats")
        self.menu.addAction("archive\\gzip", "formats")
        self.menu.addAction("archive\\lzh", "formats")
        self.menu.addAction("archive\\rar", "formats")
        self.menu.addAction("archive\\zip", "formats")
        self.menu.addAction("cad\\monomakh_sapr_chg", "formats")
        self.menu.addAction("common\\bcd", "formats")
        self.menu.addAction("database\\dbf", "formats")
        self.menu.addAction("database\\gettext_mo", "formats")
        self.menu.addAction("database\\sqlite3", "formats")
        self.menu.addAction("database\\tsm", "formats")
        self.menu.addAction("executable\\dex", "formats")
        self.menu.addAction("executable\\dos_mz", "formats")
        self.menu.addAction("executable\\elf", "formats")
        self.menu.addAction("executable\\java_class", "formats")
        self.menu.addAction("executable\\mach_o", "formats")
        self.menu.addAction("executable\\microsoft_pe", "formats")
        self.menu.addAction("executable\\python_pyc_27", "formats")
        self.menu.addAction("executable\\swf", "formats")
        self.menu.addAction("filesystem\\apm_partition_table", "formats")
        self.menu.addAction("filesystem\\apple_single_double", "formats")
        self.menu.addAction("filesystem\\cramfs", "formats")
        self.menu.addAction("filesystem\\ext2", "formats")
        self.menu.addAction("filesystem\\gpt_partition_table", "formats")
        self.menu.addAction("filesystem\\iso9660", "formats")
        self.menu.addAction("filesystem\\luks", "formats")
        self.menu.addAction("filesystem\\lvm2", "formats")
        self.menu.addAction("filesystem\\mbr_partition_table", "formats")
        self.menu.addAction("filesystem\\tr_dos_image", "formats")
        self.menu.addAction("filesystem\\vdi", "formats")
        self.menu.addAction("filesystem\\vfat", "formats")
        self.menu.addAction("filesystem\\vmware_vmdk", "formats")
        self.menu.addAction("firmware\\andes_firmware", "formats")
        self.menu.addAction("firmware\\ines", "formats")
        self.menu.addAction("firmware\\uimage", "formats")
        self.menu.addAction("font\\ttf", "formats")
        self.menu.addAction("game\\allegro_dat", "formats")
        self.menu.addAction("game\\doom_wad", "formats")
        self.menu.addAction("game\\dune_2_pak", "formats")
        self.menu.addAction("game\\fallout_dat", "formats")
        self.menu.addAction("game\\ftl_dat", "formats")
        self.menu.addAction("game\\gran_turismo_vol", "formats")
        self.menu.addAction("game\\heaps_pak", "formats")
        self.menu.addAction("game\\heroes_of_might_and_magic_agg", "formats")
        self.menu.addAction("game\\heroes_of_might_and_magic_bmp", "formats")
        self.menu.addAction("game\\quake_mdl", "formats")
        self.menu.addAction("game\\quake_pak", "formats")
        self.menu.addAction("game\\renderware_binary_stream", "formats")
        self.menu.addAction("game\\saints_row_2_vpp_pc", "formats")
        self.menu.addAction("game\\warcraft_2_pud", "formats")
        self.menu.addAction("geospatial\\shapefile_index", "formats")
        self.menu.addAction("geospatial\\shapefile_main", "formats")
        self.menu.addAction("hardware\\edid", "formats")
        self.menu.addAction("hardware\\mifare\\mifare_classic", "formats")
        self.menu.addAction("image\\bmp", "formats")
        self.menu.addAction("image\\dicom", "formats")
        self.menu.addAction("image\\exif", "formats")
        self.menu.addAction("image\\exif_be", "formats")
        self.menu.addAction("image\\exif_le", "formats")
        self.menu.addAction("image\\gif", "formats")
        self.menu.addAction("image\\icc_4", "formats")
        self.menu.addAction("image\\ico", "formats")
        self.menu.addAction("image\\jpeg", "formats")
        self.menu.addAction("image\\pcx", "formats")
        self.menu.addAction("image\\pcx_dcx", "formats")
        self.menu.addAction("image\\png", "formats")
        self.menu.addAction("image\\psx_tim", "formats")
        self.menu.addAction("image\\tga", "formats")
        self.menu.addAction("image\\wmf", "formats")
        self.menu.addAction("image\\xwd", "formats")
        self.menu.addAction("log\\aix_utmp", "formats")
        self.menu.addAction("log\\glibc_utmp", "formats")
        self.menu.addAction("log\\systemd_journal", "formats")
        self.menu.addAction("log\\windows_evt_log", "formats")
        self.menu.addAction("machine_code\\code_6502", "formats")
        self.menu.addAction("media\\avi", "formats")
        self.menu.addAction("media\\blender_blend", "formats")
        self.menu.addAction("media\\creative_voice_file", "formats")
        self.menu.addAction("media\\genmidi_op2", "formats")
        self.menu.addAction("media\\id3v1_1", "formats")
        self.menu.addAction("media\\id3v2_3", "formats")
        self.menu.addAction("media\\id3v2_4", "formats")
        self.menu.addAction("media\\magicavoxel_vox", "formats")
        self.menu.addAction("media\\ogg", "formats")
        self.menu.addAction("media\\quicktime_mov", "formats")
        self.menu.addAction("media\\standard_midi_file", "formats")
        self.menu.addAction("media\\stl", "formats")
        self.menu.addAction("media\\tracker_modules\\fasttracker_xm_module", "formats")
        self.menu.addAction("media\\tracker_modules\\s3m", "formats")
        self.menu.addAction("media\\vp8_ivf", "formats")
        self.menu.addAction("media\\wav", "formats")
        self.menu.addAction("network\\bitcoin_transaction", "formats")
        self.menu.addAction("network\\dns_packet", "formats")
        self.menu.addAction("network\\hccap", "formats")
        self.menu.addAction("network\\hccapx", "formats")
        self.menu.addAction("network\\icmp_packet", "formats")

        if sys.version_info[0] == 3:
            self.menu.addAction("network\\ethernet_frame", "formats")
            self.menu.addAction("network\\ipv4_packet", "formats")
            self.menu.addAction("network\\ipv6_packet", "formats")
            self.menu.addAction("network\\microsoft_network_monitor_v2", "formats")
            self.menu.addAction("network\\packet_ppi", "formats")
            self.menu.addAction("network\\pcap", "formats")
            self.menu.addAction("network\\protocol_body", "formats")

        self.menu.addAction("network\\rtcp_payload", "formats")
        self.menu.addAction("network\\rtp_packet", "formats")
        self.menu.addAction("network\\tcp_segment", "formats")
        self.menu.addAction("network\\tls_client_hello", "formats")
        self.menu.addAction("network\\udp_datagram", "formats")
        self.menu.addAction("network\\windows_systemtime", "formats")
        self.menu.addAction("scientific\\nt_mdt\\nt_mdt", "formats")
        self.menu.addAction("scientific\\nt_mdt\\nt_mdt_pal", "formats")
        self.menu.addAction("scientific\\spectroscopy\\avantes_roh60", "formats")
        self.menu.addAction("scientific\\spectroscopy\\specpr", "formats")
        self.menu.addAction("security\\openpgp_message", "formats")
        self.menu.addAction("security\\ssh_public_key", "formats")
        self.menu.addAction("serialization\\asn1\\asn1_der", "formats")
        self.menu.addAction("serialization\\bson", "formats")
        self.menu.addAction("serialization\\google_protobuf", "formats")
        self.menu.addAction("serialization\\microsoft_cfb", "formats")
        self.menu.addAction("serialization\\msgpack", "formats")
        self.menu.addAction("serialization\\ruby_marshal", "formats")
        self.menu.addAction("windows\\regf", "formats")
        self.menu.addAction("windows\\windows_lnk_file", "formats")
        self.menu.addAction("windows\\windows_minidump", "formats")
        self.menu.addAction("windows\\windows_resource_file", "formats")
        self.menu.addAction("windows\\windows_shell_items", "formats")
        self.menu.addAction("windows\\windows_systemtime", "formats")

    def bindActions(self):
        self.action_handler.bindAction("archive\\cpio_old_le", UIAction(self.on_cpio_old_le))
        self.action_handler.bindAction("archive\\gzip", UIAction(self.on_gzip))
        self.action_handler.bindAction("archive\\lzh", UIAction(self.on_lzh))
        self.action_handler.bindAction("archive\\rar", UIAction(self.on_rar))
        self.action_handler.bindAction("archive\\zip", UIAction(self.on_zip))
        self.action_handler.bindAction("cad\\monomakh_sapr_chg", UIAction(self.on_monomakh_sapr_chg))
        self.action_handler.bindAction("common\\bcd", UIAction(self.on_bcd))
        self.action_handler.bindAction("database\\dbf", UIAction(self.on_dbf))
        self.action_handler.bindAction("database\\gettext_mo", UIAction(self.on_gettext_mo))
        self.action_handler.bindAction("database\\sqlite3", UIAction(self.on_sqlite3))
        self.action_handler.bindAction("database\\tsm", UIAction(self.on_tsm))
        self.action_handler.bindAction("executable\\dex", UIAction(self.on_dex))
        self.action_handler.bindAction("executable\\dos_mz", UIAction(self.on_dos_mz))
        self.action_handler.bindAction("executable\\elf", UIAction(self.on_elf))
        self.action_handler.bindAction("executable\\java_class", UIAction(self.on_java_class))
        self.action_handler.bindAction("executable\\mach_o", UIAction(self.on_mach_o))
        self.action_handler.bindAction("executable\\microsoft_pe", UIAction(self.on_microsoft_pe))
        self.action_handler.bindAction("executable\\python_pyc_27", UIAction(self.on_python_pyc_27))
        self.action_handler.bindAction("executable\\swf", UIAction(self.on_swf))
        self.action_handler.bindAction("filesystem\\apm_partition_table", UIAction(self.on_apm_partition_table))
        self.action_handler.bindAction("filesystem\\apple_single_double", UIAction(self.on_apple_single_double))
        self.action_handler.bindAction("filesystem\\cramfs", UIAction(self.on_cramfs))
        self.action_handler.bindAction("filesystem\\ext2", UIAction(self.on_ext2))
        self.action_handler.bindAction("filesystem\\gpt_partition_table", UIAction(self.on_gpt_partition_table))
        self.action_handler.bindAction("filesystem\\iso9660", UIAction(self.on_iso9660))
        self.action_handler.bindAction("filesystem\\luks", UIAction(self.on_luks))
        self.action_handler.bindAction("filesystem\\lvm2", UIAction(self.on_lvm2))
        self.action_handler.bindAction("filesystem\\mbr_partition_table", UIAction(self.on_mbr_partition_table))
        self.action_handler.bindAction("filesystem\\tr_dos_image", UIAction(self.on_tr_dos_image))
        self.action_handler.bindAction("filesystem\\vdi", UIAction(self.on_vdi))
        self.action_handler.bindAction("filesystem\\vfat", UIAction(self.on_vfat))
        self.action_handler.bindAction("filesystem\\vmware_vmdk", UIAction(self.on_vmware_vmdk))
        self.action_handler.bindAction("firmware\\andes_firmware", UIAction(self.on_andes_firmware))
        self.action_handler.bindAction("firmware\\ines", UIAction(self.on_ines))
        self.action_handler.bindAction("firmware\\uimage", UIAction(self.on_uimage))
        self.action_handler.bindAction("font\\ttf", UIAction(self.on_ttf))
        self.action_handler.bindAction("game\\allegro_dat", UIAction(self.on_allegro_dat))
        self.action_handler.bindAction("game\\doom_wad", UIAction(self.on_doom_wad))
        self.action_handler.bindAction("game\\dune_2_pak", UIAction(self.on_dune_2_pak))
        self.action_handler.bindAction("game\\fallout_dat", UIAction(self.on_fallout_dat))
        self.action_handler.bindAction("game\\ftl_dat", UIAction(self.on_ftl_dat))
        self.action_handler.bindAction("game\\gran_turismo_vol", UIAction(self.on_gran_turismo_vol))
        self.action_handler.bindAction("game\\heaps_pak", UIAction(self.on_heaps_pak))
        self.action_handler.bindAction("game\\heroes_of_might_and_magic_agg", UIAction(self.on_heroes_of_might_and_magic_agg))
        self.action_handler.bindAction("game\\heroes_of_might_and_magic_bmp", UIAction(self.on_heroes_of_might_and_magic_bmp))
        self.action_handler.bindAction("game\\quake_mdl", UIAction(self.on_quake_mdl))
        self.action_handler.bindAction("game\\quake_pak", UIAction(self.on_quake_pak))
        self.action_handler.bindAction("game\\renderware_binary_stream", UIAction(self.on_renderware_binary_stream))
        self.action_handler.bindAction("game\\saints_row_2_vpp_pc", UIAction(self.on_saints_row_2_vpp_pc))
        self.action_handler.bindAction("game\\warcraft_2_pud", UIAction(self.on_warcraft_2_pud))
        self.action_handler.bindAction("geospatial\\shapefile_index", UIAction(self.on_shapefile_index))
        self.action_handler.bindAction("geospatial\\shapefile_main", UIAction(self.on_shapefile_main))
        self.action_handler.bindAction("hardware\\edid", UIAction(self.on_edid))
        self.action_handler.bindAction("hardware\\mifare\\mifare_classic", UIAction(self.on_mifare_classic))
        self.action_handler.bindAction("image\\bmp", UIAction(self.on_bmp))
        self.action_handler.bindAction("image\\dicom", UIAction(self.on_dicom))
        self.action_handler.bindAction("image\\exif", UIAction(self.on_exif))
        self.action_handler.bindAction("image\\exif_be", UIAction(self.on_exif_be))
        self.action_handler.bindAction("image\\exif_le", UIAction(self.on_exif_le))
        self.action_handler.bindAction("image\\gif", UIAction(self.on_gif))
        self.action_handler.bindAction("image\\icc_4", UIAction(self.on_icc_4))
        self.action_handler.bindAction("image\\ico", UIAction(self.on_ico))
        self.action_handler.bindAction("image\\jpeg", UIAction(self.on_jpeg))
        self.action_handler.bindAction("image\\pcx", UIAction(self.on_pcx))
        self.action_handler.bindAction("image\\pcx_dcx", UIAction(self.on_pcx_dcx))
        self.action_handler.bindAction("image\\png", UIAction(self.on_png))
        self.action_handler.bindAction("image\\psx_tim", UIAction(self.on_psx_tim))
        self.action_handler.bindAction("image\\tga", UIAction(self.on_tga))
        self.action_handler.bindAction("image\\wmf", UIAction(self.on_wmf))
        self.action_handler.bindAction("image\\xwd", UIAction(self.on_xwd))
        self.action_handler.bindAction("log\\aix_utmp", UIAction(self.on_aix_utmp))
        self.action_handler.bindAction("log\\glibc_utmp", UIAction(self.on_glibc_utmp))
        self.action_handler.bindAction("log\\systemd_journal", UIAction(self.on_systemd_journal))
        self.action_handler.bindAction("log\\windows_evt_log", UIAction(self.on_windows_evt_log))
        self.action_handler.bindAction("machine_code\\code_6502", UIAction(self.on_code_6502))
        self.action_handler.bindAction("media\\avi", UIAction(self.on_avi))
        self.action_handler.bindAction("media\\blender_blend", UIAction(self.on_blender_blend))
        self.action_handler.bindAction("media\\creative_voice_file", UIAction(self.on_creative_voice_file))
        self.action_handler.bindAction("media\\genmidi_op2", UIAction(self.on_genmidi_op2))
        self.action_handler.bindAction("media\\id3v1_1", UIAction(self.on_id3v1_1))
        self.action_handler.bindAction("media\\id3v2_3", UIAction(self.on_id3v2_3))
        self.action_handler.bindAction("media\\id3v2_4", UIAction(self.on_id3v2_4))
        self.action_handler.bindAction("media\\magicavoxel_vox", UIAction(self.on_magicavoxel_vox))
        self.action_handler.bindAction("media\\ogg", UIAction(self.on_ogg))
        self.action_handler.bindAction("media\\quicktime_mov", UIAction(self.on_quicktime_mov))
        self.action_handler.bindAction("media\\standard_midi_file", UIAction(self.on_standard_midi_file))
        self.action_handler.bindAction("media\\stl", UIAction(self.on_stl))
        self.action_handler.bindAction("media\\tracker_modules\\fasttracker_xm_module", UIAction(self.on_fasttracker_xm_module))
        self.action_handler.bindAction("media\\tracker_modules\\s3m", UIAction(self.on_s3m))
        self.action_handler.bindAction("media\\vp8_ivf", UIAction(self.on_vp8_ivf))
        self.action_handler.bindAction("media\\wav", UIAction(self.on_wav))
        self.action_handler.bindAction("network\\bitcoin_transaction", UIAction(self.on_bitcoin_transaction))
        self.action_handler.bindAction("network\\dns_packet", UIAction(self.on_dns_packet))
        self.action_handler.bindAction("network\\hccap", UIAction(self.on_hccap))
        self.action_handler.bindAction("network\\hccapx", UIAction(self.on_hccapx))
        self.action_handler.bindAction("network\\icmp_packet", UIAction(self.on_icmp_packet))

        if sys.version_info[0] == 3:
            self.action_handler.bindAction("network\\ethernet_frame", UIAction(self.on_ethernet_frame))
            self.action_handler.bindAction("network\\ipv4_packet", UIAction(self.on_ipv4_packet))
            self.action_handler.bindAction("network\\ipv6_packet", UIAction(self.on_ipv6_packet))
            self.action_handler.bindAction("network\\microsoft_network_monitor_v2", UIAction(self.on_microsoft_network_monitor_v2))
            self.action_handler.bindAction("network\\packet_ppi", UIAction(self.on_packet_ppi))
            self.action_handler.bindAction("network\\pcap", UIAction(self.on_pcap))
            self.action_handler.bindAction("network\\protocol_body", UIAction(self.on_protocol_body))

        self.action_handler.bindAction("network\\rtcp_payload", UIAction(self.on_rtcp_payload))
        self.action_handler.bindAction("network\\rtp_packet", UIAction(self.on_rtp_packet))
        self.action_handler.bindAction("network\\tcp_segment", UIAction(self.on_tcp_segment))
        self.action_handler.bindAction("network\\tls_client_hello", UIAction(self.on_tls_client_hello))
        self.action_handler.bindAction("network\\udp_datagram", UIAction(self.on_udp_datagram))
        self.action_handler.bindAction("network\\windows_systemtime", UIAction(self.on_windows_systemtime))
        self.action_handler.bindAction("scientific\\nt_mdt\\nt_mdt", UIAction(self.on_nt_mdt))
        self.action_handler.bindAction("scientific\\nt_mdt\\nt_mdt_pal", UIAction(self.on_nt_mdt_pal))
        self.action_handler.bindAction("scientific\\spectroscopy\\avantes_roh60", UIAction(self.on_avantes_roh60))
        self.action_handler.bindAction("scientific\\spectroscopy\\specpr", UIAction(self.on_specpr))
        self.action_handler.bindAction("security\\openpgp_message", UIAction(self.on_openpgp_message))
        self.action_handler.bindAction("security\\ssh_public_key", UIAction(self.on_ssh_public_key))
        self.action_handler.bindAction("serialization\\asn1\\asn1_der", UIAction(self.on_asn1_der))
        self.action_handler.bindAction("serialization\\bson", UIAction(self.on_bson))
        self.action_handler.bindAction("serialization\\google_protobuf", UIAction(self.on_google_protobuf))
        self.action_handler.bindAction("serialization\\microsoft_cfb", UIAction(self.on_microsoft_cfb))
        self.action_handler.bindAction("serialization\\msgpack", UIAction(self.on_msgpack))
        self.action_handler.bindAction("serialization\\ruby_marshal", UIAction(self.on_ruby_marshal))
        self.action_handler.bindAction("windows\\regf", UIAction(self.on_regf))
        self.action_handler.bindAction("windows\\windows_lnk_file", UIAction(self.on_windows_lnk_file))
        self.action_handler.bindAction("windows\\windows_minidump", UIAction(self.on_windows_minidump))
        self.action_handler.bindAction("windows\\windows_resource_file", UIAction(self.on_windows_resource_file))
        self.action_handler.bindAction("windows\\windows_shell_items", UIAction(self.on_windows_shell_items))
        self.action_handler.bindAction("windows\\windows_systemtime", UIAction(self.on_windows_systemtime))

    def mousePressEvent(self, event):
        # when someone clicks our label, pop up the context menu
        self.contextMenuManager.show(self.menu, self.action_handler)

    def enterEvent(self, event):
        self.setAutoFillBackground(True)
        self.setForegroundRole(QPalette.HighlightedText)
        QLabel.enterEvent(self, event)

    def leaveEvent(self, event):
        self.setAutoFillBackground(False)
        self.setForegroundRole(QPalette.WindowText)
        QLabel.leaveEvent(self, event)

    def on_cpio_old_le(self, uiActionContext):
        self.kv.construct_view('cpio_old_le')

    def on_gzip(self, uiActionContext):
        self.kv.construct_view('gzip')

    def on_lzh(self, uiActionContext):
        self.kv.construct_view('lzh')

    def on_rar(self, uiActionContext):
        self.kv.construct_view('rar')

    def on_zip(self, uiActionContext):
        self.kv.construct_view('zip')

    def on_monomakh_sapr_chg(self, uiActionContext):
        self.kv.construct_view('monomakh_sapr_chg')

    def on_bcd(self, uiActionContext):
        self.kv.construct_view('bcd')

    def on_dbf(self, uiActionContext):
        self.kv.construct_view('dbf')

    def on_gettext_mo(self, uiActionContext):
        self.kv.construct_view('gettext_mo')

    def on_sqlite3(self, uiActionContext):
        self.kv.construct_view('sqlite3')

    def on_tsm(self, uiActionContext):
        self.kv.construct_view('tsm')

    def on_dex(self, uiActionContext):
        self.kv.construct_view('dex')

    def on_dos_mz(self, uiActionContext):
        self.kv.construct_view('dos_mz')

    def on_elf(self, uiActionContext):
        self.kv.construct_view('elf')

    def on_java_class(self, uiActionContext):
        self.kv.construct_view('java_class')

    def on_mach_o(self, uiActionContext):
        self.kv.construct_view('mach_o')

    def on_microsoft_pe(self, uiActionContext):
        self.kv.construct_view('microsoft_pe')

    def on_python_pyc_27(self, uiActionContext):
        self.kv.construct_view('python_pyc_27')

    def on_swf(self, uiActionContext):
        self.kv.construct_view('swf')

    def on_apm_partition_table(self, uiActionContext):
        self.kv.construct_view('apm_partition_table')

    def on_apple_single_double(self, uiActionContext):
        self.kv.construct_view('apple_single_double')

    def on_cramfs(self, uiActionContext):
        self.kv.construct_view('cramfs')

    def on_ext2(self, uiActionContext):
        self.kv.construct_view('ext2')

    def on_gpt_partition_table(self, uiActionContext):
        self.kv.construct_view('gpt_partition_table')

    def on_iso9660(self, uiActionContext):
        self.kv.construct_view('iso9660')

    def on_luks(self, uiActionContext):
        self.kv.construct_view('luks')

    def on_lvm2(self, uiActionContext):
        self.kv.construct_view('lvm2')

    def on_mbr_partition_table(self, uiActionContext):
        self.kv.construct_view('mbr_partition_table')

    def on_tr_dos_image(self, uiActionContext):
        self.kv.construct_view('tr_dos_image')

    def on_vdi(self, uiActionContext):
        self.kv.construct_view('vdi')

    def on_vfat(self, uiActionContext):
        self.kv.construct_view('vfat')

    def on_vmware_vmdk(self, uiActionContext):
        self.kv.construct_view('vmware_vmdk')

    def on_andes_firmware(self, uiActionContext):
        self.kv.construct_view('andes_firmware')

    def on_ines(self, uiActionContext):
        self.kv.construct_view('ines')

    def on_uimage(self, uiActionContext):
        self.kv.construct_view('uimage')

    def on_ttf(self, uiActionContext):
        self.kv.construct_view('ttf')

    def on_allegro_dat(self, uiActionContext):
        self.kv.construct_view('allegro_dat')

    def on_doom_wad(self, uiActionContext):
        self.kv.construct_view('doom_wad')

    def on_dune_2_pak(self, uiActionContext):
        self.kv.construct_view('dune_2_pak')

    def on_fallout_dat(self, uiActionContext):
        self.kv.construct_view('fallout_dat')

    def on_ftl_dat(self, uiActionContext):
        self.kv.construct_view('ftl_dat')

    def on_gran_turismo_vol(self, uiActionContext):
        self.kv.construct_view('gran_turismo_vol')

    def on_heaps_pak(self, uiActionContext):
        self.kv.construct_view('heaps_pak')

    def on_heroes_of_might_and_magic_agg(self, uiActionContext):
        self.kv.construct_view('heroes_of_might_and_magic_agg')

    def on_heroes_of_might_and_magic_bmp(self, uiActionContext):
        self.kv.construct_view('heroes_of_might_and_magic_bmp')

    def on_quake_mdl(self, uiActionContext):
        self.kv.construct_view('quake_mdl')

    def on_quake_pak(self, uiActionContext):
        self.kv.construct_view('quake_pak')

    def on_renderware_binary_stream(self, uiActionContext):
        self.kv.construct_view('renderware_binary_stream')

    def on_saints_row_2_vpp_pc(self, uiActionContext):
        self.kv.construct_view('saints_row_2_vpp_pc')

    def on_warcraft_2_pud(self, uiActionContext):
        self.kv.construct_view('warcraft_2_pud')

    def on_shapefile_index(self, uiActionContext):
        self.kv.construct_view('shapefile_index')

    def on_shapefile_main(self, uiActionContext):
        self.kv.construct_view('shapefile_main')

    def on_edid(self, uiActionContext):
        self.kv.construct_view('edid')

    def on_mifare_classic(self, uiActionContext):
        self.kv.construct_view('mifare_classic')

    def on_bmp(self, uiActionContext):
        self.kv.construct_view('bmp')

    def on_dicom(self, uiActionContext):
        self.kv.construct_view('dicom')

    def on_exif(self, uiActionContext):
        self.kv.construct_view('exif')

    def on_exif_be(self, uiActionContext):
        self.kv.construct_view('exif_be')

    def on_exif_le(self, uiActionContext):
        self.kv.construct_view('exif_le')

    def on_gif(self, uiActionContext):
        self.kv.construct_view('gif')

    def on_icc_4(self, uiActionContext):
        self.kv.construct_view('icc_4')

    def on_ico(self, uiActionContext):
        self.kv.construct_view('ico')

    def on_jpeg(self, uiActionContext):
        self.kv.construct_view('jpeg')

    def on_pcx(self, uiActionContext):
        self.kv.construct_view('pcx')

    def on_pcx_dcx(self, uiActionContext):
        self.kv.construct_view('pcx_dcx')

    def on_png(self, uiActionContext):
        self.kv.construct_view('png')

    def on_psx_tim(self, uiActionContext):
        self.kv.construct_view('psx_tim')

    def on_tga(self, uiActionContext):
        self.kv.construct_view('tga')

    def on_wmf(self, uiActionContext):
        self.kv.construct_view('wmf')

    def on_xwd(self, uiActionContext):
        self.kv.construct_view('xwd')

    def on_aix_utmp(self, uiActionContext):
        self.kv.construct_view('aix_utmp')

    def on_glibc_utmp(self, uiActionContext):
        self.kv.construct_view('glibc_utmp')

    def on_systemd_journal(self, uiActionContext):
        self.kv.construct_view('systemd_journal')

    def on_windows_evt_log(self, uiActionContext):
        self.kv.construct_view('windows_evt_log')

    def on_code_6502(self, uiActionContext):
        self.kv.construct_view('code_6502')

    def on_avi(self, uiActionContext):
        self.kv.construct_view('avi')

    def on_blender_blend(self, uiActionContext):
        self.kv.construct_view('blender_blend')

    def on_creative_voice_file(self, uiActionContext):
        self.kv.construct_view('creative_voice_file')

    def on_genmidi_op2(self, uiActionContext):
        self.kv.construct_view('genmidi_op2')

    def on_id3v1_1(self, uiActionContext):
        self.kv.construct_view('id3v1_1')

    def on_id3v2_3(self, uiActionContext):
        self.kv.construct_view('id3v2_3')

    def on_id3v2_4(self, uiActionContext):
        self.kv.construct_view('id3v2_4')

    def on_magicavoxel_vox(self, uiActionContext):
        self.kv.construct_view('magicavoxel_vox')

    def on_ogg(self, uiActionContext):
        self.kv.construct_view('ogg')

    def on_quicktime_mov(self, uiActionContext):
        self.kv.construct_view('quicktime_mov')

    def on_standard_midi_file(self, uiActionContext):
        self.kv.construct_view('standard_midi_file')

    def on_stl(self, uiActionContext):
        self.kv.construct_view('stl')

    def on_fasttracker_xm_module(self, uiActionContext):
        self.kv.construct_view('fasttracker_xm_module')

    def on_s3m(self, uiActionContext):
        self.kv.construct_view('s3m')

    def on_vp8_ivf(self, uiActionContext):
        self.kv.construct_view('vp8_ivf')

    def on_wav(self, uiActionContext):
        self.kv.construct_view('wav')

    def on_bitcoin_transaction(self, uiActionContext):
        self.kv.construct_view('bitcoin_transaction')

    def on_dns_packet(self, uiActionContext):
        self.kv.construct_view('dns_packet')

    def on_ethernet_frame(self, uiActionContext):
        self.kv.construct_view('ethernet_frame')

    def on_hccap(self, uiActionContext):
        self.kv.construct_view('hccap')

    def on_hccapx(self, uiActionContext):
        self.kv.construct_view('hccapx')

    def on_icmp_packet(self, uiActionContext):
        self.kv.construct_view('icmp_packet')

    def on_ipv4_packet(self, uiActionContext):
        self.kv.construct_view('ipv4_packet')

    def on_ipv6_packet(self, uiActionContext):
        self.kv.construct_view('ipv6_packet')

    def on_microsoft_network_monitor_v2(self, uiActionContext):
        self.kv.construct_view('microsoft_network_monitor_v2')

    def on_packet_ppi(self, uiActionContext):
        self.kv.construct_view('packet_ppi')

    def on_pcap(self, uiActionContext):
        self.kv.construct_view('pcap')

    def on_protocol_body(self, uiActionContext):
        self.kv.construct_view('protocol_body')

    def on_rtcp_payload(self, uiActionContext):
        self.kv.construct_view('rtcp_payload')

    def on_rtp_packet(self, uiActionContext):
        self.kv.construct_view('rtp_packet')

    def on_tcp_segment(self, uiActionContext):
        self.kv.construct_view('tcp_segment')

    def on_tls_client_hello(self, uiActionContext):
        self.kv.construct_view('tls_client_hello')

    def on_udp_datagram(self, uiActionContext):
        self.kv.construct_view('udp_datagram')

    def on_windows_systemtime(self, uiActionContext):
        self.kv.construct_view('windows_systemtime')

    def on_nt_mdt(self, uiActionContext):
        self.kv.construct_view('nt_mdt')

    def on_nt_mdt_pal(self, uiActionContext):
        self.kv.construct_view('nt_mdt_pal')

    def on_avantes_roh60(self, uiActionContext):
        self.kv.construct_view('avantes_roh60')

    def on_specpr(self, uiActionContext):
        self.kv.construct_view('specpr')

    def on_openpgp_message(self, uiActionContext):
        self.kv.construct_view('openpgp_message')

    def on_ssh_public_key(self, uiActionContext):
        self.kv.construct_view('ssh_public_key')

    def on_asn1_der(self, uiActionContext):
        self.kv.construct_view('asn1_der')

    def on_bson(self, uiActionContext):
        self.kv.construct_view('bson')

    def on_google_protobuf(self, uiActionContext):
        self.kv.construct_view('google_protobuf')

    def on_microsoft_cfb(self, uiActionContext):
        self.kv.construct_view('microsoft_cfb')

    def on_msgpack(self, uiActionContext):
        self.kv.construct_view('msgpack')

    def on_ruby_marshal(self, uiActionContext):
        self.kv.construct_view('ruby_marshal')

    def on_regf(self, uiActionContext):
        self.kv.construct_view('regf')

    def on_windows_lnk_file(self, uiActionContext):
        self.kv.construct_view('windows_lnk_file')

    def on_windows_minidump(self, uiActionContext):
        self.kv.construct_view('windows_minidump')

    def on_windows_resource_file(self, uiActionContext):
        self.kv.construct_view('windows_resource_file')

    def on_windows_shell_items(self, uiActionContext):
        self.kv.construct_view('windows_shell_items')

    def on_windows_systemtime(self, uiActionContext):
        self.kv.construct_view('windows_systemtime')


# KaitaiOptionsBarWidget <- OptionsBarWidget <- QFrame
class KaitaiOptionsBarWidget(QWidget):
    def __init__(self, parent):
        print('INFO: KaitaiOptionsBarWidget.__init__()')

        #icon = binaryninjaui.ClickableIcon(QImage(":/icons/images/menu.png"), QSize(16, 16))

        self.kaitaiView = parent

        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0,0,0,0)

        self.options = KaitaiOptionsWidget(self)
        self.layout.addWidget(self.options)

    def updateStatus(self):
        print('INFO: KaitaiOptionsBarWidget.updateStatus()')
        pass
