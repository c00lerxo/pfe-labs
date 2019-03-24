import matplotlib.pyplot as plt

with open('scatter.txt') as f:
    lines = f.readlines()

x = [float(i) for i in lines[0].split()]
y = [float(i) for i in lines[1].split()]

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
c = ax.scatter(x, y, c=y, cmap='hsv', alpha=0.75)

plt.show()
