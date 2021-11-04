resp = 'S'
quant = 0
soma = 0
maior = 0
menor = 0

while resp == 'S':
    num = int(input('insira um numero: '))
    quant += 1
    soma += num
    resp = input('deseja continuar[S/N]? ').upper().strip()
    media = soma / quant
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < maior:
            menor = num
        

print('voce digitou {} numeros e a media dos valores inseridos foi: {}'.format(quant, media))
print('o maior numero foi {} e o menor foi {}'.format(maior, menor))



'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores'''