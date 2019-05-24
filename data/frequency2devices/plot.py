#!/usr/bin/python3

import sys

import matplotlib.pyplot as plt

b1 = []
t1 = []
b4 = []
t4 = []

f = open(sys.argv[1],'r')
for line in f:
        parts = line.split()
        if parts[0] == "1":
            t1.append(int(parts[1]))
            b1.append(float(parts[3]))
        else:
            t4.append(int(parts[1]))
            b4.append(float(parts[3]))

at1 = [0];
at4 = [(-t1[0] + t4[0])/1000.0];

for i in range(1,len(t1)):
    at1.append((t1[i] - t1[0])/1000.0)


for i in range(1,len(t4)):
    at4.append((t1[i] - t1[0] - (t1[0] - t4[0]))/1000.0)

plt.xlabel("Time(s)")
plt.ylabel("Frequency(Hz)")

plt.plot(at1[1:-1],b1[1:-1], label='Device 1')
plt.plot(at4[1:-1],b4[1:-1], label='Device 4')
plt.legend(loc='center right')
plt.show()
