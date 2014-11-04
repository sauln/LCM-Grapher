"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

class tthrust_cmd_t(object):
    __slots__ = ["utime", "port", "stbd"]

    def __init__(self):
        self.utime = 0
        self.port = 0.0
        self.stbd = 0.0

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(tthrust_cmd_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qff", self.utime, self.port, self.stbd))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != tthrust_cmd_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return tthrust_cmd_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = tthrust_cmd_t()
        self.utime, self.port, self.stbd = struct.unpack(">qff", buf.read(16))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if tthrust_cmd_t in parents: return 0
        tmphash = (0x73ac062e94788630) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if tthrust_cmd_t._packed_fingerprint is None:
            tthrust_cmd_t._packed_fingerprint = struct.pack(">Q", tthrust_cmd_t._get_hash_recursive([]))
        return tthrust_cmd_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

