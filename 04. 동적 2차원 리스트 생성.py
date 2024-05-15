s = []

row = 3
col = 5
i = 0
for i in range(row):
    s += [[i]*col]
    i += 1

rows = len(s)
cols = len(s[0])

for r in range(rows):
    for c in range(cols):
        print(s[r][c], end=",")
    print()


