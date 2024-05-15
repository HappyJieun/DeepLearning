import numpy as np
import matplotlib.pyplot as plt
import random

# 오차 평가 : 평균제곱근(root mean square error)

def differentiation(a, b, x, delta, y):
    y_delta_a = RMSE(a + delta, b, x, y)
    y_delta_b = RMSE(a, b + delta, x, y)
    y = RMSE(a, b, x, y)
    gradient_a = (y_delta_a - y) / delta
    gradient_b = (y_delta_b - y) / delta
    return gradient_a, gradient_b

def func_(a, b, x):
    return b + a * x

def mean(x):
    return sum(x) / len(x)

def RMSE(a, b, x, y):
    return np.sqrt(mean((y - func_(a, b, x))**2))

## main ##
x = np.linspace(0, 4, 30)
sigma = 1
error = np.random.normal(0, sigma, len(x))

y = 1 + 2 * x + error

a = np.random.random()
b = np.random.random()

learning_rate = 0.0001
delta = 0.001
eps = 0.00001
i_ter = 0
prev_rmse = float('inf')

while True:
    g_d_a, g_d_b = differentiation(a, b, x, delta, y)
    a_n = a + (-g_d_a * learning_rate)
    b_n = b + (-g_d_b * learning_rate)
    rmse = RMSE(a_n, b_n, x, y)
    i_ter += 1
    if abs(prev_rmse - rmse) <= eps:
        print('a* =', a_n, ', b* =', b_n, ', min of rmse =', rmse)
        break
    a, b = a_n, b_n
    prev_rmse = rmse
    if i_ter % 10000 == 0:
        print('i_ter:', i_ter, 'a =', a_n, 'b =', b_n, 'rmse =', rmse)

plt.plot(x, y, '.b', label='real data')
plt.plot(x, func_(a_n, b_n, x), 'r-', label='estimation')
plt.legend()
plt.show()

