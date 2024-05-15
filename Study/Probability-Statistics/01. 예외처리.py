sum = 0
count = 0

while count < 3:
    try:
        num = int(input("정수 입력:"))
        sum += num
        count += 1

    except ValueError:
        print("정수 입력")
if count > 0:
    print(sum/count)
else:
    print("정수 없음")

