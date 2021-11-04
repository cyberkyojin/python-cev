lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        lista[l][c] = int(input(f'Digite o valor para [{l}, {c}]: '))

print('MATRIZ(não formatada): ')
print(lista[0])
print(lista[1])
print(lista[2])