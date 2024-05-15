s_i ={}
s_i = dict()
print(type(s_i))
s_i["키"]="1"
print(s_i)

s_i[1]="kim"
print(s_i)

s_i[2]="lee"
print(s_i)

s_i[3]="kim"
s_i[1]="jim"
print(s_i)

if 2 in s_i:
    print("있음") # 키 값으로 접근
    
print()
print(s_i.keys())
print(s_i.values())
print(s_i.items())
print(s_i[1])
print(s_i.get(1))

print({i:j for i, j in enumerate('My name is jieun lee'.split())})
