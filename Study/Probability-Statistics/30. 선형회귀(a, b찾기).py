import numpy as np
import math
from matplotlib import pyplot as plt

x = np.linspace(0,4,15)
sigma = 1
error = np.random.normal(0, sigma, len(x))
y = 1 + 2 * x + error # 실제 식

guass = lambda x, m : 1/(2*math.pi)**0.5*math.exp(-(x-m)**2/2)
a = np.linspace(0,3,100) #추정할 a들 
b = np.linspace(-1,2,100) #추정할 b들 
likelihood = []

for i in range(len(a)):
    a_h = a[i]
    for i2 in range(len(b)):
        b_h = b[i]
        likelihood_f = 0
        for j in range(len(x)):
            x_data = x[j]
            y_ = b_h + a_h * x_data # x와 y의 관계식: y = b + a*x
            likelihood_f += math.log10(guass(y[j], y_))
        likelihood.append((a_h, b_h, likelihood_f))

likelihood.sort(key=lambda x: x[2], reverse=True)
max_likelihood = max(likelihood, key=lambda x: x[2])
max_a = max_likelihood[0]
max_b = max_likelihood[1]

y_h = max_b + max_a * x

print(max_a, max_b)

plt.plot(x,y,'.b', label='real data')
plt.plot(x,y_h,'r-', label = 'estimation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
