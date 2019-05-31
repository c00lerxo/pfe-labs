import numpy as np
import scipy.stats as sci
import matplotlib.pyplot as plt

mu, sigma = (0.0, 1.0)
mu1, sigma1 = (2.0, 0.8)

x = np.random.normal(mu, sigma, size=100)
x1 = np.random.normal(mu1, sigma1, size=100)

stacked = np.hstack([x, x1])
density = sci.gaussian_kde(stacked)

x3 = np.linspace(-5, 7, num=100)

plt.hist(stacked, bins=20, edgecolor='black', linewidth=1.2, density=True)
plt.plot(x3, density(x3))

plt.show()