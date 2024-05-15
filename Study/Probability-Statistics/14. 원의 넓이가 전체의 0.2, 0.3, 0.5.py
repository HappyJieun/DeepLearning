import random

r1 = [0.6, 0.7, 0.707, 0.8]
r2 = [0.3, 0.4, 0.447, 0.5]
total_try = 50000
#for i in range(101):  # 0부터 100까지 총 101번 반복
#    r1.append(i/100.0)  # 0부터 1까지의 값으로 변환
#    r2.append(i/100.0)

for i in r1:
    for k in r2:
        try_ = 0
        inner1 = 0
        inner2 = 0
        for _ in range(total_try):
            a = random.random()
            b = random.random()
            r = (a**2+b**2)**0.5
            while r > 1:
                a = random.random()
                b = random.random()
                r = (a**2+b**2)**0.5
            try_ += 1
            if r < i:
                inner1 += 1
                if r < k:
                    inner2 += 1
        print(i, k, ":", (inner1/try_), (inner2/try_))
