lista = [[], []]

print('Digite 7 numeros.')
print('=-' * 12)
for i in range(1,8):
    num = int(input(f'Digite o {i}º valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[1].sort()
print(f'Lista de numeros pares: {sorted(lista[0])}')
print(f'Lista de numeros ímpares: {lista[1]}')