from math import hypot

co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))

print('{:.2f}'.format(hypot(co,ca)))
