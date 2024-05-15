import random
import matplotlib.pyplot as plt

total_try = 5000
out = [0]*2
try_ = 0

for _ in range(total_try):
    i = random.randint(0, 1)
    if (i == 0):
        out[0] += 1
    else:
        out[1] += 1
    try_ += 1

out[0] = out[0]/try_
out[1] = out[1]/try_

prob = [0.5, 0.5]
plt.bar(range(0,2), out, width=0.2)
plt.plot(range(0,2), prob, 'r.')
plt.legend(['sim','analy'])
plt.show()
########################################
import random
import matplotlib.pyplot as plt

total_try = 5000
pmf_ber_s = [0]*4
try_ = 0

for _ in range(total_try):
    i = random.randint(0, 3)
    if (i == 0):
        pmf_ber_s[0] += 1
    elif (i == 1):
        pmf_ber_s[1] += 1
    elif (i == 2):
        pmf_ber_s[2] += 1
    else:
        pmf_ber_s[3] += 1

pmf_ber_s[0] = pmf_ber_s[0]/total_try
pmf_ber_s[1] = pmf_ber_s[1]/total_try
pmf_ber_s[2] = pmf_ber_s[2]/total_try
pmf_ber_s[3] = pmf_ber_s[3]/total_try

prob = [0.25, 0.25, 0.25, 0.25]

plt.bar(range(0,4), pmf_ber_s, width=0.2)
plt.plot(range(0,4), prob, 'r.')
plt.legend(['sim','analy'])
plt.show()