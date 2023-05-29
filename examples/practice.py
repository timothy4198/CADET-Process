import numpy as np
from scipy.optimize import minimize
# def rosen(x):
#     """The Rosenbrock function"""
#     return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)


input=np.linspace(-5,5)
def simulation(a):
    return a*(input**2)

TRUE_VAL_A = 4
output = simulation(TRUE_VAL_A)

from matplotlib import pyplot as plt

def loss(var):
    v=(simulation(var)-output)**2
    return np.sum(v)


plt.plot(input,output)
plt.show()
x0=0
res=minimize(loss,x0)
print(res)

# x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])

# res = minimize(rosen, x0, method='nelder-mead',
#               options={'xatol': 1e-8, 'disp': True})