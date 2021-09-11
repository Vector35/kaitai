# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class BitcoinTransaction(KaitaiStruct):
    """
    .. seealso::
       Source - https://bitcoin.org/en/developer-guide#transactions
       https://en.bitcoin.it/wiki/Transaction
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.version = self._io.read_u4le()
        self.num_vins = self._io.read_u1()
        self.vins = [None] * (self.num_vins)
        for i in range(self.num_vins):
            self.vins[i] = BitcoinTransaction.Vin(self._io, self, self._root)

        self.num_vouts = self._io.read_u1()
        self.vouts = [None] * (self.num_vouts)
        for i in range(self.num_vouts):
            self.vouts[i] = BitcoinTransaction.Vout(self._io, self, self._root)

        self.locktime = self._io.read_u4le()

    class Vin(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.txid = self._io.read_bytes(32)
            self.output_id = self._io.read_u4le()
            self.len_script = self._io.read_u1()
            self._raw_script_sig = self._io.read_bytes(self.len_script)
            _io__raw_script_sig = KaitaiStream(BytesIO(self._raw_script_sig))
            self.script_sig = BitcoinTransaction.Vin.ScriptSignature(_io__raw_script_sig, self, self._root)
            self.end_of_vin = self._io.read_bytes(4)
            if not self.end_of_vin == b"\xFF\xFF\xFF\xFF":
                raise kaitaistruct.ValidationNotEqualError(b"\xFF\xFF\xFF\xFF", self.end_of_vin, self._io, u"/types/vin/seq/4")

        class ScriptSignature(KaitaiStruct):

            class SighashType(Enum):
                sighash_all = 1
                sighash_none = 2
                sighash_single = 3
                sighash_anyonecanpay = 80
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.len_sig_stack = self._io.read_u1()
                self.der_sig = BitcoinTransaction.Vin.ScriptSignature.DerSignature(self._io, self, self._root)
                self.sig_type = KaitaiStream.resolve_enum(BitcoinTransaction.Vin.ScriptSignature.SighashType, self._io.read_u1())
                self.len_pubkey_stack = self._io.read_u1()
                self.pubkey = BitcoinTransaction.Vin.ScriptSignature.PublicKey(self._io, self, self._root)

            class DerSignature(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.sequence = self._io.read_bytes(1)
                    if not self.sequence == b"\x30":
                        raise kaitaistruct.ValidationNotEqualError(b"\x30", self.sequence, self._io, u"/types/vin/types/script_signature/types/der_signature/seq/0")
                    self.len_sig = self._io.read_u1()
                    self.sep_1 = self._io.read_bytes(1)
                    if not self.sep_1 == b"\x02":
                        raise kaitaistruct.ValidationNotEqualError(b"\x02", self.sep_1, self._io, u"/types/vin/types/script_signature/types/der_signature/seq/2")
                    self.len_sig_r = self._io.read_u1()
                    self.sig_r = self._io.read_bytes(self.len_sig_r)
                    self.sep_2 = self._io.read_bytes(1)
                    if not self.sep_2 == b"\x02":
                        raise kaitaistruct.ValidationNotEqualError(b"\x02", self.sep_2, self._io, u"/types/vin/types/script_signature/types/der_signature/seq/5")
                    self.len_sig_s = self._io.read_u1()
                    self.sig_s = self._io.read_bytes(self.len_sig_s)


            class PublicKey(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.type = self._io.read_u1()
                    self.x = self._io.read_bytes(32)
                    self.y = self._io.read_bytes(32)




    class Vout(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.amount = self._io.read_u8le()
            self.len_script = self._io.read_u1()
            self.script_pub_key = self._io.read_bytes(self.len_script)



