import pywt
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
from scipy.signal import argrelextrema
import sys
from datetime import datetime
import math
import cmath
from random import *



f = open(sys.argv[1], 'rb')
y1 = np.fromfile(f, np.int16)
x1 = list(range(0, len(y1)))
y1[:] = [y * 0.0068 for y in y1]
x1[:] = [x / 12000.0 -0.7 for x in x1]
plt.plot(x1, y1, label="Device 1")


f = open(sys.argv[2], 'rb')
y2 = np.fromfile(f, np.int16)
x2 = list(range(888,len(y2) + 888))
x2[:] = [x / 12000.0 -0.7 for x in x2]
y2[:] = [y * 0.0069 for y in y2]

plt.xlabel("Time(s)")
plt.ylabel("Voltage(V)")
plt.xlim(0.25,0.5)
plt.plot(x2, y2, label="Device 4")
plt.legend(loc='center right')
plt.show()


