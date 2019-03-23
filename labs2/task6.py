import matplotlib.pyplot as plt
from matplotlib import cm

with open('pie.txt') as f:
  data = f.readlines()

x = [float(i) for i in data[0].split()]

fig = plt.figure()
explode = (0.1, 0.04, 0.15, 0.2, 0.18)
ax = fig.add_subplot(111)
pie = ax.pie(x, explode = explode,
            wedgeprops = {"edgecolor":"black", 'linewidth': 0.5, 'antialiased': True})
            
plt.show()
