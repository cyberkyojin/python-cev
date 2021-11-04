def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade <= 15:
        print(f'Com {idade} anos, NÃO VOTA.')
    elif idade >= 16 and idade <= 17 or idade >= 65:
        print(f'Com {idade} anos, É OPCIONAL.')
    elif idade >= 18:
        print(f'Com {idade} anos, É OBRIGATORIO.')


ano = int(input('Ano de nascimento: '))
voto(ano)
