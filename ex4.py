import numpy as np
import cmath as cm
import sympy as sp
import sympy.solvers as sol

x= sp.Symbol('x')
print("Solucoes:",sol.solve(x**2+2*x+2,x))
print("-1+i eh solucao")