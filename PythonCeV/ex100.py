from random import randint

numeros = []

def sorteia():
    for cont in range(0,5):
        n = randint(1, 10)
        numeros.append(n)
    print(numeros)


def somaPar():
    soma = 0
    for cont in numeros:
        if cont % 2 == 0:
            soma += cont
    print(f'A soma dos valores pares foi {soma}')


sorteia()
somaPar()