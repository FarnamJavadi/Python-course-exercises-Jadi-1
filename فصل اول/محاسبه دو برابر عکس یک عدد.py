number = int(input())
reverse_num = 0

while number > 0:
    temp = number % 10
    reverse_num = reverse_num * 10 + temp
    number = number // 10
x = reverse_num * 2
print(x)
