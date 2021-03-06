"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

class imu_45_nav_t(object):
    __slots__ = ["utime", "filter_state", "dynamics_mode", "status_flags", "pos_valid_flags", "latitude", "longitude", "ellipsoid_height", "vel_valid_flags", "north", "east", "down", "euler_valid_flags", "roll", "pitch", "yaw", "pos_unc_valid_flags", "north_pos_unc", "east_pos_unc", "down_pos_unc", "vel_unc_valid_flags", "north_vel_unc", "east_vel_unc", "down_vel_unc"]

    def __init__(self):
        self.utime = 0
        self.filter_state = 0
        self.dynamics_mode = 0
        self.status_flags = 0
        self.pos_valid_flags = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.ellipsoid_height = 0.0
        self.vel_valid_flags = 0
        self.north = 0.0
        self.east = 0.0
        self.down = 0.0
        self.euler_valid_flags = 0
        self.roll = 0.0
        self.pitch = 0.0
        self.yaw = 0.0
        self.pos_unc_valid_flags = 0
        self.north_pos_unc = 0.0
        self.east_pos_unc = 0.0
        self.down_pos_unc = 0.0
        self.vel_unc_valid_flags = 0
        self.north_vel_unc = 0.0
        self.east_vel_unc = 0.0
        self.down_vel_unc = 0.0

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(imu_45_nav_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qhhhhdddhfffhfffhfffhfff", self.utime, self.filter_state, self.dynamics_mode, self.status_flags, self.pos_valid_flags, self.latitude, self.longitude, self.ellipsoid_height, self.vel_valid_flags, self.north, self.east, self.down, self.euler_valid_flags, self.roll, self.pitch, self.yaw, self.pos_unc_valid_flags, self.north_pos_unc, self.east_pos_unc, self.down_pos_unc, self.vel_unc_valid_flags, self.north_vel_unc, self.east_vel_unc, self.down_vel_unc))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != imu_45_nav_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return imu_45_nav_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = imu_45_nav_t()
        self.utime, self.filter_state, self.dynamics_mode, self.status_flags, self.pos_valid_flags, self.latitude, self.longitude, self.ellipsoid_height, self.vel_valid_flags, self.north, self.east, self.down, self.euler_valid_flags, self.roll, self.pitch, self.yaw, self.pos_unc_valid_flags, self.north_pos_unc, self.east_pos_unc, self.down_pos_unc, self.vel_unc_valid_flags, self.north_vel_unc, self.east_vel_unc, self.down_vel_unc = struct.unpack(">qhhhhdddhfffhfffhfffhfff", buf.read(96))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if imu_45_nav_t in parents: return 0
        tmphash = (0x8d9208739c54da4b) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if imu_45_nav_t._packed_fingerprint is None:
            imu_45_nav_t._packed_fingerprint = struct.pack(">Q", imu_45_nav_t._get_hash_recursive([]))
        return imu_45_nav_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

