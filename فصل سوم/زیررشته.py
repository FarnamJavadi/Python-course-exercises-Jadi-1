a = input()

a = a.replace('AB', '！')
a = a.replace('BA', '@')

vaziat = ''

if ('!' in a) and ('@' in a):
    vaziat = 'YES'
else:
    vaziat = 'NO'
print(vaziat)
