valor = float(input('valor da compra: '))

print('''TIPO DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque: 10% de desconto.
[ 2 ] à vista no cartão: 5% de desconto.
[ 3 ] em até 2x no cartão: preço normal.
[ 4 ] 3x ou mais no cartão: 20% de juros.''')

opcao = int(input('opção: '))

if opcao == 1:
    print('o preço a vista e com 10% de desconto sera: {}'.format(valor - (valor * 10/100)))

elif opcao == 2:
    print('o preço a vista no cartao e com 5% de desconto sera: {}'.format(valor - (valor * 5/100)))

elif opcao == 3:
    parcela = valor / 2
    print('voce ira pagar {} com 2 parcelas de {} SEM JUROS'.format(valor, parcela))

elif opcao == 4:
    parcela = int(input('quantas parcelas: '))
    preco = valor + (valor * 20/100)
    parcelareal = preco / parcela
    print('voce ira pagar {} reais, em {}x de {} com juros de 20%'.format(preco, parcela, parcelareal))

else:
    print('opção invalida')