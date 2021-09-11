# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Wav(KaitaiStruct):
    """The WAVE file format is a subset of Microsoft's RIFF specification for the
    storage of multimedia files. A RIFF file starts out with a file header
    followed by a sequence of data chunks. A WAVE file is often just a RIFF
    file with a single "WAVE" chunk which consists of two sub-chunks --
    a "fmt " chunk specifying the data format and a "data" chunk containing
    the actual sample data.
    
    This Kaitai implementation was written by John Byrd of Gigantic Software
    (jbyrd@giganticsoftware.com), and it is likely to contain bugs.
    
    .. seealso::
       Source - http://soundfile.sapp.org/doc/WaveFormat/
    """

    class WFormatTagType(Enum):
        unknown = 0
        pcm = 1
        adpcm = 2
        ieee_float = 3
        vselp = 4
        ibm_cvsd = 5
        alaw = 6
        mulaw = 7
        dts = 8
        drm = 9
        wmavoice9 = 10
        wmavoice10 = 11
        oki_adpcm = 16
        dvi_adpcm = 17
        mediaspace_adpcm = 18
        sierra_adpcm = 19
        g723_adpcm = 20
        digistd = 21
        digifix = 22
        dialogic_oki_adpcm = 23
        mediavision_adpcm = 24
        cu_codec = 25
        hp_dyn_voice = 26
        yamaha_adpcm = 32
        sonarc = 33
        dspgroup_truespeech = 34
        echosc1 = 35
        audiofile_af36 = 36
        aptx = 37
        audiofile_af10 = 38
        prosody_1612 = 39
        lrc = 40
        dolby_ac2 = 48
        gsm610 = 49
        msnaudio = 50
        antex_adpcme = 51
        control_res_vqlpc = 52
        digireal = 53
        digiadpcm = 54
        control_res_cr10 = 55
        nms_vbxadpcm = 56
        cs_imaadpcm = 57
        echosc3 = 58
        rockwell_adpcm = 59
        rockwell_digitalk = 60
        xebec = 61
        g721_adpcm = 64
        g728_celp = 65
        msg723 = 66
        intel_g723_1 = 67
        intel_g729 = 68
        sharp_g726 = 69
        mpeg = 80
        rt24 = 82
        pac = 83
        mpeglayer3 = 85
        lucent_g723 = 89
        cirrus = 96
        espcm = 97
        voxware = 98
        canopus_atrac = 99
        g726_adpcm = 100
        g722_adpcm = 101
        dsat = 102
        dsat_display = 103
        voxware_byte_aligned = 105
        voxware_ac8 = 112
        voxware_ac10 = 113
        voxware_ac16 = 114
        voxware_ac20 = 115
        voxware_rt24 = 116
        voxware_rt29 = 117
        voxware_rt29hw = 118
        voxware_vr12 = 119
        voxware_vr18 = 120
        voxware_tq40 = 121
        voxware_sc3 = 122
        voxware_sc3_1 = 123
        softsound = 128
        voxware_tq60 = 129
        msrt24 = 130
        g729a = 131
        mvi_mvi2 = 132
        df_g726 = 133
        df_gsm610 = 134
        isiaudio = 136
        onlive = 137
        multitude_ft_sx20 = 138
        infocom_its_g721_adpcm = 139
        convedia_g729 = 140
        congruency = 141
        sbc24 = 145
        dolby_ac3_spdif = 146
        mediasonic_g723 = 147
        prosody_8kbps = 148
        zyxel_adpcm = 151
        philips_lpcbb = 152
        packed = 153
        malden_phonytalk = 160
        racal_recorder_gsm = 161
        racal_recorder_g720_a = 162
        racal_recorder_g723_1 = 163
        racal_recorder_tetra_acelp = 164
        nec_aac = 176
        raw_aac1 = 255
        rhetorex_adpcm = 256
        irat = 257
        vivo_g723 = 273
        vivo_siren = 274
        philips_celp = 288
        philips_grundig = 289
        digital_g723 = 291
        sanyo_ld_adpcm = 293
        siprolab_aceplnet = 304
        siprolab_acelp4800 = 305
        siprolab_acelp8v3 = 306
        siprolab_g729 = 307
        siprolab_g729a = 308
        siprolab_kelvin = 309
        voiceage_amr = 310
        g726adpcm = 320
        dictaphone_celp68 = 321
        dictaphone_celp54 = 322
        qualcomm_purevoice = 336
        qualcomm_halfrate = 337
        tubgsm = 341
        msaudio1 = 352
        wmaudio2 = 353
        wmaudio3 = 354
        wmaudio_lossless = 355
        wmaspdif = 356
        unisys_nap_adpcm = 368
        unisys_nap_ulaw = 369
        unisys_nap_alaw = 370
        unisys_nap_16k = 371
        sycom_acm_syc008 = 372
        sycom_acm_syc701_g726l = 373
        sycom_acm_syc701_celp54 = 374
        sycom_acm_syc701_celp68 = 375
        knowledge_adventure_adpcm = 376
        fraunhofer_iis_mpeg2_aac = 384
        dts_ds = 400
        creative_adpcm = 512
        creative_fastspeech8 = 514
        creative_fastspeech10 = 515
        uher_adpcm = 528
        ulead_dv_audio = 533
        ulead_dv_audio_1 = 534
        quarterdeck = 544
        ilink_vc = 560
        raw_sport = 576
        esst_ac3 = 577
        generic_passthru = 585
        ipi_hsx = 592
        ipi_rpelp = 593
        cs2 = 608
        sony_scx = 624
        sony_scy = 625
        sony_atrac3 = 626
        sony_spc = 627
        telum_audio = 640
        telum_ia_audio = 641
        norcom_voice_systems_adpcm = 645
        fm_towns_snd = 768
        micronas = 848
        micronas_celp833 = 849
        btv_digital = 1024
        intel_music_coder = 1025
        indeo_audio = 1026
        qdesign_music = 1104
        on2_vp7_audio = 1280
        on2_vp6_audio = 1281
        vme_vmpcm = 1664
        tpc = 1665
        lightwave_lossless = 2222
        oligsm = 4096
        oliadpcm = 4097
        olicelp = 4098
        olisbc = 4099
        oliopr = 4100
        lh_codec = 4352
        lh_codec_celp = 4353
        lh_codec_sbc8 = 4354
        lh_codec_sbc12 = 4355
        lh_codec_sbc16 = 4356
        norris = 5120
        isiaudio_2 = 5121
        soundspace_musicompress = 5376
        mpeg_adts_aac = 5632
        mpeg_raw_aac = 5633
        mpeg_loas = 5634
        nokia_mpeg_adts_aac = 5640
        nokia_mpeg_raw_aac = 5641
        vodafone_mpeg_adts_aac = 5642
        vodafone_mpeg_raw_aac = 5643
        mpeg_heaac = 5648
        voxware_rt24_speech = 6172
        sonicfoundry_lossless = 6513
        innings_telecom_adpcm = 6521
        lucent_sx8300p = 7175
        lucent_sx5363s = 7180
        cuseeme = 7939
        ntcsoft_alf2cm_acm = 8132
        dvm = 8192
        dts2 = 8193
        makeavis = 13075
        divio_mpeg4_aac = 16707
        nokia_adaptive_multirate = 16897
        divio_g726 = 16963
        lead_speech = 17228
        lead_vorbis = 22092
        wavpack_audio = 22358
        ogg_vorbis_mode_1 = 26447
        ogg_vorbis_mode_2 = 26448
        ogg_vorbis_mode_3 = 26449
        ogg_vorbis_mode_1_plus = 26479
        ogg_vorbis_mode_2_plus = 26480
        ogg_vorbis_mode_3_plus = 26481
        threecom_nbx = 28672
        faad_aac = 28781
        amr_nb = 29537
        amr_wb = 29538
        amr_wp = 29539
        gsm_amr_cbr = 31265
        gsm_amr_vbr_sid = 31266
        comverse_infosys_g723_1 = 41216
        comverse_infosys_avqsbc = 41217
        comverse_infosys_sbc = 41218
        symbol_g729_a = 41219
        voiceage_amr_wb = 41220
        ingenient_g726 = 41221
        mpeg4_aac = 41222
        encore_g726 = 41223
        zoll_asao = 41224
        speex_voice = 41225
        vianix_masc = 41226
        wm9_spectrum_analyzer = 41227
        wmf_spectrum_anayzer = 41228
        gsm_610 = 41229
        gsm_620 = 41230
        gsm_660 = 41231
        gsm_690 = 41232
        gsm_adaptive_multirate_wb = 41233
        polycom_g722 = 41234
        polycom_g728 = 41235
        polycom_g729_a = 41236
        polycom_siren = 41237
        global_ip_ilbc = 41238
        radiotime_time_shift_radio = 41239
        nice_aca = 41240
        nice_adpcm = 41241
        vocord_g721 = 41242
        vocord_g726 = 41243
        vocord_g722_1 = 41244
        vocord_g728 = 41245
        vocord_g729 = 41246
        vocord_g729_a = 41247
        vocord_g723_1 = 41248
        vocord_lbc = 41249
        nice_g728 = 41250
        frace_telecom_g729 = 41251
        codian = 41252
        flac = 61868
        extensible = 65534
        development = 65535

    class Fourcc(Enum):
        cue = 543520099
        fmt = 544501094
        wave = 1163280727
        riff = 1179011410
        info = 1330007625
        list = 1414744396
        data = 1635017060
        umid = 1684630901
        minf = 1718511981
        regn = 1852269938
        bext = 1954047330
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.chunk = Riff.Chunk(self._io, self, self._root)

    class SampleType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.sample = self._io.read_u2le()


    class FormatChunkType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.w_format_tag = KaitaiStream.resolve_enum(Wav.WFormatTagType, self._io.read_u2le())
            self.n_channels = self._io.read_u2le()
            self.n_samples_per_sec = self._io.read_u4le()
            self.n_avg_bytes_per_sec = self._io.read_u4le()
            self.n_block_align = self._io.read_u2le()
            self.w_bits_per_sample = self._io.read_u2le()
            if not (self.is_basic_pcm):
                self.cb_size = self._io.read_u2le()

            if self.is_cb_size_meaningful:
                self.w_valid_bits_per_sample = self._io.read_u2le()

            if self.is_extensible:
                self.channel_mask_and_subformat = Wav.ChannelMaskAndSubformatType(self._io, self, self._root)


        @property
        def is_extensible(self):
            if hasattr(self, '_m_is_extensible'):
                return self._m_is_extensible if hasattr(self, '_m_is_extensible') else None

            self._m_is_extensible = self.w_format_tag == Wav.WFormatTagType.extensible
            return self._m_is_extensible if hasattr(self, '_m_is_extensible') else None

        @property
        def is_basic_pcm(self):
            if hasattr(self, '_m_is_basic_pcm'):
                return self._m_is_basic_pcm if hasattr(self, '_m_is_basic_pcm') else None

            self._m_is_basic_pcm = self.w_format_tag == Wav.WFormatTagType.pcm
            return self._m_is_basic_pcm if hasattr(self, '_m_is_basic_pcm') else None

        @property
        def is_basic_float(self):
            if hasattr(self, '_m_is_basic_float'):
                return self._m_is_basic_float if hasattr(self, '_m_is_basic_float') else None

            self._m_is_basic_float = self.w_format_tag == Wav.WFormatTagType.ieee_float
            return self._m_is_basic_float if hasattr(self, '_m_is_basic_float') else None

        @property
        def is_cb_size_meaningful(self):
            if hasattr(self, '_m_is_cb_size_meaningful'):
                return self._m_is_cb_size_meaningful if hasattr(self, '_m_is_cb_size_meaningful') else None

            self._m_is_cb_size_meaningful =  ((not (self.is_basic_pcm)) and (self.cb_size != 0)) 
            return self._m_is_cb_size_meaningful if hasattr(self, '_m_is_cb_size_meaningful') else None


    class GuidType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.data1 = self._io.read_u4le()
            self.data2 = self._io.read_u2le()
            self.data3 = self._io.read_u2le()
            self.data4 = self._io.read_u4be()
            self.data4a = self._io.read_u4be()


    class InfoChunkType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.chunk = Riff.Chunk(self._io, self, self._root)

        @property
        def chunk_data(self):
            if hasattr(self, '_m_chunk_data'):
                return self._m_chunk_data if hasattr(self, '_m_chunk_data') else None

            io = self.chunk.data_slot._io
            _pos = io.pos()
            io.seek(0)
            self._m_chunk_data = (io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            io.seek(_pos)
            return self._m_chunk_data if hasattr(self, '_m_chunk_data') else None


    class CuePointType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.dw_name = self._io.read_u4le()
            self.dw_position = self._io.read_u4le()
            self.fcc_chunk = self._io.read_u4le()
            self.dw_chunk_start = self._io.read_u4le()
            self.dw_block_start = self._io.read_u4le()
            self.dw_sample_offset = self._io.read_u4le()


    class DataChunkType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.data = self._io.read_bytes_full()


    class SamplesType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.samples = self._io.read_u4le()


    class ChannelMaskAndSubformatType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.dw_channel_mask = Wav.ChannelMaskType(self._io, self, self._root)
            self.subformat = Wav.GuidType(self._io, self, self._root)


    class CueChunkType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.dw_cue_points = self._io.read_u4le()
            self.cue_points = [None] * (self.dw_cue_points)
            for i in range(self.dw_cue_points):
                self.cue_points[i] = Wav.CuePointType(self._io, self, self._root)



    class ListChunkType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.parent_chunk_data = Riff.ParentChunkData(self._io, self, self._root)

        @property
        def form_type(self):
            if hasattr(self, '_m_form_type'):
                return self._m_form_type if hasattr(self, '_m_form_type') else None

            self._m_form_type = KaitaiStream.resolve_enum(Wav.Fourcc, self.parent_chunk_data.form_type)
            return self._m_form_type if hasattr(self, '_m_form_type') else None

        @property
        def subchunks(self):
            if hasattr(self, '_m_subchunks'):
                return self._m_subchunks if hasattr(self, '_m_subchunks') else None

            io = self.parent_chunk_data.subchunks_slot._io
            _pos = io.pos()
            io.seek(0)
            self._m_subchunks = []
            i = 0
            while not io.is_eof():
                _on = self.form_type
                if _on == Wav.Fourcc.info:
                    self._m_subchunks.append(Wav.InfoChunkType(io, self, self._root))
                i += 1

            io.seek(_pos)
            return self._m_subchunks if hasattr(self, '_m_subchunks') else None


    class ChannelMaskType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.front_right_of_center = self._io.read_bits_int_be(1) != 0
            self.front_left_of_center = self._io.read_bits_int_be(1) != 0
            self.back_right = self._io.read_bits_int_be(1) != 0
            self.back_left = self._io.read_bits_int_be(1) != 0
            self.low_frequency = self._io.read_bits_int_be(1) != 0
            self.front_center = self._io.read_bits_int_be(1) != 0
            self.front_right = self._io.read_bits_int_be(1) != 0
            self.front_left = self._io.read_bits_int_be(1) != 0
            self.top_center = self._io.read_bits_int_be(1) != 0
            self.side_right = self._io.read_bits_int_be(1) != 0
            self.side_left = self._io.read_bits_int_be(1) != 0
            self.back_center = self._io.read_bits_int_be(1) != 0
            self.top_back_left = self._io.read_bits_int_be(1) != 0
            self.top_front_right = self._io.read_bits_int_be(1) != 0
            self.top_front_center = self._io.read_bits_int_be(1) != 0
            self.top_front_left = self._io.read_bits_int_be(1) != 0
            self.unused1 = self._io.read_bits_int_be(6)
            self.top_back_right = self._io.read_bits_int_be(1) != 0
            self.top_back_center = self._io.read_bits_int_be(1) != 0
            self.unused2 = self._io.read_bits_int_be(8)


    class ChunkType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.chunk = Riff.Chunk(self._io, self, self._root)

        @property
        def chunk_id(self):
            if hasattr(self, '_m_chunk_id'):
                return self._m_chunk_id if hasattr(self, '_m_chunk_id') else None

            self._m_chunk_id = KaitaiStream.resolve_enum(Wav.Fourcc, self.chunk.id)
            return self._m_chunk_id if hasattr(self, '_m_chunk_id') else None

        @property
        def chunk_data(self):
            if hasattr(self, '_m_chunk_data'):
                return self._m_chunk_data if hasattr(self, '_m_chunk_data') else None

            io = self.chunk.data_slot._io
            _pos = io.pos()
            io.seek(0)
            _on = self.chunk_id
            if _on == Wav.Fourcc.list:
                self._m_chunk_data = Wav.ListChunkType(io, self, self._root)
            elif _on == Wav.Fourcc.fmt:
                self._m_chunk_data = Wav.FormatChunkType(io, self, self._root)
            elif _on == Wav.Fourcc.bext:
                self._m_chunk_data = Wav.BextChunkType(io, self, self._root)
            elif _on == Wav.Fourcc.cue:
                self._m_chunk_data = Wav.CueChunkType(io, self, self._root)
            elif _on == Wav.Fourcc.data:
                self._m_chunk_data = Wav.DataChunkType(io, self, self._root)
            io.seek(_pos)
            return self._m_chunk_data if hasattr(self, '_m_chunk_data') else None


    class BextChunkType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.description = (KaitaiStream.bytes_terminate(self._io.read_bytes(256), 0, False)).decode(u"ASCII")
            self.originator = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ASCII")
            self.originator_reference = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ASCII")
            self.origination_date = (self._io.read_bytes(10)).decode(u"ASCII")
            self.origination_time = (self._io.read_bytes(8)).decode(u"ASCII")
            self.time_reference_low = self._io.read_u4le()
            self.time_reference_high = self._io.read_u4le()
            self.version = self._io.read_u2le()
            self.umid = self._io.read_bytes(64)
            self.loudness_value = self._io.read_u2le()
            self.loudness_range = self._io.read_u2le()
            self.max_true_peak_level = self._io.read_u2le()
            self.max_momentary_loudness = self._io.read_u2le()
            self.max_short_term_loudness = self._io.read_u2le()


    @property
    def subchunks(self):
        if hasattr(self, '_m_subchunks'):
            return self._m_subchunks if hasattr(self, '_m_subchunks') else None

        if self.is_form_type_wave:
            io = self.parent_chunk_data.subchunks_slot._io
            _pos = io.pos()
            io.seek(0)
            self._m_subchunks = []
            i = 0
            while not io.is_eof():
                self._m_subchunks.append(Wav.ChunkType(io, self, self._root))
                i += 1

            io.seek(_pos)

        return self._m_subchunks if hasattr(self, '_m_subchunks') else None

    @property
    def parent_chunk_data(self):
        if hasattr(self, '_m_parent_chunk_data'):
            return self._m_parent_chunk_data if hasattr(self, '_m_parent_chunk_data') else None

        if self.is_riff_chunk:
            io = self.chunk.data_slot._io
            _pos = io.pos()
            io.seek(0)
            self._m_parent_chunk_data = Riff.ParentChunkData(io, self, self._root)
            io.seek(_pos)

        return self._m_parent_chunk_data if hasattr(self, '_m_parent_chunk_data') else None

    @property
    def is_form_type_wave(self):
        if hasattr(self, '_m_is_form_type_wave'):
            return self._m_is_form_type_wave if hasattr(self, '_m_is_form_type_wave') else None

        self._m_is_form_type_wave =  ((self.is_riff_chunk) and (self.form_type == Wav.Fourcc.wave)) 
        return self._m_is_form_type_wave if hasattr(self, '_m_is_form_type_wave') else None

    @property
    def is_riff_chunk(self):
        if hasattr(self, '_m_is_riff_chunk'):
            return self._m_is_riff_chunk if hasattr(self, '_m_is_riff_chunk') else None

        self._m_is_riff_chunk = self.chunk_id == Wav.Fourcc.riff
        return self._m_is_riff_chunk if hasattr(self, '_m_is_riff_chunk') else None

    @property
    def chunk_id(self):
        if hasattr(self, '_m_chunk_id'):
            return self._m_chunk_id if hasattr(self, '_m_chunk_id') else None

        self._m_chunk_id = KaitaiStream.resolve_enum(Wav.Fourcc, self.chunk.id)
        return self._m_chunk_id if hasattr(self, '_m_chunk_id') else None

    @property
    def form_type(self):
        if hasattr(self, '_m_form_type'):
            return self._m_form_type if hasattr(self, '_m_form_type') else None

        self._m_form_type = KaitaiStream.resolve_enum(Wav.Fourcc, self.parent_chunk_data.form_type)
        return self._m_form_type if hasattr(self, '_m_form_type') else None


