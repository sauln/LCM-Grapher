"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

class pwr_mntr_t(object):
    __slots__ = ["utime", "volts", "amps", "watts", "watt_hrs"]

    def __init__(self):
        self.utime = 0
        self.volts = 0.0
        self.amps = 0.0
        self.watts = 0.0
        self.watt_hrs = 0.0

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(pwr_mntr_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qfddd", self.utime, self.volts, self.amps, self.watts, self.watt_hrs))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != pwr_mntr_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return pwr_mntr_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = pwr_mntr_t()
        self.utime, self.volts, self.amps, self.watts, self.watt_hrs = struct.unpack(">qfddd", buf.read(36))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if pwr_mntr_t in parents: return 0
        tmphash = (0xe1a0c85922aa6554) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if pwr_mntr_t._packed_fingerprint is None:
            pwr_mntr_t._packed_fingerprint = struct.pack(">Q", pwr_mntr_t._get_hash_recursive([]))
        return pwr_mntr_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

