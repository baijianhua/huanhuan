"""
用方程的形式绘制球
https://stackoverflow.com/questions/4680525/plotting-implicit-equations-in-3d

还是没能完全做到，不过有点那个意思。
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def hyp_part1(x, y, z):
    return (x ** 2) + (y ** 2) + (z ** 2) - 10000


fig = plt.figure()
ax: Axes3D = fig.add_subplot(111, projection='3d')

x_range = np.arange(-100, 100, 1)
y_range = np.arange(-100, 100, 1)
X, Y = np.meshgrid(x_range, y_range)
A = np.linspace(-100, 100, 20)

A1, A2 = np.meshgrid(A, A)

for z in A:
    X, Y = A1, A2
    Z = hyp_part1(X, Y, z)
    ax.contour(X, Y, Z + z, [z], zdir='z', color="r")

for y in A:
    X, Z = A1, A2
    Y = hyp_part1(X, y, Z)
    ax.contour(X, Y + y, Z, [y], zdir='y')

for x in A:
    Y, Z = A1, A2
    X = hyp_part1(x, Y, Z)
    ax.contour(X + x, Y, Z, [x], zdir='x')

ax.set_zlim3d(-100, 100)
ax.set_xlim3d(-100, 100)
ax.set_ylim3d(-100, 100)
ax.axvline
ax.axhline
#ax.set_aspect('equal')
plt.show()
