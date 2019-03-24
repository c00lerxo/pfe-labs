import matplotlib.pyplot as plt
from matplotlib import cm

with open('bars.txt') as f:
    lines = f.readlines()

x = [float(i) for i in lines[0].split()]
y = [float(i) for i in lines[1].split()]

color = cm.copper(y)

fig = plt.figure()
ax = fig.add_subplot(111)
rects = ax.bar(x, y, color=color)

for rect in rects:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2.,
            1.005*height,
            '%.2f' % float(height),
            ha='center',
            va='bottom')

plt.show()
