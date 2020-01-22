from sympy import *
from sympy import *
import matplotlib.pyplot as plt
from matplotlib import rc


x, y, z = symbols('x y z')
# 表达式
expr1 = exp(x*y*z)

# 求导
r1 = diff(expr1, x, y, evaluate=False)
r2 = latex(diff(expr1, x, 1, y, 2, z, 4, evaluate=False))

pprint("r1:", r1)
pprint("r2:", r2)

# tex = r"$\sum_{n=1}^\infty\frac{-e^{i\pi}}{2^n}!$"
tex = "$"+latex(r2)+"$"
# 不设置这一行会出现dvipng报错
rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
rc('text', usetex=True)
rc('text.latex', preamble=r'\usepackage{amsmath}')
plt.text(0.05, 0.5, tex, size=40)
plt.axis('off')
plt.show()

