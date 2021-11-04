from random import randint

print('acerte o numero de 0 a 10!')

computador = randint(0,10)

palpite = False
palpites = 0

while not palpite:
    usuario = int(input('qual seu palpite?: '))
    palpites = palpites + 1
    if usuario == computador:
        palpite = True
    else:
        if usuario > computador:
            print('menos... tente novamente!')
        elif usuario < computador:
            print('mais... tente novamente!')

print('acertou depois de {} palpites.'.format(palpites))    