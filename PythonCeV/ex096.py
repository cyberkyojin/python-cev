def area(larg, comp):
    a = larg * comp
    print(f'A area de um terreno {larg}x{comp} é {a}m²')

l = float(input('Largura: '))
c = float(input('Comprimento: '))

area(l, c)
