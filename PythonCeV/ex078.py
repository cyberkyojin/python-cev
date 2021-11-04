listanum = []
mai = 0
men = 0
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))   
    if c == 0:
        mai = listanum[c]
        men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]

print('-='*30)
print(f'Voce digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições: ', end='')
for i, v in enumerate(listanum):
    print(f'maior I: {i} maior V: {v}')
    if v == mai:
        print(f'v == mai  V: {v} MAI: {mai}')
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men} nas posições: ', end='')
for i, v in enumerate(listanum):
    print(f'menor I: {i} menor V: {v}')
    if v == men:
        print(f'v == men   V: {v} MEN: {men}')
        print(f'{i}...', end='')
print()