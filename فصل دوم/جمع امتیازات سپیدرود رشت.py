sum1 = 0
win_counter = 0

for i in range(0, 30):
    vorodi = int(input())
    sum1 += vorodi
    if vorodi == 3:
        win_counter += 1

print(sum1, '', win_counter)
