x = int(input())
c = 0

for i in range(1, x):
    if x % i == 0:
        c += 1

if c == 1:
    print("prime")
else:
    print("not prime")
