import moeda
p = float(input('Digite o preço: '))

print(f'aumentando 10% de {moeda.moeda(p)} fica: {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'diminuindo 10% de {p} fica: {moeda.moeda(moeda.diminuir(p, 10))}')
print(f'o dobro de {p} é {moeda.moeda(moeda.dobro(p))}')
print(f'a metade de {p} é {moeda.moeda(moeda.metade(p))}')