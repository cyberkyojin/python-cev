import math

angulo = float(input('digite o angulo: '))

seno = math.sin(math.radians(angulo))

cosseno = math.cos(math.radians(angulo))

tangente = math.tan(math.radians(angulo))

print('o angulo é de: {:.2f}\n o angulo do seno é: {:.2f}\n o angulo do cosseno é: {:.2f}\n o angulo da tangente é: {:.2f}'.format(angulo, seno, cosseno, tangente))