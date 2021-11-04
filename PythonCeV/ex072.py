cont = ('zero', 'um', 'dois', 'tres', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quinze', 'dezesseis', 'dezessete',
        'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('digite o numero: '))
    if num >= 0 and num <= 20:
        break

print(f'foi digitado o numero {cont[num]}')