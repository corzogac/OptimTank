import numpy as np
from scipy.optimize import minimize
from bokeh.plotting import figure, output_file, show
from sugawara import *


# output to static HTML file
output_file("first.html")

x= np.linspace(1,1000,1000)
x1= np.linspace(1,1000,1000)
x2= np.linspace(1,1000,1000)
y= np.multiply(np.random.rand(1000),x)
# create a new plot with a title and axis labels
p = figure(title="Time Series Sugawara", x_axis_label='x', y_axis_label='y')

'''
Testing function    
'''

for i in range(1000):
    prec = np.random.uniform(0, 100)
    evap = np.random.uniform(0, 10)
    st = [np.random.uniform(0, 30), np.random.uniform(0, 30)]
    param = [0.1819, 0.0412, 0.3348, 0.0448, 3.2259, 0.3800,1,1, 1]
    extra_param = [1, 145]
    q, s=step(prec, evap, st, param, extra_param)
    x1[i]=s[0]
    x2[i]=s[1]
    y[i]=q

#def fun_rosenbrock(x):
#   return np.array([10 * (x[1] - x[0]**2), (1 - x[0])])

#res = minimize(fun_rosenbrock, x0, method='nelder-mead')



# add a line renderer with legend and line thickness
p.line(x, y, legend="Random Line", line_width=2)

# show the results
show(p)