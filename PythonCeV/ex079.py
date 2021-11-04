lista = list()
while True:
    n = int(input('DIGITE O NUMERO: '))
    if n not in lista:
        lista.append(n)
        print('VALOR ADICIONADO!')
    else:
        print('ESTE VALOR JA FOI DIGITADO.')

    r = input('DESEJA CONTINUAR[S/N]? ').upper()
    if r == 'N':
        break
print(f'SUA LISTA: {lista}')