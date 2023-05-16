reshte = input()
reshte = reshte.lower()
reshte = reshte.replace('a','')
reshte = reshte.replace('e','')
reshte = reshte.replace('i','')
reshte = reshte.replace('o','')
reshte = reshte.replace('u','')
nahaii = ''
for i in range(0,len(reshte)):
    nahaii += '.'+reshte[i]
print(nahaii)
