n = int(input())

prices = []
values = []

for i in range(1, n + 1):
    enter = input()
    enter = enter.split()
    prices.append(int(enter[0]))
    values.append(int(enter[1]))



result = False
tedad = 0
counter = -1
for i in prices:
    counter += 1
    rest = prices[:counter] + prices[(counter + 1):]
    valuerest = values[:counter] + values[(counter + 1):]
    restcounter = -1
    for j in rest:
        restcounter += 1
        if prices[counter] <= rest[restcounter]:
            tedad += 1
            small = prices[counter]
            big = rest[restcounter]
            if values[counter] >= valuerest[restcounter]:
                result = True

            
if result == True:
    print("happy irsa")
else:
    print("poor irsa")