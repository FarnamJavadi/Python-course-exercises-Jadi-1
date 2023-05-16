s = input()
x1, x2, x3 = s.split(' ')
x1 = int(x1)
x2 = int(x2)
x3 = int(x3)

print(max(x1, x2, x3) - min(x1, x2, x3))
