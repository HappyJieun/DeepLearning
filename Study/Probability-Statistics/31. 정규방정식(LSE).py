import numpy as np
import math
from matplotlib import pyplot as plt

# 정규방정식-LSE 이용 (최소제곱법)

x = np.linspace(0,4,10)
sigma = 1
error = np.random.normal(0, sigma, len(x))
y = 2 + 3 * x + error

def cov(x_, y_):
    s= 0
    for i in range(len(x)):
        s += x_[i] * y_[i]
    return (s / len(x_)) - (mean(x_) * mean(y_))

def mean(k):
    s = 0
    for i in k:
        s += i
    return s/len(k)

def var(k):
    s = 0
    m = mean(k)
    for i in k:
        s += (i-m) ** 2
    return s/len(k)

beta1 = cov(x,y)/var(x)
beta0 = mean(y) - beta1 * mean(x)

print(beta1, beta0)
y_h = beta0 + beta1 * x

plt.plot(x, y,'.b', label = 'real data')
plt.plot(x, y_h, 'r-', label = 'estimation')
plt.legend()
plt.show()
