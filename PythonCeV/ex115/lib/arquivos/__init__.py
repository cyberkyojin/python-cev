from ex115.lib.interface import *

def existeA(arq):
    try:
        a = open(arq, 'r')
        a.close()
    except:
        return False
    else:
        return True


def criarA(arq):
    try:
        a = open(arq, 'w')
        a.close()
    except:
        print('ARQUIVO NAO CRIADO')
    else:
        print(f'ARQUIVO {arq} CRIADO!')

def lerA(arq):
    try:
        a = open(arq, 'r')
    except:
        print('ERRO AO TENTAR LER')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for i in a:
            dado = i.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')
    finally:
        a.close()


def cad(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'a')
    except:
        print('erro ao abrir arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('erro ao cadastrar')
        else:
            print(f'{nome} adicionado! ')
    finally:
        a.close()