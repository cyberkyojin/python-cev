from datetime import datetime

dic = {}

dic['nome'] = input('Nome: ')
nasc = int(input('Ano de nascimento: '))
dic['idade'] = datetime.now().year - nasc
dic['ct'] = int(input("Carteira de trabalho ('0' = nao tem): "))

if dic['ct'] != 0:
    dic['contratação'] = int(input('Ano de contratação: '))
    dic['salario'] = float(input('Salario: '))
    dic['aposentadoria'] = dic['idade'] + ((dic['contratação'] + 35) - datetime.now().year)

print('-=' * 30)
for k, v in dic.items():
    print(f'{k}: {v}')


'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''