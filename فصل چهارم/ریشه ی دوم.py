import math

n = int(input())

result = []

for i in range(1, n + 1):
    number = int(input())
    radical = math.sqrt(number)
    result.append(radical)


for j in result:
    eight = (f'{j:.8f}')
    four = eight[:-4]
    print(four)