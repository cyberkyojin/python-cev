num = 0
soma = 0
cont = 0

while num != 999:
    num = int(input('numero[999 fecha]: '))
    cont += 1
    soma = soma + num
print('voce digitou {} numeros e a soma entre eles foi de: {}'.format(cont - 1, soma - 999))