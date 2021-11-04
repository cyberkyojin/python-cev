palavras = ('aprender', 'programar', 'linguagem', 'python'
            ,'curso', 'gratis', 'estudar')

for i in palavras:
    print(f'\nas vogais de {i.upper()} são: ', end='')
    for l in i:
        if l in 'aeiou':
            print(l, end=' ')

