from random import randint
from operator import itemgetter

dic = { 'jogador1' : randint(1, 6),
        'jogador2' : randint(1, 6),
        'jogador3' : randint(1, 6),
        'jogador4' : randint(1, 6) }

for k, v in dic.items():
    print(f'o {k} tirou {v}\n')

print('-+' * 20)

ordenar = {}
ordenar = sorted(dic.items(), key=itemgetter(1), reverse=True)

for a, b in enumerate(ordenar):
    print(f'     {a + 1}º lugar: {b[0]} que tirou {b[1]}\n')

'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados
em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou 
o maior número no dado.'''