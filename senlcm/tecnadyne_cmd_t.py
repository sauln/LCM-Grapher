"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

class tecnadyne_cmd_t(object):
    __slots__ = ["utime", "port", "stbd", "lat", "pump"]

    def __init__(self):
        self.utime = 0
        self.port = 0.0
        self.stbd = 0.0
        self.lat = 0.0
        self.pump = 0.0

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(tecnadyne_cmd_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qffff", self.utime, self.port, self.stbd, self.lat, self.pump))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != tecnadyne_cmd_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return tecnadyne_cmd_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = tecnadyne_cmd_t()
        self.utime, self.port, self.stbd, self.lat, self.pump = struct.unpack(">qffff", buf.read(24))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if tecnadyne_cmd_t in parents: return 0
        tmphash = (0xa99a6f1941358bf9) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if tecnadyne_cmd_t._packed_fingerprint is None:
            tecnadyne_cmd_t._packed_fingerprint = struct.pack(">Q", tecnadyne_cmd_t._get_hash_recursive([]))
        return tecnadyne_cmd_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

