a = int(input())
b = [int(i) for i in input().split(' ')]

temp = []
for i in range(0, len(b)):
    temp.append(int(b[i]))

coun = 0
for j in range(0, len(temp)):
    if temp[j] == 0 or temp[j] == 1 or temp[j] == 2:
        coun += 1

print(int(coun / 3))
