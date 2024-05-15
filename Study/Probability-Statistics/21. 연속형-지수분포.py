import random
import matplotlib.pyplot as plt
import math
import numpy as np

# 지수분포의 모수 (비율)를 정의합니다.
lambda_parameter = 0.5

# 데이터를 저장할 리스트를 초기화합니다.
data = []

# 10,000개의 데이터를 생성합니다.
for _ in range(1000):
    # 람다 값에 대한 무작위 지수분포 난수를 생성합니다.
    random_value = random.random()
    exponential_value = -math.log(1 - random_value) / lambda_parameter
    data.append(exponential_value)
# 데이터의 평균과 분산을 계산합니다.
mean = sum(data) / len(data)
variance = sum((x - mean) ** 2 for x in data) / len(data)

print("평균:", mean)
print("분산:", variance)

# PDF 계산
def exponential_pdf(x, lmbda):
    return lmbda * math.exp(-lmbda * x)
# PDF 계산 - 2
def pdf_f(x, n):
    max_v = max(x)
    min_v = min(x)
    dx = (max_v - min_v) / n
    x_l = [min_v + x *dx for x in range(n+1)]
    p_set = [0] * len(x_l)

    for i in range(len(x)):
        for j in range(n):
            if x_l[j] <= x[i] < x_l[j+1]:
                p_set[j] += 1 / len(x) /dx
    return p_set, x_l
pdf_set, x_set = pdf_f(data,30)

# CDF 계산
def exponential_cdf(x, lmbda):
    return 1 - math.exp(-lmbda * x)

# PDF와 CDF를 계산할 x 값들을 정의합니다.
x_values = np.linspace(0, max(data), 100)
pdf_values = [exponential_pdf(x, lambda_parameter) for x in x_values]
cdf_values = [exponential_cdf(x, lambda_parameter) for x in x_values]

# PDF 및 CDF 그래프를 그립니다.
plt.figure(figsize=(12, 4))
plt.subplot(121)
plt.plot(x_values, pdf_values, 'b-')
plt.plot(x_set[0:(len(x_set)-1)], pdf_set[0:(len(x_set)-1)], 'r.')
plt.title("PDF (확률밀도함수)")
plt.xlabel("x")
plt.ylabel("확률밀도")
plt.legend(['sim', 'analy'])

plt.subplot(122)
plt.plot(x_values, cdf_values, 'b-')
plt.title("CDF (누적분포함수)")
plt.xlabel("x")
plt.ylabel("누적확률")

plt.show()

                    

