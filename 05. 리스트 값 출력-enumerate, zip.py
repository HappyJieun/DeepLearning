# enumerate 함수 : 리스트 값을 인덱스와 함께 출력
for i, v in enumerate(['tic', 'tac', 'toc']):
    print(i, v)
print()

# 직접 구현
s = ['tic', 'tac', 'toc']
for i in range(len(s)):
    print(i, s[i])

print()
######################################################
# zip 함수 : 리스트 값을 병렬로 묶어 출력
alist = [1, 2, 3, 4]
blist = [5, 6, 7, 8]
for a, b in zip(alist, blist):
    print(a, b)
print()

# 직접 구현 
a=[1,2,3,4]
b=[5,6,7,8]
c=[]
for i in range(len(a)):
    c.append((a[i],b[i]))
for a, b in c:
    print(a,b)
print()

# zip 파헤치기 
a = [1,2,3]
b = [4,5,6]
c = zip(a,b) # c는 튜플
print(c)
print(list(c))
print()
a, b, c= zip((1,2,3),(10,20,30),(100,200,300))
print(a,b,c)

# 같이 사용
k = [1, 2, 3]
m = [4, 5, 6]
for i, (a, b) in enumerate(zip(k, m)):
    print(i, a, b)

# sum
print([sum(x) for x in zip((1,2,3),(10,20,30),(100,200,300))])
