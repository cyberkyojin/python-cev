def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! digite um numero valido!\033[m')
        except (KeyboardInterrupt):
            print('\033[31mUsuario interrompeu.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! digite um numero valido!\033[m')
        except (KeyboardInterrupt):
            print('\033[31mUsuario interrompeu.\033[m')
            return 0
        else:
            return n

print(leiaInt('digite um numero inteiro: '))
print(leiaFloat('digite um numero float: '))
'''Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um
número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''
