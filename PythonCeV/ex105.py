def notas(*nota, sit=False):
    """
    <documentação foda>
    """
    dic = dict()
    dic['quantidade'] = len(nota)
    dic['maior'] = max(nota)
    dic['menor'] = min(nota)
    dic['media'] = sum(nota) / len(nota)
    if sit:
        if dic['media'] >= 7:
            dic['situação'] = 'Boa'
        elif dic['media'] >= 5:
            dic['situação'] = 'Razoavel'
        else:
            dic['situação'] = 'Ruim'

    return dic 


resp = notas(9, 8, 9, sit=True)
print(notas.__dict__)
