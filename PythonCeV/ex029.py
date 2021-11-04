velo = int(input('qual a velocidade do carro: '))

mult = 7 * (velo - 80)

if velo > 80:
    print('tera de pagar uma multa de {} reais'.format(mult))
