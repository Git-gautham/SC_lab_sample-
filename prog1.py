# 1. Implement the function given below and plot its two cycles. Plot its histogram also.
# f(t) = cost cos5t + cos5t
# @author:GAUTHAM
import numpy as np
import matplotlib.pyplot as plt
#0 to 4pi
t = np.linspace(0, 4 * np.pi, 1000)
x=np.cos(t) * np.cos(5*t) + np.cos(5*t)
#Ploting the function
plt.plot(t,x,label='f(t) = cos(t) * cos(5t) + cos(5t)')
plt.title('Plot of f(t) over two cycles')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.legend()
plt.show()
#Histogram
plt.hist(x, bins=30)
plt.title('Histogram of f(t)')
plt.xlabel('f(t) values')
plt.ylabel('Frequency')
plt.show()