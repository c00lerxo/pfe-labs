import matplotlib.pyplot as plt
import numpy as np

with open('data2.dat') as f:
    data = f.readlines()

x = [float(i) for i in data]

cmap = np.random.rand(3,)

fig = plt.figure()
ax1 = fig.add_subplot(121)
hist1 = ax1.hist(x, bins=250, cumulative=True, color=cmap)

ax2 = fig.add_subplot(122)
hist2 = ax2.hist(x, bins=250, cumulative=False, color=cmap)

plt.show()
