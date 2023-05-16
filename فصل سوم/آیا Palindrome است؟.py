def palindrome(hey):
    lenny = len(hey)
    vaziat = True
    temp = hey[::-1]
    for i in range(0, lenny):
        if hey[i] != temp[i]:
            vaziat = False
    return vaziat


a = input()
a = a.lower()

if palindrome(a):
    print('palindrome')
else:
    print('not palindrome')
