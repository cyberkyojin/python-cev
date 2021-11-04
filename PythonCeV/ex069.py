totM = totF = totI = 0
while True:
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('sexo [M/F]: ').upper()
    if idade >= 18:
        totI += 1
    if sexo == 'M':
        totM += 1
    if sexo =='F' and idade < 20:
        totF += 1
    resp = ' '
    while resp not in 'SN':
        resp= input('quer continuar? ').upper()
    if resp == 'N':
        break
print(f'{totI} pessoas tem mais de 18 anos')
print(f'{totM} homens foram cadastrados')
print(f'{totF} mulheres com menos de 20 anos')