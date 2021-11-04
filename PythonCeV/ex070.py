total = totmil = menor = cont = 0
barato = ''

while True:
    nome = input('nome do produto: ')
    preço = float(input('preço do produto: '))
    cont += 1
    total += preço
    if preço >= 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = input('quer continuar? ').upper()
    if resp == 'N':
        break

print(f'O total da compra foi {total}')
print(f'{totmil} produtos custam mais de 1000 reais')
print(f'O produto mais barato foi {barato} que custa {menor}')