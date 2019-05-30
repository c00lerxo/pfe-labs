import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

data = np.loadtxt('pcadata.txt')

petal_length = data[0]
sepal_length = data[1]
sepal_width = data[2]

mean = np.mean(data)
covariant_matrix = np.cov(data)

print('Mean:', mean)
print('Covariant matrix:', covariant_matrix)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(petal_length, sepal_length, sepal_width, color='blue')

plt.show()