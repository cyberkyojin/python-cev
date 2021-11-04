ano = int(input('ano: '))

bi = ano % 4

if bi == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('ano bissexto')
else:
    print('nao é ano bissexto')