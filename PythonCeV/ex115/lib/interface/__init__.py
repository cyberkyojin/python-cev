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


def linha(tam=43):
    return '-' * tam


def cabecalho(msg):
    print(linha())
    print(f'{msg.center(43)}')
    print(linha())


def menu(listaa):
    cont = 1
    for i in listaa:
        print(f'\033[93m{cont}\033[m - {i}')
        cont += 1
    print(linha())
    opc = leiaInt('\033[92mOpção: \033[m')
    return opc
