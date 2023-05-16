bozorg = 0

while True:
    sen = int(input())
    if sen == -1:
        break
    if sen > bozorg:
        bozorg = sen

print(bozorg)
