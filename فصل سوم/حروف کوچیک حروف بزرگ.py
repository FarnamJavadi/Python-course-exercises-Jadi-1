def lo_counter():
    I_counter = 0
    lo = a.lower()
    for i in range(0, int(len(a))):
        if a[i] == lo[i]:
            I_counter += 1
    return I_counter


def up_counter():
    u_counter = 0
    up = a.upper()
    for j in range(0, int(len(a))):
        if a[j] == up[j]:
            u_counter += 1
    return u_counter


a = input()

vaziat = True

if lo_counter() == up_counter():
    vaziat = True
if lo_counter() > up_counter():
    vaziat = True
if lo_counter() < up_counter():
    vaziat = False
if vaziat:
    a = a.lower()
else:
    a = a.upper()

print(a)
