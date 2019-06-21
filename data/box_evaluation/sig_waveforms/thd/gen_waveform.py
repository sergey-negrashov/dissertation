import math
import matplotlib.pyplot as plt

header = """data length,16384
frequency,60.000000000
amp,15.388740000
offset,0.000000000
phase,0.000000000







xpos,value"""

print(header)

sample_count = 16384;
dt = 1.0/60.0/(sample_count - 1)
ampl = 0.125
thd = 0.01;
data = []
for i in range(0, sample_count):
	data.append(thd*ampl*math.sin(8*math.pi*i/sample_count) + ampl*math.sin(2*math.pi*i/sample_count))
	print(str(i*dt) + "," + str(data[i]))

import matplotlib.pyplot as plt
plt.plot(data)
plt.show()
