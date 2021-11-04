nu = int(input('digite o numero: '))

u = nu % 10
d = nu // 10 % 10
c = nu // 100 % 10
m = nu // 1000 % 10

print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))