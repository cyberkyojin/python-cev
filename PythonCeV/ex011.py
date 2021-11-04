lar = float(input('qual a largura da parede?(m): '))
alt = float(input('qual a altura da parede?(m): '))

area = lar * alt

metroq = area / 2

print('a area é: {} metros, e sera necessario {} litros de tinta.'.format(area, metroq))