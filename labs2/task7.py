import matplotlib.pyplot as plt

x = [1, 5.5, 7.5, 8.5, 10]
y = [0, 7.3, 8.6, 9.4, 9.9]

fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_xlim([0, 10])
ax.set_ylim([0, 10])

# Don't allow the axis to be on top of your data
ax.set_axisbelow(True)
# Turn on the minor TICKS, which are required for the minor GRID
ax.minorticks_on()

# Customize the major grid
ax.grid(which='major', linestyle='-', linewidth='0.5', color='black')
# Customize the minor grid
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

empty_string_labels = ['']*len(ax.get_xticklabels())

ax.set_xticklabels(empty_string_labels)
ax.set_yticklabels(empty_string_labels)

ax.plot(x, y, linestyle='-.', color='red', linewidth=2.5, marker='o',
        markersize=10, markerfacecolor='blue', markeredgecolor='red')

plt.show()
