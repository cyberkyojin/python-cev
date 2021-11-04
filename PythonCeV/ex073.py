times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense',
        'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR', 'Bragantino', 'Ceará',
        'Corinthians', 'Atlético-GO', 'Bahia', 'Sport', 'Fortaleza', 'Vasco', 'Goiás',
        'Coritiba', 'Bota fogo', 'Chapecoense')

print('Times brasileirao 2020:')
print('')
for t in times:
    print(t)
print('-' * 30)
print(f'PRIMEIROS 5 TIMES: {times[0:5]}')
print('-' * 30)
print(f'ULTIMOS 4 COLOCADOS: {times[-4:]}')
print('-' * 30)
print(f'TIMES EM ORDEM ALFABETICAS: {sorted(times)}')
print('-' * 30)
print(f'CHAPECOENSE ESTA NA POSIÇÃO: {times.index("Chapecoense")+1}')
