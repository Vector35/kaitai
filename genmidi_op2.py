# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class GenmidiOp2(KaitaiStruct):
    """GENMIDI.OP2 is a sound bank file used by players based on DMX sound
    library to play MIDI files with General MIDI instruments using OPL2
    sound chip (which was commonly installed on popular AdLib and Sound
    Blaster sound cards).
    
    Major users of DMX sound library include:
    
    * Original Doom game engine (and games based on it: Heretic, Hexen, Strife, Chex Quest)
    * Raptor: Call of the Shadows 
    
    .. seealso::
       http://doom.wikia.com/wiki/GENMIDI - http://www.fit.vutbr.cz/~arnost/muslib/op2_form.zip
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(8)
        if not self.magic == b"\x23\x4F\x50\x4C\x5F\x49\x49\x23":
            raise kaitaistruct.ValidationNotEqualError(b"\x23\x4F\x50\x4C\x5F\x49\x49\x23", self.magic, self._io, u"/seq/0")
        self.instruments = [None] * (175)
        for i in range(175):
            self.instruments[i] = GenmidiOp2.InstrumentEntry(self._io, self, self._root)

        self.instrument_names = [None] * (175)
        for i in range(175):
            self.instrument_names[i] = (KaitaiStream.bytes_terminate(KaitaiStream.bytes_strip_right(self._io.read_bytes(32), 0), 0, False)).decode(u"ASCII")


    class InstrumentEntry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.flags = self._io.read_u2le()
            self.finetune = self._io.read_u1()
            self.note = self._io.read_u1()
            self.instruments = [None] * (2)
            for i in range(2):
                self.instruments[i] = GenmidiOp2.Instrument(self._io, self, self._root)



    class Instrument(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.op1 = GenmidiOp2.OpSettings(self._io, self, self._root)
            self.feedback = self._io.read_u1()
            self.op2 = GenmidiOp2.OpSettings(self._io, self, self._root)
            self.unused = self._io.read_u1()
            self.base_note = self._io.read_s2le()


    class OpSettings(KaitaiStruct):
        """OPL2 settings for one operator (carrier or modulator)
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.trem_vibr = self._io.read_u1()
            self.att_dec = self._io.read_u1()
            self.sust_rel = self._io.read_u1()
            self.wave = self._io.read_u1()
            self.scale = self._io.read_u1()
            self.level = self._io.read_u1()



