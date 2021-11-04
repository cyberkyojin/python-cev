frase = input('frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)

inverso = ''
for i in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[i]

print(junto, inverso)

if junto == inverso:
    print('é um palindromo')
else:
    print('não é um palindromo')

'''inverso = junto[::-1]
print(junto, inverso)'''