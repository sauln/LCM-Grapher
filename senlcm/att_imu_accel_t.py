"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

class att_imu_accel_t(object):
    __slots__ = ["utime", "accel_x", "accel_y", "accel_z", "angrate_x", "angrate_y", "angrate_z"]

    def __init__(self):
        self.utime = 0
        self.accel_x = 0.0
        self.accel_y = 0.0
        self.accel_z = 0.0
        self.angrate_x = 0.0
        self.angrate_y = 0.0
        self.angrate_z = 0.0

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(att_imu_accel_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qffffff", self.utime, self.accel_x, self.accel_y, self.accel_z, self.angrate_x, self.angrate_y, self.angrate_z))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != att_imu_accel_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return att_imu_accel_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = att_imu_accel_t()
        self.utime, self.accel_x, self.accel_y, self.accel_z, self.angrate_x, self.angrate_y, self.angrate_z = struct.unpack(">qffffff", buf.read(32))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if att_imu_accel_t in parents: return 0
        tmphash = (0x69a2b4ec73f7e85e) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if att_imu_accel_t._packed_fingerprint is None:
            att_imu_accel_t._packed_fingerprint = struct.pack(">Q", att_imu_accel_t._get_hash_recursive([]))
        return att_imu_accel_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

