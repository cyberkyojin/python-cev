import moeda
p = float(input('Digite o preço: '))

print(f'aumentando 10% de {p} fica: {moeda.aumentar(p, 10, True)}')
print(f'diminuindo 10% de {p} fica: {moeda.diminuir(p, 10, True)}')
print(f'o dobro de {p} é {moeda.dobro(p, True)}')
print(f'a metade de {p} é {moeda.metade(p, True)}')
