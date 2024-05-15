import numpy as np
import matplotlib.pyplot as plt
# 미분함수
def differentitation(x, delta):
    y_delta = func_(x + delta)
    y = func_(x)
    gradient = (y_delta - y)/(delta)
    return gradient

def func_(x):
    return x**2 + x

x = np.linspace(-10, 10, 40)
y = []
y_m = []
delta = 0.000001

y_m = differentitation(x, delta)
y = func_(x)

plt.figure(1)
plt.plot(x, y,label = 'x^2+x')
plt.plot(x, y_m, label = '2x+1')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend(loc='upper right')
plt.grid()
plt.show()
    
