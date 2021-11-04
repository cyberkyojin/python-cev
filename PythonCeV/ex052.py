num = int(input('numero: '))
cont =  0

for i in range(1, num+1):
    if num%i == 0:
        cont = cont + 1

print('foi dividido por {} numeros:'.format(cont))
if cont == 2:
    print('é primo')
else:
    print('nao e primo')