import sys
import matplotlib.pyplot as plt
import numpy as np
if(len(sys.argv) < 2):
    print("need an argument")
    sys.exit()
with open(sys.argv[1]) as f:
    content = f.readlines()
data = [];

i = 0

for line in content:
    try:
        data.append(float(line))
    except ValueError:
        print("not a float " + line)
        continue
    if len(data) == 200:
        break
print(len(data))

timestep = 1/60.0/200.0

x = []
for i in range(0,len(data)):
	x.append(i*timestep*1000)

fig, axs = plt.subplots(1, 1, sharey=True, tight_layout=True)

# We can set the number of bins with the `bins` kwarg
plt.xlabel("Time(ms)")
plt.ylabel("Voltage")

axs.plot(x,data);
plt.show()
