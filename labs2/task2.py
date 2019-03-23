import matplotlib.pyplot as plt
import numpy as np

with open('scatter.txt') as file:
    content = file.readlines()

data = [line for line in content]
x = data[0].split()
y = data[1].split()

x = [float(i) for i in x]
y = [float(i) for i in y]

ax = plt.axes(polar = True)
plt.scatter(x, y)

plt.show()
