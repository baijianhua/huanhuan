import numpy as np
import matplotlib.pyplot as plt

# 1.圆半径
x = np.arange(-3, 3, 0.01)
y = (9 - x ** 2) ** 0.5
fig = plt.figure()
axes = fig.add_subplot(111)

axes.plot(x, y)
axes.axis('equal')
plt.axhline(linewidth=2, color='r')
plt.axvline(linewidth=2, color='r')
plt.show()
