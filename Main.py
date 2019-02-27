import numpy as np
from scipy.optimize import minimize
from bokeh.plotting import figure, output_file, show


x= np.linespace(1,1000,1)
y= np.multiply(np.random.rand(1000),x)

#def fun_rosenbrock(x):
#   return np.array([10 * (x[1] - x[0]**2), (1 - x[0])])

#res = minimize(fun_rosenbrock, x0, method='nelder-mead')

# output to static HTML file
output_file("first.html")

# create a new plot with a title and axis labels
p = figure(title="Random Numbers", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
p.line(x, y, legend="Random Line", line_width=2)

# show the results
show(p)