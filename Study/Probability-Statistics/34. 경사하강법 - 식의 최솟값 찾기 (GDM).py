import numpy as np
import matplotlib.pyplot as plt
import random

# 경사하강법을 이용하여 주어진 식에 대한 최솟값 찾기 
# 1) 임의의 a1에서 미분을 구한다.
# 2) 구해진 기울기의 반대 방향 얼마간 이동시킨 a2에서 미분을 구한다.
# 3) f(a1)과 f(a2) 의 차이를 구한다.
# 4) 값의 차이가 0(차이가 크지 않다)이 아니면 2~3번 과정을 반복한다

def differentitation(x, delta):
    y_delta = func_(x + delta)
    y = func_(x)
    gradient = (y_delta - y)/(delta)
    return gradient

def func_(x):
    return x**2 + x #식 

learning_rate = 0.001
delta = 0.000001
eps = 0.00001

x_i = random.random()
y_i = func_(x_i)

i_ter = 0
 
while (True):
    g_d = differentitation(x_i, delta)
    x_n = x_i + (-g_d*learning_rate)
    y_n = func_(x_n)
    
    if (abs(x_n-x_i)<=eps):  # Xi+1 == Xi
        print('x*=', x_n, ', min of f(x) =', y_n)
        break
    
    i_ter += 1
    if (i_ter%100) == 0:
        print('i_ter:', i_ter, 'x=', x_n, 'f(X)=',y_n)
    x_i = x_n
    
print("===============================================")

x_i = random.random()
y_i = func_(x_i)

i_ter = 0

while (True):
    g_d = differentitation(x_i, delta)
    x_n = x_i + (-g_d*learning_rate)
    y_n = func_(x_n)
    
    if (abs(y_n-y_i)<=eps):  # f(Xi+1) == f(Xi)
        print('x*=', x_n, ', min of f(x) =', y_n)
        break
        
    i_ter += 1
    if (i_ter%100) == 0:
        print('i_ter:', i_ter, 'x=', x_n, 'f(X)=',y_n)
    x_i = x_n
    y_i = y_n
