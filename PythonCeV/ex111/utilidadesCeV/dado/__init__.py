def leiaDinheiro(msg):
    validacao = False
    while validacao == False:
        entrada = input(msg).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print('\033[31mERRO! Digite um numero válido\033[m')
        else:
            validacao = True
            return float(entrada)
