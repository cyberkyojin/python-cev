pessoas = {}
galera = []

soma = media = 0

while True:
    pessoas.clear()
    pessoas['nome'] = input('Nome: ')
    while True:
        pessoas['sexo'] = input('Sexo [M/F]: ').upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('Apenas M ou F')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    galera.append(pessoas.copy())
    while True:
        resp = input('Quer continuar [S/N]: ').upper()[0]
        if resp in 'SN':
            break
        print('Apenas S ou N')
    if resp == 'N':
        break

print('-=' * 30)
print(f'{len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'a media de idade é: {media:.2f}')
print(f'Mulheres: ', end='')

for m in galera:
    if m['sexo'] == 'F':
        print(f'{m["nome"]}', end=', ')

for p in galera:
    if p['idade'] > media:
        print(p['nome'])
'''um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''