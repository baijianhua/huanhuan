from sympy import *
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams

a, b, c, d = symbols('a b c d')
M = Matrix([[a, b],
            [c, d]])

print(M)
print(M.T)
lat = latex(M.inv())
print(lat)

# tex = r"$\sum_{n=1}^\infty\frac{-e^{i\pi}}{2^n}!$"
tex = "$"+lat+"$"
rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
rc('text', usetex=True)
rc('text.latex', preamble=r'\usepackage{amsmath}')
plt.text(0.5, 0.5, tex, size=40)
plt.axis('off')
plt.show()
