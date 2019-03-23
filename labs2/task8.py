import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

with open('data3.dat') as f:
  data = f.readlines()

x = [float(i) for line in data for i in line.split(',')]

fig = plt.figure()
ax1 = fig.add_subplot(121)
bp1 = ax1.boxplot(x)


plt.show()
