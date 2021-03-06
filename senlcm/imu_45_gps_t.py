"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

class imu_45_gps_t(object):
    __slots__ = ["utime", "pos_valid_flags", "latitude", "longitude", "ellipsoid_height", "horizontal_accuracy", "vertical_accuracy", "v", "speed", "ground_speed", "heading", "speed_accuracy", "heading_accuracy", "vel_valid_flags"]

    def __init__(self):
        self.utime = 0
        self.pos_valid_flags = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.ellipsoid_height = 0.0
        self.horizontal_accuracy = 0.0
        self.vertical_accuracy = 0.0
        self.v = [ 0.0 for dim0 in range(3) ]
        self.speed = 0.0
        self.ground_speed = 0.0
        self.heading = 0.0
        self.speed_accuracy = 0.0
        self.heading_accuracy = 0.0
        self.vel_valid_flags = 0

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(imu_45_gps_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qhdddff", self.utime, self.pos_valid_flags, self.latitude, self.longitude, self.ellipsoid_height, self.horizontal_accuracy, self.vertical_accuracy))
        buf.write(struct.pack('>3f', *self.v[:3]))
        buf.write(struct.pack(">fffffh", self.speed, self.ground_speed, self.heading, self.speed_accuracy, self.heading_accuracy, self.vel_valid_flags))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != imu_45_gps_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return imu_45_gps_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = imu_45_gps_t()
        self.utime, self.pos_valid_flags, self.latitude, self.longitude, self.ellipsoid_height, self.horizontal_accuracy, self.vertical_accuracy = struct.unpack(">qhdddff", buf.read(42))
        self.v = struct.unpack('>3f', buf.read(12))
        self.speed, self.ground_speed, self.heading, self.speed_accuracy, self.heading_accuracy, self.vel_valid_flags = struct.unpack(">fffffh", buf.read(22))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if imu_45_gps_t in parents: return 0
        tmphash = (0x20cedb2a403c2d93) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if imu_45_gps_t._packed_fingerprint is None:
            imu_45_gps_t._packed_fingerprint = struct.pack(">Q", imu_45_gps_t._get_hash_recursive([]))
        return imu_45_gps_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

