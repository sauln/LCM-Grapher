"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

class positionSim_t(object):
    __slots__ = ["Xhat", "X0", "Xhatdot", "T", "xCoord", "yCoord", "DU", "U0", "DU_p", "V0", "D2U0", "u", "theta", "con"]

    def __init__(self):
        self.Xhat = [ 0.0 for dim0 in range(2) ]
        self.X0 = [ 0.0 for dim0 in range(2) ]
        self.Xhatdot = [ 0.0 for dim0 in range(2) ]
        self.T = 0.0
        self.xCoord = 0.0
        self.yCoord = 0.0
        self.DU = [ 0.0 for dim0 in range(2) ]
        self.U0 = 0.0
        self.DU_p = [ 0.0 for dim0 in range(2) ]
        self.V0 = [ 0.0 for dim0 in range(2) ]
        self.D2U0 = 0.0
        self.u = [ 0.0 for dim0 in range(2) ]
        self.theta = 0.0
        self.con = [ 0.0 for dim0 in range(5) ]

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(positionSim_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack('>2f', *self.Xhat[:2]))
        buf.write(struct.pack('>2f', *self.X0[:2]))
        buf.write(struct.pack('>2f', *self.Xhatdot[:2]))
        buf.write(struct.pack(">fff", self.T, self.xCoord, self.yCoord))
        buf.write(struct.pack('>2f', *self.DU[:2]))
        buf.write(struct.pack(">f", self.U0))
        buf.write(struct.pack('>2f', *self.DU_p[:2]))
        buf.write(struct.pack('>2f', *self.V0[:2]))
        buf.write(struct.pack(">f", self.D2U0))
        buf.write(struct.pack('>2f', *self.u[:2]))
        buf.write(struct.pack(">f", self.theta))
        buf.write(struct.pack('>5f', *self.con[:5]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != positionSim_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return positionSim_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = positionSim_t()
        self.Xhat = struct.unpack('>2f', buf.read(8))
        self.X0 = struct.unpack('>2f', buf.read(8))
        self.Xhatdot = struct.unpack('>2f', buf.read(8))
        self.T, self.xCoord, self.yCoord = struct.unpack(">fff", buf.read(12))
        self.DU = struct.unpack('>2f', buf.read(8))
        self.U0 = struct.unpack(">f", buf.read(4))[0]
        self.DU_p = struct.unpack('>2f', buf.read(8))
        self.V0 = struct.unpack('>2f', buf.read(8))
        self.D2U0 = struct.unpack(">f", buf.read(4))[0]
        self.u = struct.unpack('>2f', buf.read(8))
        self.theta = struct.unpack(">f", buf.read(4))[0]
        self.con = struct.unpack('>5f', buf.read(20))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if positionSim_t in parents: return 0
        tmphash = (0xaf42e55bf038a1ba) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if positionSim_t._packed_fingerprint is None:
            positionSim_t._packed_fingerprint = struct.pack(">Q", positionSim_t._get_hash_recursive([]))
        return positionSim_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)
