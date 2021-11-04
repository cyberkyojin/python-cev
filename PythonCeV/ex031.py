dist = int(input('distancia da viagem: '))

passa = dist * 0.50

passa2 = dist * 0.45

if dist <= 200:
    print('Passagem {:.2f}'.format(passa))
else:
    print('Passagem {:.2f}'.format(passa2))