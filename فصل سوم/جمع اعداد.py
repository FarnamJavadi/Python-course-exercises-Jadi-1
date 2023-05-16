s = [i.lower() for i in input()]

for i in s:
    if i == '+':

        s.remove('+')
s.sort()
s = '+'.join(s)

print(s)
