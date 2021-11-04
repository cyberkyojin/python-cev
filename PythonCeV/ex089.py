lista = []

while True:
    nome = input('Nome: ')
    nota1 = int(input('1º Nota: '))
    nota2 = int(input('2º Nota: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])

    r = input('Quer continuar?: ')
    if r in 'Nn':
        break

print(f'{"Nº":<4} {"NOME":<10} {"MEDIA":>8}')
print('-' * 30)
for i, o in enumerate(lista):
    print(f'{i:<4} {o[0]:<10} {o[2]:>7.1f}\n')

while True:
    print("666' fecha o programa.")
    ind = int(input('Qual o aluno(N)?: '))
    if ind == 666:
        break
    if ind <= len(lista) -1:
        print(f'Notas de {lista[ind][0]} são {lista[ind][1]}')

'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa 
mostrar as notas de cada aluno individualmente.'''