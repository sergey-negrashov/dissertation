import pywt
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
from scipy.signal import argrelextrema
import sys
from datetime import datetime
import math
import cmath
import matplotlib.animation as animation
import random

trans = [-1, -4, -6, -4, 0, 6, 12, 14, 12, 6, 0, -4, -6, -4, -1]
trans = [x*0.1  for x in trans]

fig, (ax2,ax3,ax4) = plt.subplots(3,1)


f = open(sys.argv[1], 'rb')
y = np.fromfile(f, np.int16)

y = y[0:200*10]
y = [k/2.0**12  for k in y]

pos = 0

trans_pos = 0
for i in range(0, len(trans)):
	y[i + trans_pos] = y[i + trans_pos] + trans[i]

yfft = fft(y)
maxes = argrelextrema(abs(yfft[0:int(len(y)/2)]), np.greater)

acm = 0;
for m in maxes[0]:
	if(m%10 == 0 and m != 6):
		acm = (yfft[m])**2;
		yfft[m] = 0


#THD calculation
#print(yfft[maxes[0][6]])
#print(math.sqrt(acm)/abs(yfft[maxes[0][6]])) #<- this is THD
yfft[10] = 0

ax2.set_title("FFT")
fft_line, = ax2.plot(abs(yfft[0:int(len(y)/2)]))

ax3.set_title("Original and carrier/harmonics suppressed")
sup_line, = ax3.plot(y)
y = abs(ifft(yfft))
sup1_line, = ax3.plot(y)

coef =pywt.wavedec(y,'db1', level=10)		

x = range(0, len(coef[0]))
x = [k/2 for k in x]

ax4.set_title("Wavelet coefficients level 4 through " + str(len(coef)-1)  )
wave_lines = []
for i in range(1,len(coef)):
    x = range(0, len(coef[i]))
    x = [k/2**i for k in x]
    wave, = ax4.plot(x, coef[i])
    wave_lines.append(wave)
    

def animate(i):    
	f = open(sys.argv[1], 'rb')
	y = np.fromfile(f, np.int16)

	y = y[0:200*10]
	y = [k/2.0**12 for k in y]

	pos = 0

	trans_pos = i
	for i in range(0, len(trans)):
		y[i + trans_pos] = y[i + trans_pos] + trans[i]

	yfft = fft(y)
	yfft[10] = 0

	fft_line.set_ydata(abs(yfft[0:int(len(y)/2)]))

	for m in range(0, len(yfft/10),10):
		yfft[m] = 0


	sup_line.set_ydata(y)
	y = abs(ifft(yfft))
	sup1_line.set_ydata(y)
	#print(np.argmax(y))
	coef =pywt.wavedec(y,'db1', level=10)		

	#plt.plot(abs(yfft[0:int(len(y)/2)]))
	#plt.show()

	x = range(0, len(coef[0]))
	x = [k/2 for k in x]
	#plt.plot(x,coef[0])
	max_coef = 0;
	max_intex = 0;
	for i in range(1,len(coef)):
		x = range(0, len(coef[i]))
		x = [k/2**i for k in x]
		wave_lines[i-1].set_ydata(coef[i])
		if max(abs(coef[i])) > max_coef:
			max_coef = max(abs(coef[i]))
			max_index = np.argmax(abs(coef[i]))/2**i
	print(max_index)
	ax4.relim()
	return [fft_line, sup_line, sup1_line]+ wave_lines

ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y) - len(trans)),
                              interval=2, blit=True)

plt.show() 

