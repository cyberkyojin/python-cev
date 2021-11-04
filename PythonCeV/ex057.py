sexo = str(input('sexo[M/F]: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('opção invalida, digite novamente!: ')).upper().strip()[0]
print('sexo {} cadastrado com sucesso.'.format(sexo))