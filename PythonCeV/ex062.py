primeiro = int(input('primeiro termo: '))
razão = int(input('razão: '))

termo = primeiro

cont = 1
total = 0
amais = 10

while amais != 0:
    total = total + amais
    while cont <= total:
        print('{} '.format(termo), end='')
        termo = termo + razão
        cont += 1
    print('')
    amais = int(input('quantos termos a mais: '))

print('programa fechado')