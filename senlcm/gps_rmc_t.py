"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

class gps_rmc_t(object):
    __slots__ = ["utime", "tt", "lat", "lon", "sog"]

    def __init__(self):
        self.utime = 0
        self.tt = 0
        self.lat = 0.0
        self.lon = 0.0
        self.sog = 0.0

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(gps_rmc_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qiddd", self.utime, self.tt, self.lat, self.lon, self.sog))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != gps_rmc_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return gps_rmc_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = gps_rmc_t()
        self.utime, self.tt, self.lat, self.lon, self.sog = struct.unpack(">qiddd", buf.read(36))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if gps_rmc_t in parents: return 0
        tmphash = (0xee885b27777479de) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if gps_rmc_t._packed_fingerprint is None:
            gps_rmc_t._packed_fingerprint = struct.pack(">Q", gps_rmc_t._get_hash_recursive([]))
        return gps_rmc_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)
