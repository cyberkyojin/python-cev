dic = {}

dic['nome'] = input('Nome: ')
dic['media'] = float(input('Média: '))

if dic['media'] >= 7:
    dic['situação'] = 'Aprovado'

elif dic['media'] >= 5 and dic['media'] < 7:
    dic['situação'] = 'Recuperação'

else:
    dic['situação'] = 'Reprovado'

for k, v in dic.items():
    print(f'o(a) {k} é {v}.')


'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela'''