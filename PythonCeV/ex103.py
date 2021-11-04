def ficha(nome='<desconhecido>', gol=0):
    print(f'O jogador {nome} fez {gol} gol(s)')

n = input('Nome: ')
g = input('Gols: ')

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n == '':
    ficha(gol=g)
else:
    ficha(n, g)
