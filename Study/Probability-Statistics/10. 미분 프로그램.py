import matplotlib.pyplot as plt
import numpy as np

class Differentiation:
    def __init__(self, func, x_list):
        self.func=func
        self.x_list=x_list
        self.result1=[]
        self.result2=[]
        self.result3=[]
    def func_cal(self, y, delta):
        if y == 0:
            self.result1 = self.func(self.x_list)
        else:
            self.result2 = self.func(self.x_list+delta)
    def func_differ(self):
        delta=0.001
        for i in range(2):
            self.func_cal(i, delta)
        self.result3=(self.result2 - self.result1)/delta

a = -10
b = 10
c = 80
x1 = np.linspace(a,b,c)
func_x = lambda x : x**4 + x**3 + x**2 +  x**1 + 1
dd = Differentiation(func_x, x1)
dd.func_differ()
plt.figure(1)
plt.plot(x1, dd.result1, 'r--', label='f(x)')
plt.plot(x1, dd.result3, 'bs', label='f_p(x)')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend(loc='upper right')
plt.show()
