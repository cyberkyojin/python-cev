from datetime import date
data = date.today().year
nasci = int(input('ano do nascimento: '))
idade = data - nasci

menor = 18 - idade
maior = idade - 18

print('idade: {}'.format(idade))

if idade == 18:
    print('tem que se alistar agora')

elif idade < 18:
    print('nao precisa se alistar ainda')
    print('falta {} anos para voce se alistar'.format(menor))
    print('seu alistamento sera em {}'.format(data + menor))

elif idade > 18:
    print('ja passou seu alistamento')
    print('voce deveria ter se alistado a {} anos atras'.format(maior))
    print('seu alistamento foi em {}'.format(nasci + 18))