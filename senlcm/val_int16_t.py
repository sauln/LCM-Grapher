"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

class val_int16_t(object):
    __slots__ = ["utime", "val"]

    def __init__(self):
        self.utime = 0
        self.val = 0

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(val_int16_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qh", self.utime, self.val))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != val_int16_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return val_int16_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = val_int16_t()
        self.utime, self.val = struct.unpack(">qh", buf.read(10))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if val_int16_t in parents: return 0
        tmphash = (0x63bd44d4089e37d3) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if val_int16_t._packed_fingerprint is None:
            val_int16_t._packed_fingerprint = struct.pack(">Q", val_int16_t._get_hash_recursive([]))
        return val_int16_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

