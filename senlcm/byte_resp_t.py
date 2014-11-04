"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

class byte_resp_t(object):
    __slots__ = ["utime", "byte_state"]

    def __init__(self):
        self.utime = 0
        self.byte_state = 0

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(byte_resp_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qb", self.utime, self.byte_state))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != byte_resp_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return byte_resp_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = byte_resp_t()
        self.utime, self.byte_state = struct.unpack(">qb", buf.read(9))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if byte_resp_t in parents: return 0
        tmphash = (0x6a7edef8527c4ea9) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if byte_resp_t._packed_fingerprint is None:
            byte_resp_t._packed_fingerprint = struct.pack(">Q", byte_resp_t._get_hash_recursive([]))
        return byte_resp_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

