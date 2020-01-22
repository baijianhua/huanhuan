from numpy import *
from enthought.mayavi.mlab import *

x, y, z = mgrid[-100:101:25., -100:101:25., -100:101:25.]

V = 2 * x ** 2 + 3 * y ** 2 - 4 * z  # just a random function for the potential

Ex, Ey, Ez = gradient(V)
Ex = - Ex
Ey = - Ey
Ez = - Ez

quiver3d(x, y, z, Ex, Ey, Ez)  # plot the electric field just for fun