def l():
    print('-=' * 20)


def contador(i, f, p):
    print(f'contagem de {i} até {f} de {p} em {p}\n')
    if p < 0:
        p *= -1
    
    if p == 0:
        p = 1

    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=' ')
            cont += p
        print('// Fim')
        l()

    else:
        cont = i
        while cont >= f:
            print(cont, end=' ')
            cont -= p
        print('// Fim')
        l()


contador(1, 10, 1)
contador(10, 0, 1)

print('Agora você!\n')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))

contador(ini, fim, pas)