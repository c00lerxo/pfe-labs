import numpy as np 
import matplotlib.pyplot as plt

x = np.load('x.npy')
y = np.load('y.npy')
x1 = np.linspace(x[0], x[-1])
m1, c1 = np.polyfit(x, y, 1)
y1 = m1 * x + c1

a, b, c2 = np.polyfit(x, y, 2)
y2 = a * x1**2 + b * x1 + c2

pol_10 = np.polyfit(x, y, 10)
y10 = (pol_10[0] * x1**10 + pol_10[1] * x1**9 + pol_10[2] * x1**8 + pol_10[3] * x1**7 + pol_10[4] * x1**6 + pol_10[5] * x1**5 + pol_10[6] * x1**4 
       + pol_10[7] * x1**3 + pol_10[8] * x1**2 + pol_10[9] * x1**1 + pol_10[10])
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x, y, color='red')
ax.plot(x, y1, color='black', linestyle='dashed')
ax.plot(x1, y2, color='blue')
ax.plot(x1, y10, linestyle='dashed', color='green')

plt.show()
