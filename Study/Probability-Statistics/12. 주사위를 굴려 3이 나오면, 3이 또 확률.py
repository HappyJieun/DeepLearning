import random
import matplotlib.pyplot as plt

count = 0
prob = []
real = []
total_try = 100000
for i in range(1, 1+total_try):
    j = random.randint(1, 6)
    if (j == 3):
        k = random.randint(1,6)
        if (k == 3):
            count += 1
    real.append(count/i)
    prob.append(1/36)
plt.plot(range(1,total_try+1),real, 'b', range(1,total_try+1), prob, 'r')
plt.show()
    
