score_list = []

num = 0
while num < 3:
    score = int(input("점수 입력"))
    score_list.append(score)
    num += 1

sum = 0
num = 0

while num < 3:
    if (score_list[num] >= 50):
        sum += score_list[num]
        num += 1
    else:
        break

if (num == 3):
    print(sum)
    print(sum/len(score_list))
else:
    print("과락 존재")

        



    
    
