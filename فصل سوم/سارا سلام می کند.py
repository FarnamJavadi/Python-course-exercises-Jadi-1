a = input()

a = a.lower()
vaziat = 'NO'
if ('h' in a) and ('e' in a) and ('ll' in a) and ('o' in a):
    vaziat = 'YES'
else:
    vaziat = 'NO'

h = a.find('h')
e = a.find('e')
ll = a.find('ll')
o = a.find('o')
if vaziat == 'YES' and o > ll > e > h:
    vaziat = 'YES'

else:
    vaziat = 'NO'

print(vaziat)
