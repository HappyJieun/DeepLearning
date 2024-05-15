import random
import matplotlib.pyplot as plt

total = 1000
rand_v =[random.randint(1,5) for _ in range(total)]
sum = 0
dev = 0.0

for i in range(total):
    sum += rand_v[i]
    
mean = sum/total

for i in range(total):
    dev += (mean - rand_v[i]) * (mean - rand_v[i])

print("평균:", mean)
print("분산:",dev/total)

# E[2x] = 2E[x]
# V[2x] = 4V[x]
sum_2 = 0
dev_2 = 0.0
for i in range(total):
    sum_2 += rand_v[i] * 2

mean_2 = sum_2/total

for i in range(total):
    dev_2 += (mean_2 - 2 * rand_v[i]) * (mean_2 - 2 * rand_v[i])

print(mean_2)
print(dev_2/total)

## plot
RV = [0]*5
for i in rand_v:
    for k in range(1,6):
        if (k == i):
            RV[k-1] += 1
plt.bar(range(1,6), RV)
plt.show()
