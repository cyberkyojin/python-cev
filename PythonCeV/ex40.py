nota = float(input('primeira nota: '))
nota2 = float(input('segunda nota: '))

media = (nota + nota2) / 2

if media < 5:
    print('REPROVADO')

elif media >= 5 and media < 6.9:
    print('RECUPERAÇÃO')

elif media >= 7:
    print('APROVADO')