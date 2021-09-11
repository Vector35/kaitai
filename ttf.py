# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Ttf(KaitaiStruct):
    """A TrueType font file contains data, in table format, that comprises
    an outline font.
    
    .. seealso::
       Source - https://www.microsoft.com/typography/tt/ttf_spec/ttch02.doc
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.offset_table = Ttf.OffsetTable(self._io, self, self._root)
        self.directory_table = [None] * (self.offset_table.num_tables)
        for i in range(self.offset_table.num_tables):
            self.directory_table[i] = Ttf.DirTableEntry(self._io, self, self._root)


    class Post(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.format = Ttf.Fixed(self._io, self, self._root)
            self.italic_angle = Ttf.Fixed(self._io, self, self._root)
            self.underline_position = self._io.read_s2be()
            self.underline_thichness = self._io.read_s2be()
            self.is_fixed_pitch = self._io.read_u4be()
            self.min_mem_type42 = self._io.read_u4be()
            self.max_mem_type42 = self._io.read_u4be()
            self.min_mem_type1 = self._io.read_u4be()
            self.max_mem_type1 = self._io.read_u4be()
            if  ((self.format.major == 2) and (self.format.minor == 0)) :
                self.format20 = Ttf.Post.Format20(self._io, self, self._root)


        class Format20(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.number_of_glyphs = self._io.read_u2be()
                self.glyph_name_index = [None] * (self.number_of_glyphs)
                for i in range(self.number_of_glyphs):
                    self.glyph_name_index[i] = self._io.read_u2be()

                self.glyph_names = []
                i = 0
                while True:
                    _ = Ttf.Post.Format20.PascalString(self._io, self, self._root)
                    self.glyph_names.append(_)
                    if _.length == 0:
                        break
                    i += 1

            class PascalString(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.length = self._io.read_u1()
                    if self.length != 0:
                        self.value = (self._io.read_bytes(self.length)).decode(u"ascii")





    class Name(KaitaiStruct):
        """Name table is meant to include human-readable string metadata
        that describes font: name of the font, its styles, copyright &
        trademark notices, vendor and designer info, etc.
        
        The table includes a list of "name records", each of which
        corresponds to a single metadata entry.
        
        .. seealso::
           Source - https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6name.html
        """

        class Platforms(Enum):
            unicode = 0
            macintosh = 1
            reserved_2 = 2
            microsoft = 3

        class Names(Enum):
            copyright = 0
            font_family = 1
            font_subfamily = 2
            unique_subfamily_id = 3
            full_font_name = 4
            name_table_version = 5
            postscript_font_name = 6
            trademark = 7
            manufacturer = 8
            designer = 9
            description = 10
            url_vendor = 11
            url_designer = 12
            license = 13
            url_license = 14
            reserved_15 = 15
            preferred_family = 16
            preferred_subfamily = 17
            compatible_full_name = 18
            sample_text = 19
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.format_selector = self._io.read_u2be()
            self.num_name_records = self._io.read_u2be()
            self.ofs_strings = self._io.read_u2be()
            self.name_records = [None] * (self.num_name_records)
            for i in range(self.num_name_records):
                self.name_records[i] = Ttf.Name.NameRecord(self._io, self, self._root)


        class NameRecord(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.platform_id = KaitaiStream.resolve_enum(Ttf.Name.Platforms, self._io.read_u2be())
                self.encoding_id = self._io.read_u2be()
                self.language_id = self._io.read_u2be()
                self.name_id = KaitaiStream.resolve_enum(Ttf.Name.Names, self._io.read_u2be())
                self.len_str = self._io.read_u2be()
                self.ofs_str = self._io.read_u2be()

            @property
            def ascii_value(self):
                if hasattr(self, '_m_ascii_value'):
                    return self._m_ascii_value if hasattr(self, '_m_ascii_value') else None

                io = self._parent._io
                _pos = io.pos()
                io.seek((self._parent.ofs_strings + self.ofs_str))
                self._m_ascii_value = (io.read_bytes(self.len_str)).decode(u"ascii")
                io.seek(_pos)
                return self._m_ascii_value if hasattr(self, '_m_ascii_value') else None

            @property
            def unicode_value(self):
                if hasattr(self, '_m_unicode_value'):
                    return self._m_unicode_value if hasattr(self, '_m_unicode_value') else None

                io = self._parent._io
                _pos = io.pos()
                io.seek((self._parent.ofs_strings + self.ofs_str))
                self._m_unicode_value = (io.read_bytes(self.len_str)).decode(u"utf-16be")
                io.seek(_pos)
                return self._m_unicode_value if hasattr(self, '_m_unicode_value') else None



    class Head(KaitaiStruct):

        class Flags(Enum):
            baseline_at_y0 = 1
            left_sidebearing_at_x0 = 2
            flag_depend_on_point_size = 4
            flag_force_ppem = 8
            flag_may_advance_width = 16

        class FontDirectionHint(Enum):
            fully_mixed_directional_glyphs = 0
            only_strongly_left_to_right = 1
            strongly_left_to_right_and_neutrals = 2
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.version = Ttf.Fixed(self._io, self, self._root)
            self.font_revision = Ttf.Fixed(self._io, self, self._root)
            self.checksum_adjustment = self._io.read_u4be()
            self.magic_number = self._io.read_bytes(4)
            if not self.magic_number == b"\x5F\x0F\x3C\xF5":
                raise kaitaistruct.ValidationNotEqualError(b"\x5F\x0F\x3C\xF5", self.magic_number, self._io, u"/types/head/seq/3")
            self.flags = KaitaiStream.resolve_enum(Ttf.Head.Flags, self._io.read_u2be())
            self.units_per_em = self._io.read_u2be()
            self.created = self._io.read_u8be()
            self.modified = self._io.read_u8be()
            self.x_min = self._io.read_s2be()
            self.y_min = self._io.read_s2be()
            self.x_max = self._io.read_s2be()
            self.y_max = self._io.read_s2be()
            self.mac_style = self._io.read_u2be()
            self.lowest_rec_ppem = self._io.read_u2be()
            self.font_direction_hint = KaitaiStream.resolve_enum(Ttf.Head.FontDirectionHint, self._io.read_s2be())
            self.index_to_loc_format = self._io.read_s2be()
            self.glyph_data_format = self._io.read_s2be()


    class Prep(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.instructions = self._io.read_bytes_full()


    class Hhea(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.version = Ttf.Fixed(self._io, self, self._root)
            self.ascender = self._io.read_s2be()
            self.descender = self._io.read_s2be()
            self.line_gap = self._io.read_s2be()
            self.advance_width_max = self._io.read_u2be()
            self.min_left_side_bearing = self._io.read_s2be()
            self.min_right_side_bearing = self._io.read_s2be()
            self.x_max_extend = self._io.read_s2be()
            self.caret_slope_rise = self._io.read_s2be()
            self.caret_slope_run = self._io.read_s2be()
            self.reserved = self._io.read_bytes(10)
            if not self.reserved == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", self.reserved, self._io, u"/types/hhea/seq/10")
            self.metric_data_format = self._io.read_s2be()
            self.number_of_hmetrics = self._io.read_u2be()


    class Fpgm(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.instructions = self._io.read_bytes_full()


    class Kern(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.version = self._io.read_u2be()
            self.subtable_count = self._io.read_u2be()
            self.subtables = [None] * (self.subtable_count)
            for i in range(self.subtable_count):
                self.subtables[i] = Ttf.Kern.Subtable(self._io, self, self._root)


        class Subtable(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.version = self._io.read_u2be()
                self.length = self._io.read_u2be()
                self.format = self._io.read_u1()
                self.reserved = self._io.read_bits_int_be(4)
                self.is_override = self._io.read_bits_int_be(1) != 0
                self.is_cross_stream = self._io.read_bits_int_be(1) != 0
                self.is_minimum = self._io.read_bits_int_be(1) != 0
                self.is_horizontal = self._io.read_bits_int_be(1) != 0
                self._io.align_to_byte()
                if self.format == 0:
                    self.format0 = Ttf.Kern.Subtable.Format0(self._io, self, self._root)


            class Format0(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.pair_count = self._io.read_u2be()
                    self.search_range = self._io.read_u2be()
                    self.entry_selector = self._io.read_u2be()
                    self.range_shift = self._io.read_u2be()
                    self.kerning_pairs = [None] * (self.pair_count)
                    for i in range(self.pair_count):
                        self.kerning_pairs[i] = Ttf.Kern.Subtable.Format0.KerningPair(self._io, self, self._root)


                class KerningPair(KaitaiStruct):
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self._read()

                    def _read(self):
                        self.left = self._io.read_u2be()
                        self.right = self._io.read_u2be()
                        self.value = self._io.read_s2be()





    class DirTableEntry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.tag = (self._io.read_bytes(4)).decode(u"ascii")
            self.checksum = self._io.read_u4be()
            self.offset = self._io.read_u4be()
            self.length = self._io.read_u4be()

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value if hasattr(self, '_m_value') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.offset)
            _on = self.tag
            if _on == u"head":
                self._raw__m_value = io.read_bytes(self.length)
                _io__raw__m_value = KaitaiStream(BytesIO(self._raw__m_value))
                self._m_value = Ttf.Head(_io__raw__m_value, self, self._root)
            elif _on == u"cvt ":
                self._raw__m_value = io.read_bytes(self.length)
                _io__raw__m_value = KaitaiStream(BytesIO(self._raw__m_value))
                self._m_value = Ttf.Cvt(_io__raw__m_value, self, self._root)
            elif _on == u"prep":
                self._raw__m_value = io.read_bytes(self.length)
                _io__raw__m_value = KaitaiStream(BytesIO(self._raw__m_value))
                self._m_value = Ttf.Prep(_io__raw__m_value, self, self._root)
            elif _on == u"kern":
                self._raw__m_value = io.read_bytes(self.length)
                _io__raw__m_value = KaitaiStream(BytesIO(self._raw__m_value))
                self._m_value = Ttf.Kern(_io__raw__m_value, self, self._root)
            elif _on == u"hhea":
                self._raw__m_value = io.read_bytes(self.length)
                _io__raw__m_value = KaitaiStream(BytesIO(self._raw__m_value))
                self._m_value = Ttf.Hhea(_io__raw__m_value, self, self._root)
            elif _on == u"post":
                self._raw__m_value = io.read_bytes(self.length)
                _io__raw__m_value = KaitaiStream(BytesIO(self._raw__m_value))
                self._m_value = Ttf.Post(_io__raw__m_value, self, self._root)
            elif _on == u"OS/2":
                self._raw__m_value = io.read_bytes(self.length)
                _io__raw__m_value = KaitaiStream(BytesIO(self._raw__m_value))
                self._m_value = Ttf.Os2(_io__raw__m_value, self, self._root)
            elif _on == u"name":
                self._raw__m_value = io.read_bytes(self.length)
                _io__raw__m_value = KaitaiStream(BytesIO(self._raw__m_value))
                self._m_value = Ttf.Name(_io__raw__m_value, self, self._root)
            elif _on == u"maxp":
                self._raw__m_value = io.read_bytes(self.length)
                _io__raw__m_value = KaitaiStream(BytesIO(self._raw__m_value))
                self._m_value = Ttf.Maxp(_io__raw__m_value, self, self._root)
            elif _on == u"glyf":
                self._raw__m_value = io.read_bytes(self.length)
                _io__raw__m_value = KaitaiStream(BytesIO(self._raw__m_value))
                self._m_value = Ttf.Glyf(_io__raw__m_value, self, self._root)
            elif _on == u"fpgm":
                self._raw__m_value = io.read_bytes(self.length)
                _io__raw__m_value = KaitaiStream(BytesIO(self._raw__m_value))
                self._m_value = Ttf.Fpgm(_io__raw__m_value, self, self._root)
            elif _on == u"cmap":
                self._raw__m_value = io.read_bytes(self.length)
                _io__raw__m_value = KaitaiStream(BytesIO(self._raw__m_value))
                self._m_value = Ttf.Cmap(_io__raw__m_value, self, self._root)
            else:
                self._m_value = io.read_bytes(self.length)
            io.seek(_pos)
            return self._m_value if hasattr(self, '_m_value') else None


    class Os2(KaitaiStruct):
        """The OS/2 table consists of a set of metrics that are required by Windows and OS/2."""

        class WeightClass(Enum):
            thin = 100
            extra_light = 200
            light = 300
            normal = 400
            medium = 500
            semi_bold = 600
            bold = 700
            extra_bold = 800
            black = 900

        class WidthClass(Enum):
            ultra_condensed = 1
            extra_condensed = 2
            condensed = 3
            semi_condensed = 4
            normal = 5
            semi_expanded = 6
            expanded = 7
            extra_expanded = 8
            ultra_expanded = 9

        class FsType(Enum):
            restricted_license_embedding = 2
            preview_and_print_embedding = 4
            editable_embedding = 8

        class FsSelection(Enum):
            italic = 1
            underscore = 2
            negative = 4
            outlined = 8
            strikeout = 16
            bold = 32
            regular = 64
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.version = self._io.read_u2be()
            self.x_avg_char_width = self._io.read_s2be()
            self.weight_class = KaitaiStream.resolve_enum(Ttf.Os2.WeightClass, self._io.read_u2be())
            self.width_class = KaitaiStream.resolve_enum(Ttf.Os2.WidthClass, self._io.read_u2be())
            self.fs_type = KaitaiStream.resolve_enum(Ttf.Os2.FsType, self._io.read_s2be())
            self.y_subscript_x_size = self._io.read_s2be()
            self.y_subscript_y_size = self._io.read_s2be()
            self.y_subscript_x_offset = self._io.read_s2be()
            self.y_subscript_y_offset = self._io.read_s2be()
            self.y_superscript_x_size = self._io.read_s2be()
            self.y_superscript_y_size = self._io.read_s2be()
            self.y_superscript_x_offset = self._io.read_s2be()
            self.y_superscript_y_offset = self._io.read_s2be()
            self.y_strikeout_size = self._io.read_s2be()
            self.y_strikeout_position = self._io.read_s2be()
            self.s_family_class = self._io.read_s2be()
            self.panose = Ttf.Os2.Panose(self._io, self, self._root)
            self.unicode_range = Ttf.Os2.UnicodeRange(self._io, self, self._root)
            self.ach_vend_id = (self._io.read_bytes(4)).decode(u"ascii")
            self.selection = KaitaiStream.resolve_enum(Ttf.Os2.FsSelection, self._io.read_u2be())
            self.first_char_index = self._io.read_u2be()
            self.last_char_index = self._io.read_u2be()
            self.typo_ascender = self._io.read_s2be()
            self.typo_descender = self._io.read_s2be()
            self.typo_line_gap = self._io.read_s2be()
            self.win_ascent = self._io.read_u2be()
            self.win_descent = self._io.read_u2be()
            self.code_page_range = Ttf.Os2.CodePageRange(self._io, self, self._root)

        class Panose(KaitaiStruct):

            class Weight(Enum):
                any = 0
                no_fit = 1
                very_light = 2
                light = 3
                thin = 4
                book = 5
                medium = 6
                demi = 7
                bold = 8
                heavy = 9
                black = 10
                nord = 11

            class Proportion(Enum):
                any = 0
                no_fit = 1
                old_style = 2
                modern = 3
                even_width = 4
                expanded = 5
                condensed = 6
                very_expanded = 7
                very_condensed = 8
                monospaced = 9

            class FamilyKind(Enum):
                any = 0
                no_fit = 1
                text_and_display = 2
                script = 3
                decorative = 4
                pictorial = 5

            class LetterForm(Enum):
                any = 0
                no_fit = 1
                normal_contact = 2
                normal_weighted = 3
                normal_boxed = 4
                normal_flattened = 5
                normal_rounded = 6
                normal_off_center = 7
                normal_square = 8
                oblique_contact = 9
                oblique_weighted = 10
                oblique_boxed = 11
                oblique_flattened = 12
                oblique_rounded = 13
                oblique_off_center = 14
                oblique_square = 15

            class SerifStyle(Enum):
                any = 0
                no_fit = 1
                cove = 2
                obtuse_cove = 3
                square_cove = 4
                obtuse_square_cove = 5
                square = 6
                thin = 7
                bone = 8
                exaggerated = 9
                triangle = 10
                normal_sans = 11
                obtuse_sans = 12
                perp_sans = 13
                flared = 14
                rounded = 15

            class XHeight(Enum):
                any = 0
                no_fit = 1
                constant_small = 2
                constant_standard = 3
                constant_large = 4
                ducking_small = 5
                ducking_standard = 6
                ducking_large = 7

            class ArmStyle(Enum):
                any = 0
                no_fit = 1
                straight_arms_horizontal = 2
                straight_arms_wedge = 3
                straight_arms_vertical = 4
                straight_arms_single_serif = 5
                straight_arms_double_serif = 6
                non_straight_arms_horizontal = 7
                non_straight_arms_wedge = 8
                non_straight_arms_vertical = 9
                non_straight_arms_single_serif = 10
                non_straight_arms_double_serif = 11

            class StrokeVariation(Enum):
                any = 0
                no_fit = 1
                gradual_diagonal = 2
                gradual_transitional = 3
                gradual_vertical = 4
                gradual_horizontal = 5
                rapid_vertical = 6
                rapid_horizontal = 7
                instant_vertical = 8

            class Contrast(Enum):
                any = 0
                no_fit = 1
                none = 2
                very_low = 3
                low = 4
                medium_low = 5
                medium = 6
                medium_high = 7
                high = 8
                very_high = 9

            class Midline(Enum):
                any = 0
                no_fit = 1
                standard_trimmed = 2
                standard_pointed = 3
                standard_serifed = 4
                high_trimmed = 5
                high_pointed = 6
                high_serifed = 7
                constant_trimmed = 8
                constant_pointed = 9
                constant_serifed = 10
                low_trimmed = 11
                low_pointed = 12
                low_serifed = 13
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.family_type = KaitaiStream.resolve_enum(Ttf.Os2.Panose.FamilyKind, self._io.read_u1())
                self.serif_style = KaitaiStream.resolve_enum(Ttf.Os2.Panose.SerifStyle, self._io.read_u1())
                self.weight = KaitaiStream.resolve_enum(Ttf.Os2.Panose.Weight, self._io.read_u1())
                self.proportion = KaitaiStream.resolve_enum(Ttf.Os2.Panose.Proportion, self._io.read_u1())
                self.contrast = KaitaiStream.resolve_enum(Ttf.Os2.Panose.Contrast, self._io.read_u1())
                self.stroke_variation = KaitaiStream.resolve_enum(Ttf.Os2.Panose.StrokeVariation, self._io.read_u1())
                self.arm_style = KaitaiStream.resolve_enum(Ttf.Os2.Panose.ArmStyle, self._io.read_u1())
                self.letter_form = KaitaiStream.resolve_enum(Ttf.Os2.Panose.LetterForm, self._io.read_u1())
                self.midline = KaitaiStream.resolve_enum(Ttf.Os2.Panose.Midline, self._io.read_u1())
                self.x_height = KaitaiStream.resolve_enum(Ttf.Os2.Panose.XHeight, self._io.read_u1())


        class UnicodeRange(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.basic_latin = self._io.read_bits_int_be(1) != 0
                self.latin_1_supplement = self._io.read_bits_int_be(1) != 0
                self.latin_extended_a = self._io.read_bits_int_be(1) != 0
                self.latin_extended_b = self._io.read_bits_int_be(1) != 0
                self.ipa_extensions = self._io.read_bits_int_be(1) != 0
                self.spacing_modifier_letters = self._io.read_bits_int_be(1) != 0
                self.combining_diacritical_marks = self._io.read_bits_int_be(1) != 0
                self.basic_greek = self._io.read_bits_int_be(1) != 0
                self.greek_symbols_and_coptic = self._io.read_bits_int_be(1) != 0
                self.cyrillic = self._io.read_bits_int_be(1) != 0
                self.armenian = self._io.read_bits_int_be(1) != 0
                self.basic_hebrew = self._io.read_bits_int_be(1) != 0
                self.hebrew_extended = self._io.read_bits_int_be(1) != 0
                self.basic_arabic = self._io.read_bits_int_be(1) != 0
                self.arabic_extended = self._io.read_bits_int_be(1) != 0
                self.devanagari = self._io.read_bits_int_be(1) != 0
                self.bengali = self._io.read_bits_int_be(1) != 0
                self.gurmukhi = self._io.read_bits_int_be(1) != 0
                self.gujarati = self._io.read_bits_int_be(1) != 0
                self.oriya = self._io.read_bits_int_be(1) != 0
                self.tamil = self._io.read_bits_int_be(1) != 0
                self.telugu = self._io.read_bits_int_be(1) != 0
                self.kannada = self._io.read_bits_int_be(1) != 0
                self.malayalam = self._io.read_bits_int_be(1) != 0
                self.thai = self._io.read_bits_int_be(1) != 0
                self.lao = self._io.read_bits_int_be(1) != 0
                self.basic_georgian = self._io.read_bits_int_be(1) != 0
                self.georgian_extended = self._io.read_bits_int_be(1) != 0
                self.hangul_jamo = self._io.read_bits_int_be(1) != 0
                self.latin_extended_additional = self._io.read_bits_int_be(1) != 0
                self.greek_extended = self._io.read_bits_int_be(1) != 0
                self.general_punctuation = self._io.read_bits_int_be(1) != 0
                self.superscripts_and_subscripts = self._io.read_bits_int_be(1) != 0
                self.currency_symbols = self._io.read_bits_int_be(1) != 0
                self.combining_diacritical_marks_for_symbols = self._io.read_bits_int_be(1) != 0
                self.letterlike_symbols = self._io.read_bits_int_be(1) != 0
                self.number_forms = self._io.read_bits_int_be(1) != 0
                self.arrows = self._io.read_bits_int_be(1) != 0
                self.mathematical_operators = self._io.read_bits_int_be(1) != 0
                self.miscellaneous_technical = self._io.read_bits_int_be(1) != 0
                self.control_pictures = self._io.read_bits_int_be(1) != 0
                self.optical_character_recognition = self._io.read_bits_int_be(1) != 0
                self.enclosed_alphanumerics = self._io.read_bits_int_be(1) != 0
                self.box_drawing = self._io.read_bits_int_be(1) != 0
                self.block_elements = self._io.read_bits_int_be(1) != 0
                self.geometric_shapes = self._io.read_bits_int_be(1) != 0
                self.miscellaneous_symbols = self._io.read_bits_int_be(1) != 0
                self.dingbats = self._io.read_bits_int_be(1) != 0
                self.cjk_symbols_and_punctuation = self._io.read_bits_int_be(1) != 0
                self.hiragana = self._io.read_bits_int_be(1) != 0
                self.katakana = self._io.read_bits_int_be(1) != 0
                self.bopomofo = self._io.read_bits_int_be(1) != 0
                self.hangul_compatibility_jamo = self._io.read_bits_int_be(1) != 0
                self.cjk_miscellaneous = self._io.read_bits_int_be(1) != 0
                self.enclosed_cjk_letters_and_months = self._io.read_bits_int_be(1) != 0
                self.cjk_compatibility = self._io.read_bits_int_be(1) != 0
                self.hangul = self._io.read_bits_int_be(1) != 0
                self.reserved_for_unicode_subranges1 = self._io.read_bits_int_be(1) != 0
                self.reserved_for_unicode_subranges2 = self._io.read_bits_int_be(1) != 0
                self.cjk_unified_ideographs = self._io.read_bits_int_be(1) != 0
                self.private_use_area = self._io.read_bits_int_be(1) != 0
                self.cjk_compatibility_ideographs = self._io.read_bits_int_be(1) != 0
                self.alphabetic_presentation_forms = self._io.read_bits_int_be(1) != 0
                self.arabic_presentation_forms_a = self._io.read_bits_int_be(1) != 0
                self.combining_half_marks = self._io.read_bits_int_be(1) != 0
                self.cjk_compatibility_forms = self._io.read_bits_int_be(1) != 0
                self.small_form_variants = self._io.read_bits_int_be(1) != 0
                self.arabic_presentation_forms_b = self._io.read_bits_int_be(1) != 0
                self.halfwidth_and_fullwidth_forms = self._io.read_bits_int_be(1) != 0
                self.specials = self._io.read_bits_int_be(1) != 0
                self._io.align_to_byte()
                self.reserved = self._io.read_bytes(7)


        class CodePageRange(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.symbol_character_set = self._io.read_bits_int_be(1) != 0
                self.oem_character_set = self._io.read_bits_int_be(1) != 0
                self.macintosh_character_set = self._io.read_bits_int_be(1) != 0
                self.reserved_for_alternate_ansi_oem = self._io.read_bits_int_be(7)
                self.cp1361_korean_johab = self._io.read_bits_int_be(1) != 0
                self.cp950_chinese_traditional_chars_taiwan_and_hong_kong = self._io.read_bits_int_be(1) != 0
                self.cp949_korean_wansung = self._io.read_bits_int_be(1) != 0
                self.cp936_chinese_simplified_chars_prc_and_singapore = self._io.read_bits_int_be(1) != 0
                self.cp932_jis_japan = self._io.read_bits_int_be(1) != 0
                self.cp874_thai = self._io.read_bits_int_be(1) != 0
                self.reserved_for_alternate_ansi = self._io.read_bits_int_be(8)
                self.cp1257_windows_baltic = self._io.read_bits_int_be(1) != 0
                self.cp1256_arabic = self._io.read_bits_int_be(1) != 0
                self.cp1255_hebrew = self._io.read_bits_int_be(1) != 0
                self.cp1254_turkish = self._io.read_bits_int_be(1) != 0
                self.cp1253_greek = self._io.read_bits_int_be(1) != 0
                self.cp1251_cyrillic = self._io.read_bits_int_be(1) != 0
                self.cp1250_latin_2_eastern_europe = self._io.read_bits_int_be(1) != 0
                self.cp1252_latin_1 = self._io.read_bits_int_be(1) != 0
                self.cp437_us = self._io.read_bits_int_be(1) != 0
                self.cp850_we_latin_1 = self._io.read_bits_int_be(1) != 0
                self.cp708_arabic_asmo_708 = self._io.read_bits_int_be(1) != 0
                self.cp737_greek_former_437_g = self._io.read_bits_int_be(1) != 0
                self.cp775_ms_dos_baltic = self._io.read_bits_int_be(1) != 0
                self.cp852_latin_2 = self._io.read_bits_int_be(1) != 0
                self.cp855_ibm_cyrillic_primarily_russian = self._io.read_bits_int_be(1) != 0
                self.cp857_ibm_turkish = self._io.read_bits_int_be(1) != 0
                self.cp860_ms_dos_portuguese = self._io.read_bits_int_be(1) != 0
                self.cp861_ms_dos_icelandic = self._io.read_bits_int_be(1) != 0
                self.cp862_hebrew = self._io.read_bits_int_be(1) != 0
                self.cp863_ms_dos_canadian_french = self._io.read_bits_int_be(1) != 0
                self.cp864_arabic = self._io.read_bits_int_be(1) != 0
                self.cp865_ms_dos_nordic = self._io.read_bits_int_be(1) != 0
                self.cp866_ms_dos_russian = self._io.read_bits_int_be(1) != 0
                self.cp869_ibm_greek = self._io.read_bits_int_be(1) != 0
                self.reserved_for_oem = self._io.read_bits_int_be(16)



    class Fixed(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.major = self._io.read_u2be()
            self.minor = self._io.read_u2be()


    class Glyf(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.number_of_contours = self._io.read_s2be()
            self.x_min = self._io.read_s2be()
            self.y_min = self._io.read_s2be()
            self.x_max = self._io.read_s2be()
            self.y_max = self._io.read_s2be()
            if self.number_of_contours > 0:
                self.value = Ttf.Glyf.SimpleGlyph(self._io, self, self._root)


        class SimpleGlyph(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.end_pts_of_contours = [None] * (self._parent.number_of_contours)
                for i in range(self._parent.number_of_contours):
                    self.end_pts_of_contours[i] = self._io.read_u2be()

                self.instruction_length = self._io.read_u2be()
                self.instructions = self._io.read_bytes(self.instruction_length)
                self.flags = [None] * (self.point_count)
                for i in range(self.point_count):
                    self.flags[i] = Ttf.Glyf.SimpleGlyph.Flag(self._io, self, self._root)


            class Flag(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.reserved = self._io.read_bits_int_be(2)
                    self.y_is_same = self._io.read_bits_int_be(1) != 0
                    self.x_is_same = self._io.read_bits_int_be(1) != 0
                    self.repeat = self._io.read_bits_int_be(1) != 0
                    self.y_short_vector = self._io.read_bits_int_be(1) != 0
                    self.x_short_vector = self._io.read_bits_int_be(1) != 0
                    self.on_curve = self._io.read_bits_int_be(1) != 0
                    self._io.align_to_byte()
                    if self.repeat:
                        self.repeat_value = self._io.read_u1()



            @property
            def point_count(self):
                if hasattr(self, '_m_point_count'):
                    return self._m_point_count if hasattr(self, '_m_point_count') else None

                self._m_point_count = (max(self.end_pts_of_contours) + 1)
                return self._m_point_count if hasattr(self, '_m_point_count') else None



    class Cvt(KaitaiStruct):
        """cvt  - Control Value Table This table contains a list of values that can be referenced by instructions. They can be used, among other things, to control characteristics for different glyphs.
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.fwords = []
            i = 0
            while not self._io.is_eof():
                self.fwords.append(self._io.read_s2be())
                i += 1



    class Maxp(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.table_version_number = Ttf.Fixed(self._io, self, self._root)
            self.num_glyphs = self._io.read_u2be()
            self.max_points = self._io.read_u2be()
            self.max_contours = self._io.read_u2be()
            self.max_composite_points = self._io.read_u2be()
            self.max_composite_contours = self._io.read_u2be()
            self.max_zones = self._io.read_u2be()
            self.max_twilight_points = self._io.read_u2be()
            self.max_storage = self._io.read_u2be()
            self.max_function_defs = self._io.read_u2be()
            self.max_instruction_defs = self._io.read_u2be()
            self.max_stack_elements = self._io.read_u2be()
            self.max_size_of_instructions = self._io.read_u2be()
            self.max_component_elements = self._io.read_u2be()
            self.max_component_depth = self._io.read_u2be()


    class OffsetTable(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.sfnt_version = Ttf.Fixed(self._io, self, self._root)
            self.num_tables = self._io.read_u2be()
            self.search_range = self._io.read_u2be()
            self.entry_selector = self._io.read_u2be()
            self.range_shift = self._io.read_u2be()


    class Cmap(KaitaiStruct):
        """cmap - Character To Glyph Index Mapping Table This table defines the mapping of character codes to the glyph index values used in the font.
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.version_number = self._io.read_u2be()
            self.number_of_encoding_tables = self._io.read_u2be()
            self.tables = [None] * (self.number_of_encoding_tables)
            for i in range(self.number_of_encoding_tables):
                self.tables[i] = Ttf.Cmap.SubtableHeader(self._io, self, self._root)


        class SubtableHeader(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.platform_id = self._io.read_u2be()
                self.encoding_id = self._io.read_u2be()
                self.subtable_offset = self._io.read_u4be()

            @property
            def table(self):
                if hasattr(self, '_m_table'):
                    return self._m_table if hasattr(self, '_m_table') else None

                io = self._parent._io
                _pos = io.pos()
                io.seek(self.subtable_offset)
                self._m_table = Ttf.Cmap.Subtable(io, self, self._root)
                io.seek(_pos)
                return self._m_table if hasattr(self, '_m_table') else None


        class Subtable(KaitaiStruct):

            class SubtableFormat(Enum):
                byte_encoding_table = 0
                high_byte_mapping_through_table = 2
                segment_mapping_to_delta_values = 4
                trimmed_table_mapping = 6
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.format = KaitaiStream.resolve_enum(Ttf.Cmap.Subtable.SubtableFormat, self._io.read_u2be())
                self.length = self._io.read_u2be()
                self.version = self._io.read_u2be()
                _on = self.format
                if _on == Ttf.Cmap.Subtable.SubtableFormat.byte_encoding_table:
                    self._raw_value = self._io.read_bytes((self.length - 6))
                    _io__raw_value = KaitaiStream(BytesIO(self._raw_value))
                    self.value = Ttf.Cmap.Subtable.ByteEncodingTable(_io__raw_value, self, self._root)
                elif _on == Ttf.Cmap.Subtable.SubtableFormat.segment_mapping_to_delta_values:
                    self._raw_value = self._io.read_bytes((self.length - 6))
                    _io__raw_value = KaitaiStream(BytesIO(self._raw_value))
                    self.value = Ttf.Cmap.Subtable.SegmentMappingToDeltaValues(_io__raw_value, self, self._root)
                elif _on == Ttf.Cmap.Subtable.SubtableFormat.high_byte_mapping_through_table:
                    self._raw_value = self._io.read_bytes((self.length - 6))
                    _io__raw_value = KaitaiStream(BytesIO(self._raw_value))
                    self.value = Ttf.Cmap.Subtable.HighByteMappingThroughTable(_io__raw_value, self, self._root)
                elif _on == Ttf.Cmap.Subtable.SubtableFormat.trimmed_table_mapping:
                    self._raw_value = self._io.read_bytes((self.length - 6))
                    _io__raw_value = KaitaiStream(BytesIO(self._raw_value))
                    self.value = Ttf.Cmap.Subtable.TrimmedTableMapping(_io__raw_value, self, self._root)
                else:
                    self.value = self._io.read_bytes((self.length - 6))

            class ByteEncodingTable(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.glyph_id_array = self._io.read_bytes(256)


            class HighByteMappingThroughTable(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.sub_header_keys = [None] * (256)
                    for i in range(256):
                        self.sub_header_keys[i] = self._io.read_u2be()



            class SegmentMappingToDeltaValues(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.seg_count_x2 = self._io.read_u2be()
                    self.search_range = self._io.read_u2be()
                    self.entry_selector = self._io.read_u2be()
                    self.range_shift = self._io.read_u2be()
                    self.end_count = [None] * (self.seg_count)
                    for i in range(self.seg_count):
                        self.end_count[i] = self._io.read_u2be()

                    self.reserved_pad = self._io.read_u2be()
                    self.start_count = [None] * (self.seg_count)
                    for i in range(self.seg_count):
                        self.start_count[i] = self._io.read_u2be()

                    self.id_delta = [None] * (self.seg_count)
                    for i in range(self.seg_count):
                        self.id_delta[i] = self._io.read_u2be()

                    self.id_range_offset = [None] * (self.seg_count)
                    for i in range(self.seg_count):
                        self.id_range_offset[i] = self._io.read_u2be()

                    self.glyph_id_array = []
                    i = 0
                    while not self._io.is_eof():
                        self.glyph_id_array.append(self._io.read_u2be())
                        i += 1


                @property
                def seg_count(self):
                    if hasattr(self, '_m_seg_count'):
                        return self._m_seg_count if hasattr(self, '_m_seg_count') else None

                    self._m_seg_count = self.seg_count_x2 // 2
                    return self._m_seg_count if hasattr(self, '_m_seg_count') else None


            class TrimmedTableMapping(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.first_code = self._io.read_u2be()
                    self.entry_count = self._io.read_u2be()
                    self.glyph_id_array = [None] * (self.entry_count)
                    for i in range(self.entry_count):
                        self.glyph_id_array[i] = self._io.read_u2be()






