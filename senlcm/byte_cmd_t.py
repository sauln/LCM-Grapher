"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

class byte_cmd_t(object):
    __slots__ = ["utime", "bit", "on_off"]

    def __init__(self):
        self.utime = 0
        self.bit = 0
        self.on_off = False

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(byte_cmd_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qhb", self.utime, self.bit, self.on_off))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != byte_cmd_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return byte_cmd_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = byte_cmd_t()
        self.utime, self.bit, self.on_off = struct.unpack(">qhb", buf.read(11))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if byte_cmd_t in parents: return 0
        tmphash = (0x3940c986c0b141a2) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if byte_cmd_t._packed_fingerprint is None:
            byte_cmd_t._packed_fingerprint = struct.pack(">Q", byte_cmd_t._get_hash_recursive([]))
        return byte_cmd_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

