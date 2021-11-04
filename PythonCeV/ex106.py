def ajuda(comando):
    resp = help(comando)
    return resp


while True:
    com = input('\033[35m["FIM" fecha]\033[m \033[92mManual do comando: \033[m')
    if com.upper() == 'FIM':
        break
    ajuda(com)
print('\033[93mFechado!\033[m')


'''Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando
e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante:
use cores.'''