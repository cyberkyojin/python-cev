cont = 0
soma = 0

for i in range(1, 7):
    num = int(input('digite o {} valor: '.format(i)))
    if num%2 == 0:
        soma = soma + num
        cont = cont + 1
print('voce informou {} numeros pares e a soma foi: {}'.format(cont, soma))
    
