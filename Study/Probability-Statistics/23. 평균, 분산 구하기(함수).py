import random
import numpy as np

def mean_f(list_):
    s = 0
    for i in list_:
        s += i
    return s/len(list_)

def var_f(list_):
    v = 0
    m = mean_f(list_)
    for i in list_:
        v += (i-m)**2
    return v /len(list_)

total = 1000
rand_v = [random.randint(1,5) for _ in range(total)]

print(mean_f(rand_v))
print(var_f(rand_v))
