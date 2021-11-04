from ex115.lib.interface import *
from ex115.lib.arquivos import *
from time import sleep

arq = 'pessoas.txt'

if not existeA(arq):
    criarA(arq)

while True:
    cabecalho('\033[35mMENU PRINCIPAL\033[m')
    m = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if m == 1:
        lerA(arq)
    elif m == 2:
        cabecalho('Cadastrar nova pessoa')
        nome = input('nome: ')
        idade = leiaInt('idade: ')
        cad(arq, nome, idade)
    elif m == 3:
        print('\n\033[32mSaindo do sistema...\033[m')
        break
    else:
        print('\033[31mOpção inválida\033[m')
        sleep(0.5)
