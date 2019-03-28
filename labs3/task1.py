import numpy as np

random_array = np.random.rand(25, 1) * 100
random_array[np.argmax(random_array)] = 200
random_array[random_array < 50] = 0
