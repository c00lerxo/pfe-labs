import numpy as np 
import matplotlib.pyplot as plt

x = np.load('x.npy')
x1 = np.linspace(x[0], x[-1])
y = np.load('y.npy')

p1 = np.poly1d(np.polyfit(x, y, 1))
y1 = p1(x)

p2 = np.poly1d(np.polyfit(x, y, 2))
y2 = p2(x1)

p10 = np.poly1d(np.polyfit(x, y, 10))
y10 = p10(x1)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x, y, color='red')
ax.plot(x, y1, color='black', linestyle='dashed')
ax.plot(x1, y2, color='blue')
ax.plot(x1, y10, linestyle='dashed', color='green')

plt.show()
