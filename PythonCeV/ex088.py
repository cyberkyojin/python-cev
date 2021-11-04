from random import randint

num = randint(1, 60)

lista = []
jogos = []

print('-' * 21)
print('      MEGA SENA')
print('-' * 21)
qt = int(input('Quantos jogos?: '))

tot = 1

while tot <= qt:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont == 6:
            break    
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print(f'SORTEANDO {qt} JOGOS')

for i, o in enumerate(jogos):
    print(f'JOGO {i+1}: {o}')
       