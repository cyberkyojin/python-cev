num = (int(input('digite um numero: ')), int(input('digite um numero: ')),
    int(input('digite um numero: ')), int(input('digite um numero: ')))

print('-' * 15)
print(f'o 9 apareceu {num.count(9)} vezes')
print('-' * 15)
if 3 in num:
    print(f'o 3 apareceu na {num.index(3)+1} posição')
else:
    print('nao tem 3')
print('-' * 15)
print('os numeros pares foram: ', end='')
for i in num:
    if i % 2 == 0:
        print(i, end=' ')