import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

with np.load('labs7/rozklady.npz') as data:
    pairs = (data['arr_0'], data['arr_1'], data['arr_2'])

x = np.linspace(-6, 6, num=100)
fig = plt.figure()

for index, pair in enumerate(pairs, start=1):
    print('Pair', index)
    pair_densities = (stats.gaussian_kde(pair[0]), stats.gaussian_kde(pair[1]))

    means = (np.mean(pair[0]), np.mean(pair[1]))
    print('Means: ', means[0], means[1])
    
    print('Null-hypothesis test:')
    print(stats.ttest_1samp(pair[0], 0.0))
    print(stats.ttest_1samp(pair[1], 0.0))

    print('Means test:')
    print(stats.ttest_ind(pair[0], pair[1]))

    ax = fig.add_subplot(1, 3, index)
    ax.plot(x, pair_densities[0](x), color='blue')
    ax.plot(x, pair_densities[1](x), color='green')

plt.show()