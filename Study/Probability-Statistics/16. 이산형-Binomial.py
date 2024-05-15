import random
import matplotlib.pyplot as plt

total_try = 50000
n = 3
pmf_ber_s = [0]*4

for _ in range(total_try):
    count = 0
    for _ in range(n):
        i = random.randint(0, 1)
        if (i == 0): # 0이 나오면 앞면
            count += 1
    if (count == 0):
        pmf_ber_s[0] += 1
    elif (count == 1):
        pmf_ber_s[1] += 1
    elif (count == 2):
        pmf_ber_s[2] += 1
    else:
        pmf_ber_s[3] += 1
print(pmf_ber_s)

# 구한 pmf
pmf_ber_s[0] = pmf_ber_s[0]/total_try # 앞면이 0 번 나온 확률
pmf_ber_s[1] = pmf_ber_s[1]/total_try # 앞면이 1 번 나온 확률
pmf_ber_s[2] = pmf_ber_s[2]/total_try # 앞면이 2 번 나온 확률
pmf_ber_s[3] = pmf_ber_s[3]/total_try # 앞면이 3 번 나온 확률

# 계산 pmf: (n팩/n-k팩/k팩)*p**k*(1-p)**(n-k)
prob = [1/8, 3/8, 3/8, 1/8]
print(pmf_ber_s)
plt.bar(range(0,4), pmf_ber_s, width=0.2)
plt.plot(range(0,4), prob, 'r.')
plt.legend(['sim','analy'])
plt.show()
