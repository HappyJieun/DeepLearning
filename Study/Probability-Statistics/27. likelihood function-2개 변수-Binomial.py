import random
import matplotlib.pyplot as plt
import math
import numpy as np

# 동전 던지기 100번 시행, 앞면이 56번 나왔다고 가정,
# 반복적인 동전 던지기는 성공 확률이 p인 베르누이 시행을 n번 반복 시행할 때
# 성공 횟수의 분포인 이항분포를 따름
# p(x) = (n x)p*x (1-p)^(n-x)
# θ = 0.5 <= 앞면이 나올 확률
# p(x = 56 | θ = 0.5) = (100 56) * (0.5)^56 * (1-0.5)^100-56


# 0과 1사이의 p값을 무수히 많이 대입하여 likelihood가 max가 되는 p 값 찾기
# RV 2개
p_values = np.linspace(0.4, 0.8, 1000)
n1, k1 = 100, 56  
n2, k2 = 50, 30   

# A와 B의 각각의 가능도 함수 정의
likelihood_A = lambda p: (math.factorial(n1) / (math.factorial(k1) * math.factorial(n1 - k1))) * p**k1 * (1 - p)**(n1 - k1)
likelihood_B = lambda p: (math.factorial(n2) / (math.factorial(k2) * math.factorial(n2 - k2))) * p**k2 * (1 - p)**(n2 - k2)

# 각 p 값에 대한 가능도의 곱 계산
likelihood_f = [likelihood_A(p_) * likelihood_B(p_) for p_ in p_values]

# max p 값 출력
print(p_values[likelihood_f.index(max(likelihood_f))])

plt.plot(p_values, likelihood_f,'b-', label="MyMLE")
plt.xlabel('p')
plt.ylabel('ML_f')
plt.legend()
plt.show()



