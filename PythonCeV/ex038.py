num1 = int(input('primeiro numero: '))
num2 = int(input('segundo numero: '))

if num1 > num2:
    print('primeiro numero é maior')

elif num2 > num1:
    print('segundo numero é maior')

elif num1 == num2 and num2 == num1:
    print('numeros iguais')

else:
    print('opção invalida')