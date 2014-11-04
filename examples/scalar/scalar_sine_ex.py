'''
file: scalar_sine_ex.py
'''

import time, math
import lcm
from graphing_ex import *

lc = lcm.LCM()
scalar_msg = scalar_voltage_t()

ff = 1.0  # frequency [Hz]
N = 100.0  # Number of cycles

t0 = time.time()
et = time.time()-t0

TT = ff*N  # time to run
print "Running scalar_sine_ex for %4.2f s ..."%TT
while et < TT:
    y = math.sin(ff*2*math.pi*et)
    scalar_msg.utime = time.time()*1.0e6
    scalar_msg.voltage = y
    lc.publish("scalar_sine_ex",scalar_msg.encode())

    time.sleep(1.0/ff/10.0)
    et = time.time()-t0



    
