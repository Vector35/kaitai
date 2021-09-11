# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Warcraft2Pud(KaitaiStruct):
    """Warcraft II game engine uses this format for map files. External
    maps can be edited by official Warcraft II map editor and saved in
    .pud files. Maps supplied with the game (i.e. single player
    campaign) follow the same format, but are instead embedded inside
    the game container files.
    
    There are two major versions: 0x11 (original one) and 0x13 (roughly
    corresponds to v1.33 of the game engine, although some of the
    features got limited support in v1.3).
    
    File consists of a sequence of typed sections.
    
    .. seealso::
       Source - http://cade.datamax.bg/war2x/pudspec.html
    """

    class Controller(Enum):
        computer = 1
        passive_computer = 2
        nobody = 3
        computer = 4
        human = 5
        rescue_passive = 6
        rescue_active = 7

    class TerrainType(Enum):
        forest = 0
        winter = 1
        wasteland = 2
        swamp = 3

    class UnitType(Enum):
        infantry = 0
        grunt = 1
        peasant = 2
        peon = 3
        ballista = 4
        catapult = 5
        knight = 6
        ogre = 7
        archer = 8
        axethrower = 9
        mage = 10
        death_knight = 11
        paladin = 12
        ogre_mage = 13
        dwarves = 14
        goblin_sapper = 15
        attack_peasant = 16
        attack_peon = 17
        ranger = 18
        berserker = 19
        alleria = 20
        teron_gorefiend = 21
        kurdan_and_sky_ree = 22
        dentarg = 23
        khadgar = 24
        grom_hellscream = 25
        human_tanker = 26
        orc_tanker = 27
        human_transport = 28
        orc_transport = 29
        elven_destroyer = 30
        troll_destroyer = 31
        battleship = 32
        juggernaught = 33
        deathwing = 35
        gnomish_submarine = 38
        giant_turtle = 39
        gnomish_flying_machine = 40
        goblin_zepplin = 41
        gryphon_rider = 42
        dragon = 43
        turalyon = 44
        eye_of_kilrogg = 45
        danath = 46
        khorgath_bladefist = 47
        cho_gall = 49
        lothar = 50
        gul_dan = 51
        uther_lightbringer = 52
        zuljin = 53
        skeleton = 55
        daemon = 56
        critter = 57
        farm = 58
        pig_farm = 59
        human_barracks = 60
        orc_barracks = 61
        church = 62
        altar_of_storms = 63
        human_scout_tower = 64
        orc_scout_tower = 65
        stables = 66
        ogre_mound = 67
        gnomish_inventor = 68
        goblin_alchemist = 69
        gryphon_aviary = 70
        dragon_roost = 71
        human_shipyard = 72
        orc_shipyard = 73
        town_hall = 74
        great_hall = 75
        elven_lumber_mill = 76
        troll_lumber_mill = 77
        human_foundry = 78
        orc_foundry = 79
        mage_tower = 80
        temple_of_the_damned = 81
        human_blacksmith = 82
        orc_blacksmith = 83
        human_refinery = 84
        orc_refinery = 85
        human_oil_well = 86
        orc_oil_well = 87
        keep = 88
        stronghold = 89
        castle = 90
        fortress = 91
        gold_mine = 92
        oil_patch = 93
        human_start = 94
        orc_start = 95
        human_guard_tower = 96
        orc_guard_tower = 97
        human_cannon_tower = 98
        orc_cannon_tower = 99
        circle_of_power = 100
        dark_portal = 101
        runestone = 102
        human_wall = 103
        orc_wall = 104
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.sections = []
        i = 0
        while not self._io.is_eof():
            self.sections.append(Warcraft2Pud.Section(self._io, self, self._root))
            i += 1


    class SectionStartingResource(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.resources_by_player = []
            i = 0
            while not self._io.is_eof():
                self.resources_by_player.append(self._io.read_u2le())
                i += 1



    class SectionEra(KaitaiStruct):
        """Section that specifies terrain type for this map."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.terrain = KaitaiStream.resolve_enum(Warcraft2Pud.TerrainType, self._io.read_u2le())


    class SectionVer(KaitaiStruct):
        """Section that specifies format version."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.version = self._io.read_u2le()


    class SectionDim(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_u2le()
            self.y = self._io.read_u2le()


    class SectionType(KaitaiStruct):
        """Section that confirms that this file is a "map file" by certain
        magic string and supplies a tag that could be used in
        multiplayer to check that all player use the same version of the
        map.
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(10)
            if not self.magic == b"\x57\x41\x52\x32\x20\x4D\x41\x50\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x57\x41\x52\x32\x20\x4D\x41\x50\x00\x00", self.magic, self._io, u"/types/section_type/seq/0")
            self.unused = self._io.read_bytes(2)
            self.id_tag = self._io.read_u4le()


    class SectionUnit(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.units = []
            i = 0
            while not self._io.is_eof():
                self.units.append(Warcraft2Pud.Unit(self._io, self, self._root))
                i += 1



    class Section(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = (self._io.read_bytes(4)).decode(u"ASCII")
            self.size = self._io.read_u4le()
            _on = self.name
            if _on == u"SLBR":
                self._raw_body = self._io.read_bytes(self.size)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Warcraft2Pud.SectionStartingResource(_io__raw_body, self, self._root)
            elif _on == u"ERAX":
                self._raw_body = self._io.read_bytes(self.size)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Warcraft2Pud.SectionEra(_io__raw_body, self, self._root)
            elif _on == u"OWNR":
                self._raw_body = self._io.read_bytes(self.size)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Warcraft2Pud.SectionOwnr(_io__raw_body, self, self._root)
            elif _on == u"ERA ":
                self._raw_body = self._io.read_bytes(self.size)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Warcraft2Pud.SectionEra(_io__raw_body, self, self._root)
            elif _on == u"SGLD":
                self._raw_body = self._io.read_bytes(self.size)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Warcraft2Pud.SectionStartingResource(_io__raw_body, self, self._root)
            elif _on == u"VER ":
                self._raw_body = self._io.read_bytes(self.size)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Warcraft2Pud.SectionVer(_io__raw_body, self, self._root)
            elif _on == u"SOIL":
                self._raw_body = self._io.read_bytes(self.size)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Warcraft2Pud.SectionStartingResource(_io__raw_body, self, self._root)
            elif _on == u"UNIT":
                self._raw_body = self._io.read_bytes(self.size)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Warcraft2Pud.SectionUnit(_io__raw_body, self, self._root)
            elif _on == u"DIM ":
                self._raw_body = self._io.read_bytes(self.size)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Warcraft2Pud.SectionDim(_io__raw_body, self, self._root)
            elif _on == u"TYPE":
                self._raw_body = self._io.read_bytes(self.size)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Warcraft2Pud.SectionType(_io__raw_body, self, self._root)
            else:
                self.body = self._io.read_bytes(self.size)


    class SectionOwnr(KaitaiStruct):
        """Section that specifies who controls each player."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.controller_by_player = []
            i = 0
            while not self._io.is_eof():
                self.controller_by_player.append(KaitaiStream.resolve_enum(Warcraft2Pud.Controller, self._io.read_u1()))
                i += 1



    class Unit(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_u2le()
            self.y = self._io.read_u2le()
            self.u_type = KaitaiStream.resolve_enum(Warcraft2Pud.UnitType, self._io.read_u1())
            self.owner = self._io.read_u1()
            self.options = self._io.read_u2le()

        @property
        def resource(self):
            if hasattr(self, '_m_resource'):
                return self._m_resource if hasattr(self, '_m_resource') else None

            if  ((self.u_type == Warcraft2Pud.UnitType.gold_mine) or (self.u_type == Warcraft2Pud.UnitType.human_oil_well) or (self.u_type == Warcraft2Pud.UnitType.orc_oil_well) or (self.u_type == Warcraft2Pud.UnitType.oil_patch)) :
                self._m_resource = (self.options * 2500)

            return self._m_resource if hasattr(self, '_m_resource') else None



