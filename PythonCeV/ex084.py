lista = []
temp = []
mai = men = 0 
while True:
    temp.append(input('Nome: '))
    temp.append(int(input('Peso: ')))
    
    if len(lista) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    lista.append(temp[:])
    temp.clear()

    r = input('Quer continuar? [s/n]: ')
    if r in 'Nn':
        break
print('=-' * 30)
print(f'{len(lista)} pessoas cadastradas.')
print(f'Maior peso: {mai} de ', end='')
for p in lista:
    if p[1] == mai:
        print(f'{p[0]}')
print(f'Menor peso: {men} de ', end='')
for p in lista:
    if p[1] == men:
        print(f'{p[0]}')