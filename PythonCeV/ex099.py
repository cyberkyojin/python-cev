def maior(* num):
    cont = maior = 0
    print('-=' * 20)
    print('analisando os valores passados...')
    for valores in num:
        print(valores, end=' ')
        if cont == 0:
            maior = valores
        if valores > maior:
            maior = valores
        cont += 1
    print(f'foram informados "{cont}" valores ao todo')
    print(f'o maior valor informado foi "{maior}".')


maior(4, 0, 0, 2, 8, 9, 2, 2)
