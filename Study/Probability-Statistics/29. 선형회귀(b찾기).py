import numpy as np
import math
from matplotlib import pyplot as plt

x = np.linspace(0,4,15)
sigma = 1
error = np.random.normal(0, sigma, len(x))
y = 1 + 2 * x + error # 실제 식

guass = lambda x, m : 1/(2*math.pi)**0.5*math.exp(-(x-m)**2/2)
b = np.linspace(0,3,100) #추정할 b들 
likelihood = []

for i in range(len(b)):
    b_h = b[i]
    likelihood_f = 0
    for j in range(len(x)):
        x_data = x[j]
        y_ = b_h + 2 * x_data # x와 y의 관계식: y = b + 2*x
        likelihood_f += math.log10(guass(y[j], y_))
    likelihood.append(likelihood_f)

max_b = b[likelihood.index(max(likelihood))]
y_h = max_b + 2 * x

plt.figure(1)
plt.plot(b, likelihood,'b-')
plt.xlabel('b')
plt.ylabel('ML_f')
plt.figure(2)
plt.plot(x,y,'.b', label='real data')
plt.plot(x,y_h,'r-', label = 'estimation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
