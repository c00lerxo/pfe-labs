import matplotlib.pyplot as plt

with open('data3.dat') as f:
    data = f.readlines()

x = [float(i) for line in data for i in line.split(',')]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect(16/9)  # Not sure about this one...
bp = ax.boxplot(x)

plt.show()
