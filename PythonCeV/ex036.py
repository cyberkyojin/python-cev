casa = float(input('valor da casa: '))
salario = float(input('seu salario: '))
anos = int(input('em quantos anos ira pagar? '))

prest = casa / (anos * 12)

print('para pagar uma casa de {} reais, com um salario de {:.2f}\nsera preciso pagar {:.2f} de prestação'.format(casa, salario, prest))

mini = salario * (30 / 100)

if prest <= mini:
    print('concedido')
else:
    print('nao foi possivel')