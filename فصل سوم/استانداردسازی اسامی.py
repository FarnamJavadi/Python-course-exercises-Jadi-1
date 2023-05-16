def estandard(a):
    a = a.lower()
    first = a[0]
    edame = a[1::]
    first = first.upper()
    return first + edame


listis = []

for i in range(0, 10):
    temp = estandard(input())
    listis.append(temp)

for j in range(0, 10):
    print(listis[j])
