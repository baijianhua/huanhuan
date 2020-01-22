from sympy import *
import matplotlib.pyplot as plt
from matplotlib import rc

a, b, c, d = symbols('a b c d')
M = Matrix([[a, b],
            [c, d]])

print(M)
print(M.T)
lat = latex(M.T @ M)
print(lat)

tex = "$"+lat+"$"
rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
rc('text', usetex=True)
rc('text.latex', preamble=r'\usepackage{amsmath}')
plt.text(0.05, 0.5, tex, size=40)
plt.axis('off')
plt.show()
