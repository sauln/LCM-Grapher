"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

class analogin_helios_t(object):
    __slots__ = ["utime", "sample", "voltage"]

    def __init__(self):
        self.utime = 0
        self.sample = 0
        self.voltage = 0.0

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(analogin_helios_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qhd", self.utime, self.sample, self.voltage))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != analogin_helios_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return analogin_helios_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = analogin_helios_t()
        self.utime, self.sample, self.voltage = struct.unpack(">qhd", buf.read(18))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if analogin_helios_t in parents: return 0
        tmphash = (0xbf731b6bd406fb8c) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if analogin_helios_t._packed_fingerprint is None:
            analogin_helios_t._packed_fingerprint = struct.pack(">Q", analogin_helios_t._get_hash_recursive([]))
        return analogin_helios_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

