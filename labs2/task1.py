import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [3, 7, 4.5, 8]
y2 = [3.25, 3.5, 6.5, 6.85]

plt.xlabel('Parametr X')
plt.ylabel('Parametr Y')
plt.title('Wykres - XY')

plt.plot(x, y1, linestyle='dashed', marker='^', color='red', label='funkcja1')
plt.plot(x, y2, linestyle='dashed', marker='o', color='green', label='funkcja2')
plt.legend(numpoints=2)
plt.show()
