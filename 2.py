import matplotlib.pyplot as plt
import numpy as np
# some imports to plot an equation


def f(x):
    return (0.3139 * x ** 2) + (0.8402 * x) + 2.2701
    # This is the equation I got after plotting the given first curve


def f2(x):
    return (-(0.3139 * x ** 2)) + (0.8402 * x) - 2.2701
    # This is the equation I got after plotting the given second curve which is exactly opposite of the first one


xlist = np.linspace(-10, 10, num=100)   # list of x values
xlist2 = np.linspace(-10, 10, num=100)   # list of x values for second curve
ylist = f(xlist)   # list of y values after calculating from the equation
ylist2 = f2(xlist2)   # list of y values for second curve after calculating from the equation


plt.figure(num=0, dpi=120)   # this determine the figure number and display pixels
plt.axhline(0, color='black', alpha=0.5, dashes=[2, 4], linewidth=1)
plt.axvline(0, color='black', alpha=0.5, dashes=[2, 4], linewidth=1)
plt.xlabel('X-Axis' + '\n' + 'Parabola')   # axis level
plt.ylabel('Y-Axis')
plt.plot(xlist, ylist)   # plotting the first curve
plt.plot(xlist2, ylist2)   # plotting the second curve
plt.show()   # showing the plot on pyCharm
