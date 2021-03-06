"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

class bangbang_t(object):
    __slots__ = ["utime", "Goal", "Input", "Error", "DeadbandPos", "DeadbandNeg", "Output"]

    def __init__(self):
        self.utime = 0
        self.Goal = 0.0
        self.Input = 0.0
        self.Error = 0.0
        self.DeadbandPos = 0.0
        self.DeadbandNeg = 0.0
        self.Output = 0

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(bangbang_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qfffffh", self.utime, self.Goal, self.Input, self.Error, self.DeadbandPos, self.DeadbandNeg, self.Output))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != bangbang_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return bangbang_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = bangbang_t()
        self.utime, self.Goal, self.Input, self.Error, self.DeadbandPos, self.DeadbandNeg, self.Output = struct.unpack(">qfffffh", buf.read(30))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if bangbang_t in parents: return 0
        tmphash = (0x8bfd449ca06ba2d9) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if bangbang_t._packed_fingerprint is None:
            bangbang_t._packed_fingerprint = struct.pack(">Q", bangbang_t._get_hash_recursive([]))
        return bangbang_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

