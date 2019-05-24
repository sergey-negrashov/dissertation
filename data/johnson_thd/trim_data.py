import sys
import matplotlib.pyplot as plt
import matplotlib

f = open(sys.argv[1])

time = []
thd = []
frequency = []
voltage = []

for line in f:
    parts = line.split()
    time.append(int(parts[1]))
    thd.append(float(parts[4]))
    frequency.append(float(parts[3]))
    voltage.append(float(parts[2]))

time = [(x - 1514564949770.0)/1000/60/60 + 6.5 for x in time]

font = {'family' : 'normal', 'weight' : 'normal', 'size'   : 22}
matplotlib.rc('font', **font)


fig, ax1 = plt.subplots()
ax1.plot(time, thd, 'b-')
#plt.xlim(0,24)
ax1.set_xlabel('Time(Hr)')
ax1.set_ylabel('THD(%)')
#ax2 = ax1.twinx()
#ax2.plot(time, voltage,'r-')
plt.show()
