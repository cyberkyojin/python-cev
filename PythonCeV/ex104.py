def leiaInt(msg):
    valor = 0
    while True:
        num = input(msg)
        if num.isnumeric():
            valor = int(num)
            break
        else:
            print('\033[31mDigite um valor inteiro!\033[m')
    return valor


n = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o número {n}')










'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)'''