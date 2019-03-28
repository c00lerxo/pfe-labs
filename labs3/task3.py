import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 500)
sin_y = np.sin(x)
cos_y = np.cos(x)
distance = np.absolute(np.array(cos_y - sin_y))
distance_x = x[distance < 0.1]
distance_sin_y = np.sin(distance_x)
distance_cos_y = np.cos(distance_x) 

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, sin_y)
ax.plot(x, cos_y)
ax.scatter(distance_x, distance_sin_y, color='red')
ax.scatter(distance_x, distance_cos_y, color='red')
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

plt.show()