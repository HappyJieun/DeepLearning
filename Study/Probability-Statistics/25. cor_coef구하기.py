import random
import matplotlib.pyplot as plt
import numpy as np
import math

x = [1,2,3,4,5]
y = [2,3,4,1,1]

# correlation = E[XY]
# covariance = E[XY] - E[X]E[Y]
# correlation_coefficient = covariance / std_x*std_y

def mean(list_a, list_b):
    mean_x, mean_y = 0, 0
    for i, j in zip(list_a, list_b):
        mean_x += i/len(list_a)
        mean_y += j/len(list_b)
    return mean_x, mean_y
    
def cor(list_a, list_b):
    s = 0
    for i in range(len(list_a)):
        s += list_a[i]*list_b[i]
    return s/len(list_a)

mean_x, mean_y = mean(x, y)
correlation = cor(x, y)

def cov(cor, mean_x, mean_y):
    return cor - (mean_x * mean_y)
covariance = cov(correlation, mean_x, mean_y)

var_x, var_y = 0, 0
for i, j in zip(x, y): 
    var_x += (i - mean_x)**2/(len(x)) # n-1?
    var_y += (j - mean_y)**2/(len(y)) # n-1?

def cor_coef(cov, var_x, var_y):
    std_x = math.sqrt(var_x)
    std_y = math.sqrt(var_y)
    return cov/(std_x*std_y)

correlation_coefficient = cor_coef(covariance, var_x, var_y)
print(correlation_coefficient )
print(np.corrcoef(x,y)[0,1])
print(np.corrcoef(x,y)[1,0])
