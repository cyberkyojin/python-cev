from random import randint

jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']
escolha = randint(0,2)
jogador = int(input('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
: '''))

if jogador >= 3 or jogador >= -1:
    print('JOGADOR escolheu uma opção invalida')

elif escolha == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')

elif escolha == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')

elif escolha == 2:
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')

print('computador escolheu {}'.format(jokenpo[escolha]))
