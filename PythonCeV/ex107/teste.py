import moeda

p = float(input('Digite o preço: R$'))

print(f'aumentando 10% de R${p} fica: {moeda.aumentar(p, 10)}')
print(f'diminuindo 10% de R${p} fica: {moeda.diminuir(p, 10)}')
print(f'o dobro de {p} é {moeda.dobro(p)}')
print(f'a metade de {p} é {moeda.metade(p)}')