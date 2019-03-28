import numpy as np

array = np.random.randint(-100, 100, (9, 9))
only_evens = np.sort(array[array % 2 == 0])
print(array)
print(only_evens)