"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

class tony_abv_state_t(object):
    __slots__ = ["utime", "lc_p", "lc_s", "lc_t"]

    def __init__(self):
        self.utime = 0
        self.lc_p = 0.0
        self.lc_s = 0.0
        self.lc_t = 0.0

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(tony_abv_state_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qfff", self.utime, self.lc_p, self.lc_s, self.lc_t))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != tony_abv_state_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return tony_abv_state_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = tony_abv_state_t()
        self.utime, self.lc_p, self.lc_s, self.lc_t = struct.unpack(">qfff", buf.read(20))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if tony_abv_state_t in parents: return 0
        tmphash = (0xc50bd1272c2904c3) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if tony_abv_state_t._packed_fingerprint is None:
            tony_abv_state_t._packed_fingerprint = struct.pack(">Q", tony_abv_state_t._get_hash_recursive([]))
        return tony_abv_state_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

