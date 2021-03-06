"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

class analogin_t(object):
    __slots__ = ["utime", "first_channel", "last_channel", "num_channels", "voltages"]

    def __init__(self):
        self.utime = 0
        self.first_channel = 0
        self.last_channel = 0
        self.num_channels = 0
        self.voltages = []

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(analogin_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qbbb", self.utime, self.first_channel, self.last_channel, self.num_channels))
        buf.write(struct.pack('>%dd' % self.num_channels, *self.voltages[:self.num_channels]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != analogin_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return analogin_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = analogin_t()
        self.utime, self.first_channel, self.last_channel, self.num_channels = struct.unpack(">qbbb", buf.read(11))
        self.voltages = struct.unpack('>%dd' % self.num_channels, buf.read(self.num_channels * 8))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if analogin_t in parents: return 0
        tmphash = (0x56f5f6cde4016849) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if analogin_t._packed_fingerprint is None:
            analogin_t._packed_fingerprint = struct.pack(">Q", analogin_t._get_hash_recursive([]))
        return analogin_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

