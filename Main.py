import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

x0= np.random.rand(1000)
plt.plot(x,'r.')

def fun_rosenbrock(x):
   return np.array([10 * (x[1] - x[0]**2), (1 - x[0])])

res = minimize(fun_rosenbrock, x0, method='nelder-mead')

print(res.x)