"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

class pose_t(object):
    __slots__ = ["utime", "pose", "state"]

    def __init__(self):
        self.utime = 0
        self.pose = [ 0.0 for dim0 in range(6) ]
        self.state = [ 0.0 for dim0 in range(12) ]

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(pose_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">q", self.utime))
        buf.write(struct.pack('>6d', *self.pose[:6]))
        buf.write(struct.pack('>12d', *self.state[:12]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != pose_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return pose_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = pose_t()
        self.utime = struct.unpack(">q", buf.read(8))[0]
        self.pose = struct.unpack('>6d', buf.read(48))
        self.state = struct.unpack('>12d', buf.read(96))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if pose_t in parents: return 0
        tmphash = (0x9974e32f6ff3d92a) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if pose_t._packed_fingerprint is None:
            pose_t._packed_fingerprint = struct.pack(">Q", pose_t._get_hash_recursive([]))
        return pose_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

