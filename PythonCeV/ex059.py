n1 = int(input('primeiro numero: '))
n2 = int(input('segundo numero: '))

print('o que deseja fazer: ')

print('''[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NUMEROS
[ 5 ] SAIR DO PROGRAMA\n''')

numesc = print('NUMEROS ESCOLHIDOS: {} e {}\n'.format(n1, n2))

opção = ''
while opção != 5:
    opção = int(input('>> '))

    if opção == 1:
        print(n1 + n2)
    elif opção == 2:
        print(n1 * n2)
    elif opção == 3:
        if n1 > n2:
            print('{} é maior.'.format(n1))
        elif n1 == n2:
            print('os dois sao iguais.')
        else:
            print('{} é maior.'.format(n2))
    elif opção == 4:
        n1 = int(input('digite o primeiro numero novamente: '))
        n2 = int(input('digite o segundo numero novamente: '))
    elif opção > 5:
        print('opção invalida. digite novamente:')

print('programa fechado.')