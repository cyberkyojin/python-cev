from random import choice

numero = [1,2,3,4,5] 

vtnc = choice(numero)

usuario = int(input('tente acertar o numero de 1 a 5: '))

print('')

if usuario == vtnc:
    print('ACERTOU!\n')
else:
    print('ERROU :(\n')

print('o numero foi: {}'.format(vtnc))
