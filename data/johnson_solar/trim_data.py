import sys
import matplotlib.pyplot as plt
import matplotlib

f = open(sys.argv[1])

time = []
volts = []

offset = 86400000*3

for line in f:
    parts = line.split()
    if int(parts[0]) >= 1513605600000 - offset and int(parts[0]) <=1513692000000 - offset :
        time.append(int(parts[0]))
        volts.append(float(parts[1]))

time = [ (x - 1513605600000 + offset)/1000.0/60/60 for x in time ]

font = {'family' : 'normal', 'weight' : 'normal', 'size'   : 22}
matplotlib.rc('font', **font)

plt.plot(time, volts)
plt.xlim(0,24)
plt.xlabel("Time(Hours)")
plt.ylabel("Voltage(V)")
plt.show()
