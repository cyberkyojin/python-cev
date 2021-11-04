num = int(input('numero: '))

result = int(input('converta {} para:\n[1] binario\n[2] octal\n[3] hexadecimal\n-- '.format(num)))

if result == 1:
    print(bin(num))
elif result == 2:
    print(oct(num))
elif result == 3:
    print(hex(num))
else:
    print('opção invalida')