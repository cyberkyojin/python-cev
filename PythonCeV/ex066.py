soma = 0
cont = 0

while True:
    num = int(input('digite um numero: '))
    if num == 999:
        break
    cont = cont + 1
    soma = soma + num

print(f'digitou {cont} numeros e a soma entre eles foi de {soma}')
