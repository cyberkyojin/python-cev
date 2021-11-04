num1 = int(input('1 numero: '))
num2 = int(input('2 numero: '))
num3 = int(input('3 numero: '))

if num1 > num2 and num3:
    print('1 numero é o maior')

elif num2 > num3 and num1:
    print('2 numero é o maior')

elif num3 > num1 and num2:
    print('3 numero é o maior')

if num1 < num2 and num3:
    print('1 numero é o menor')

elif num2 < num3 and num1:
    print('2 numero é o menor')

elif num3 < num1 and num2:
    print('3 numero é o menor')
