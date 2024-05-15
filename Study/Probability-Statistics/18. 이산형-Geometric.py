import random
import matplotlib.pyplot as plt

def pmf(list_):
    x_range = range(1,11)
    n_x = [0]*len(x_range)
    for i in x_range:
        for j in list_:
            if (i == j):
                n_x[i-1] += 1/len(list_)
    return n_x

total_try = 5000
list_n = []
for _ in range(total_try):
    i = random.randint(0,2)
    n = 1
    while (i != 1):
        n += 1
        i = random.randint(0,2)
    list_n.append(n)
pmf_l = pmf(list_n)

pmf_a = []
for x in range(1, 11):
    prob = (2/3)**(x-1)*(1/3)
    pmf_a.append(prob)


plt.bar(range(1, 11), pmf_l)
plt.plot(range(1, 11), pmf_a, 'r.')
plt.show()
