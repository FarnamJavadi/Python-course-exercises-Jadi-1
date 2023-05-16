from collections import OrderedDict

ara = OrderedDict()

n = int(input())

for i in range(1, n + 1):
    name =  input()
    ara[name] = ara.get(name , 0) + 1

keylist = list(ara.keys())
keylist.sort()

for this_one in keylist:
    value = ara[this_one]
    print(this_one , value)