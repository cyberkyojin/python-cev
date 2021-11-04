from datetime import date
ano = date.today().year
nasci = int(input('ano de nascimento: '))
idade = ano - nasci

print('nasceu em {} e tem {} anos'.format(nasci, idade))

if idade <= 9:
    print('MIRIM')

elif idade <= 14:
    print('INFANTIL')

elif idade <= 19:
    print('JUNIOR')

elif idade <= 25:
    print('SENIOR')

elif idade > 25:
    print('MASTER')