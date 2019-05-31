import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

with np.load('rozklady.npz') as data:
    arr_0 = data['arr_0']
    arr_1 = data['arr_1']
    arr_2 = data['arr_2']

