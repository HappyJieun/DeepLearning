import random

r1 = [0.699, 0.703, 0.707, 0.711]

for i in range(101):  # 0부터 100까지 총 101번 반복
    r1.append(i / 100.0)  # 0부터 1까지의 값으로 변환
print(r1)

for i in r1:
    total_try = 5000
    try_ = 0
    inner_try = 0
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
            inner_try += 1
    print(i, ":", (inner_try/try_))
