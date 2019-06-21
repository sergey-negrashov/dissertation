import sys
import matplotlib.pyplot as plt
import numpy as np
if(len(sys.argv) < 2):
    print("need an argument")
    sys.exit()
with open(sys.argv[1]) as f:
    content = f.readlines()
data = [];

for line in content:
    try:
        data.append(float(line))
    except ValueError:
        print("not a float " + line)
        continue
    if len(data) > 2000:
        break;

print(len(data))

data = data - np.average(data)
data = data*1000.0
fig, axs = plt.subplots(1, 1, sharey=True, tight_layout=True)

# We can set the number of bins with the `bins` kwarg
plt.xlabel("Voltage error(mV)")
plt.ylabel("Counts")

label = ("N=%d\n" %  len(data)) + ("$\sigma$=%.2fmV" % np.std(data))

plt.text(0.1, 0.9, label, horizontalalignment='left',verticalalignment='center', transform=axs.transAxes)
axs.hist(data, bins=128)
plt.show()
