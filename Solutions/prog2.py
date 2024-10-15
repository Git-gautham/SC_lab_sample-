# 2. Implement the functions given below and plot two cycles of them. Plot scatter plot to
# study their relationship.
# f1(t) = sint
# f2(t) = cost
# @author:GAUTHAM
import numpy as np
import matplotlib.pyplot as plt
#0 to 4pi
t = np.linspace(0, 4 * np.pi, 1000)
x1=np.sin(t)
x2=np.cos(t)
#Ploting the function
plt.plot(t,x1,label='f1(t) = sin(t)')
plt.plot(t,x2,label='f2(t) = cos(t)')
plt.title('Plot of f1(t) = sin(t) & f2(t) = cos(t) over two cycles')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.legend()
plt.show()
#scatter plot
plt.scatter(x1,x2)
plt.title('Scatter Plot of f1(t) & f2(t)')
plt.xlabel('f1(t) = sin(t)')
plt.ylabel('f2(t) = cos(t)')
plt.show()