primeiro = int(input('primeiro termo: '))
razão = int(input('razão: '))

termo = primeiro

cont = 1

while cont <= 10:
    termo = termo + razão
    cont += 1
    print('{} '.format(termo), end='')