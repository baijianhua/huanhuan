from numpy import *
import matplotlib.pyplot as plt

x = arange(-2, 5, .01)
y = 2*x + 2

plt.plot(x, y)
# draw a thick red hline at y=0 that spans the xrange
plt.axhline(linewidth=2, color='r')
plt.axvline(linewidth=2, color='r')
# plt.axis([-1, 2, -1, 2])

plt.show()
