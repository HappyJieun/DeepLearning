import random
import matplotlib.pyplot as plt

prob = []
real = []
count = 0
total_try = 300000

for i in range(1, total_try+1):
    ran = random.randint(1,6)
    if (ran == 3):
        count += 1
    real.append(count/i)
    prob.append(1/6)

plt.plot(range(1, total_try+1), real, 'b', range(1, total_try+1), prob, 'r')
plt.legend()
plt.show()

