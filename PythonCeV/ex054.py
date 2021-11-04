from datetime import date
atual = date.today().year

maiores = 0
menores = 0

for pessoas in range(1, 7 + 1):
    nasc = int(input('ano de nascimento: '))
    idade = atual - nasc
    print(idade)

    if idade >= 21:
        maiores = maiores + 1      
    else:
        menores = menores + 1

print('{} sao maiores'.format(maiores))
print('{} sao menores'.format(menores))