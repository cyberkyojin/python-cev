from random import randint


total = 0
soma = 0

while True:
    computador = randint(1, 10)
    jogador = input('Par ou Impar: ').upper().strip()[0]
    num = int(input('numero: '))
    total = num + computador
    print('Par' if jogador in 'P' else 'Impar')
    print(f'jogador = {num} e computador = {computador}, total = {total}')
    if jogador in 'P':
        if total % 2 == 0:
            print('jogador ganhou')
        else:
            break
    elif jogador in 'I':
        if total % 2 >= 1:
            print('jogador ganhou')
        else:
            break

print('computador ganhou')

'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. '''