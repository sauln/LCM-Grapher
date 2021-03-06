"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

class abv_cntrl_t(object):
    __slots__ = ["utime", "fastfill", "slowfill", "vent", "articup", "articdown", "disconnect", "port", "stbd", "lat", "pump"]

    def __init__(self):
        self.utime = 0
        self.fastfill = False
        self.slowfill = False
        self.vent = False
        self.articup = False
        self.articdown = False
        self.disconnect = False
        self.port = 0.0
        self.stbd = 0.0
        self.lat = 0.0
        self.pump = 0.0

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(abv_cntrl_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qbbbbbbffff", self.utime, self.fastfill, self.slowfill, self.vent, self.articup, self.articdown, self.disconnect, self.port, self.stbd, self.lat, self.pump))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != abv_cntrl_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return abv_cntrl_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = abv_cntrl_t()
        self.utime, self.fastfill, self.slowfill, self.vent, self.articup, self.articdown, self.disconnect, self.port, self.stbd, self.lat, self.pump = struct.unpack(">qbbbbbbffff", buf.read(30))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if abv_cntrl_t in parents: return 0
        tmphash = (0x82217bddcc732a3b) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if abv_cntrl_t._packed_fingerprint is None:
            abv_cntrl_t._packed_fingerprint = struct.pack(">Q", abv_cntrl_t._get_hash_recursive([]))
        return abv_cntrl_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

