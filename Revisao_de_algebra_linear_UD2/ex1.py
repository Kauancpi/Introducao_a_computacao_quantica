import numpy as np
import cmath as cm
import sympy as sp
import sympy.solvers as sol

x= sp.Symbol('x')
print(sol.solve(x**4+2*x**2+1,x))
print("Solucoes complexas")