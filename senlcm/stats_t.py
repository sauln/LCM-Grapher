"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

class stats_t(object):
    __slots__ = ["utime", "ntimeouts", "ngood", "nbad", "dt", "dtmax", "latency", "latencymax"]

    def __init__(self):
        self.utime = 0
        self.ntimeouts = 0
        self.ngood = 0
        self.nbad = 0
        self.dt = 0
        self.dtmax = 0
        self.latency = 0
        self.latencymax = 0

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(stats_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qiiiiiii", self.utime, self.ntimeouts, self.ngood, self.nbad, self.dt, self.dtmax, self.latency, self.latencymax))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != stats_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return stats_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = stats_t()
        self.utime, self.ntimeouts, self.ngood, self.nbad, self.dt, self.dtmax, self.latency, self.latencymax = struct.unpack(">qiiiiiii", buf.read(36))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if stats_t in parents: return 0
        tmphash = (0x557f1249354d04ec) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if stats_t._packed_fingerprint is None:
            stats_t._packed_fingerprint = struct.pack(">Q", stats_t._get_hash_recursive([]))
        return stats_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)
