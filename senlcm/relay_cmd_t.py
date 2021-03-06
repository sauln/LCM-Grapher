"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

class relay_cmd_t(object):
    __slots__ = ["utime", "on_off", "relay"]

    def __init__(self):
        self.utime = 0
        self.on_off = False
        self.relay = 0

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(relay_cmd_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qbh", self.utime, self.on_off, self.relay))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != relay_cmd_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return relay_cmd_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = relay_cmd_t()
        self.utime, self.on_off, self.relay = struct.unpack(">qbh", buf.read(11))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if relay_cmd_t in parents: return 0
        tmphash = (0x356f3f1b55f7114f) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if relay_cmd_t._packed_fingerprint is None:
            relay_cmd_t._packed_fingerprint = struct.pack(">Q", relay_cmd_t._get_hash_recursive([]))
        return relay_cmd_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

