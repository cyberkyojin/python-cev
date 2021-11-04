lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = []
spar = tc = mai = 0
for l in range(0,3):
    for c in range(0,3):
        lista[l][c] = int(input(f'Digite o valor para [{l}, {c}]: '))

print('MATRIZ(não formatada): ')
print(lista[0])
print(lista[1])
print(lista[2])
for i in lista[0]:
    if i % 2 == 0:
        pares.append(i)
for o in lista[1]:
    if o % 2 == 0:
        pares.append(o)
for u in lista[2]:
    if u % 2 == 0:
        pares.append(u)

print(f'A soma dos valores pares foi de: {sum(pares)}')
tc = tc + lista[0][2] + lista[1][2] + lista[2][2]
print(f'A soma dos valores da ultima coluna foi de: {tc}')

for s in lista[1]:
    cont = 0
    if cont == 0:
       mai = lista[1][0]
    if lista[1][1] > mai:
        mai = lista[1][1]
    if lista[1][2] > mai:
        mai = lista[1][2]
    cont += 1

print(f'O maior valor da 2 linha foi: {mai}')
