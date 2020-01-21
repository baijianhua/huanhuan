from IPython.display import display, Latex
from sympy import *

x = symbols('x')
display(x)

int_x = Integral(cos(x)*exp(x), x)
result = "$${} = {}$$".format(latex(int_x), latex(int_x.doit()))
display(Latex(result))

derv_x = Derivative(cos(x)*exp(x), x)
result = "$${} = {}$$".format(latex(derv_x), latex(derv_x.doit()))
pprint(derv_x)
