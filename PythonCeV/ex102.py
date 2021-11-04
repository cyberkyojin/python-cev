def fatorial(num=0, show=False):
    """
    ver o fatorial de um numero.
    parametro 'num': o numero que vc quer o fatorial;
    parametro 'show': se vc quer ver a conta;
    return: o valor do fatorial do num(que foi passado).
    """
    f = 1
    for c in range(num, 0, -1):
        f = f * c
        if show:
            print(c, end='')
            if c <= 1:
                print(' = ', end='')
            if c > 1:
                print(' x ', end='')
    return f


print(fatorial(5))
help(fatorial)
