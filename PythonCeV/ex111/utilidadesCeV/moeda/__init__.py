def aumentar(preço=0, taxa=0, formato=False):
    resp = preço + (preço * taxa/100)
    return resp if formato == False else moeda(resp)


def diminuir(preço=0, taxa=0, formato=False):
    resp = preço - (preço * taxa/100)
    return resp if formato == False else moeda(resp)


def dobro(preço=0, formato=False):
    resp = preço * 2
    return resp if formato == False else moeda(resp)


def metade(preço=0, formato=False):
    resp = preço / 2
    return resp if formato == False else moeda(resp)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxaA=10, taxaD=10):
    print('-' * 20)
    print(f'{"ReSuMo":^20}')
    print('-' * 20)
    print(f'aumentando {taxaA}% de {preço} fica: {aumentar(preço, taxaA, True)}')
    print(f'diminuindo {taxaD}%  de {preço} fica: {diminuir(preço, taxaD, True)}')
    print(f'o dobro de {preço} é: {dobro(preço, True)}')
    print(f'a metade de {preço} é: {metade(preço, True)}')
