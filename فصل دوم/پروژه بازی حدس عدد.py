import random

x = 1
y = 99

hads = random.randint(x,y)
print(hads)
javab = input()

while javab != 'd':
    if javab == 'k':
        y = hads
        hads = random.randint(x,y)
        print(hads)
        javab = input()
    elif javab == 'b':
        x = hads
        hads = random.randint(x,y)
        print(hads)
        javab = input()
