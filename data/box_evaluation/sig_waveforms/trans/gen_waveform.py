import math
import matplotlib.pyplot as plt
import numpy as np
header = """data length,16384
frequency,60.000000000
amp,15.388740000
offset,0.000000000
phase,0.000000000







xpos,value"""

trans = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]
trans = list(map(lambda x: x/8.0, trans))

trans = np.interp(list(map(lambda x: x/200.0*len(trans), range(0,200))), range(0,len(trans)), trans)

print(header)

sample_count = 16384;
dt = 1.0/60.0/(sample_count - 1)
ampl = 0.125
thd = 0.01;
data = []
trans_amp = 2*ampl*0.10;
for i in range(0, sample_count):
	if i >= 10000 and i < 10000 + len(trans):
		data.append(ampl*math.sin(2*math.pi*i/sample_count) + trans_amp*trans[i-10000])
	else:
		data.append(ampl*math.sin(2*math.pi*i/sample_count) )
	print(str(i*dt) + "," + str(data[i]))

import matplotlib.pyplot as plt
plt.plot(data)
plt.show()
