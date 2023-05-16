from collections import OrderedDict

n = int(input())
dictionary = OrderedDict()


for i in range(1, n + 1):
    word = input()
    word = word.split()
    real = word[0]
    translate = word[1]
    dictionary[real] = translate


keylist = list(dictionary.keys())
valuelist = list(dictionary.values())

sent = input()
sent = sent.split()

result = ''

for part in sent:
    if part in dictionary:
        result += dictionary[part] + ' '
    else:
        result += part + ' '

result = result[:-1]
print(result)