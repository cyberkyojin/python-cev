pt = int(input('primeiro termo: '))
r = int(input('razão: '))
calc = pt + (11 - 1) * r

for i in range(pt, calc, r):
    print(i)