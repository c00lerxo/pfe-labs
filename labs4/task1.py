import numpy as np
import scipy.linalg as sp
import matplotlib.pyplot as plt

a = np.array([[2, 3], [5, 4]])
b = np.array([4, 23])
x = np.linspace(-4, 10, num=200)
x2_1 = (4 - 2 * x) / 3
x2_2 = (23 - 5 * x) / 4
x2_3 = 0 * x + 18 / 5  # We have to multiply x by 0 to avoid dimension error
solution = np.linalg.solve(a, b)

c = np.concatenate((a, np.array([[0, 5]])))
d = np.concatenate((b, np.array([18])))
approximation = np.linalg.lstsq(c, d)[0]

print('Matrix rank: ', np.linalg.matrix_rank(a))
print('Matrix condition number: ', np.linalg.cond(a))
print('Matrix LU decomposition: ', sp.lu(a, permute_l=True))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, x2_1)
ax.plot(x, x2_2)
ax.plot(x, x2_3)
ax.scatter(solution[0], solution[1])
ax.scatter(approximation[0], approximation[1])

plt.show()