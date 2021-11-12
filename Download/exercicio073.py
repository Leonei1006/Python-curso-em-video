#tabela do brasileirão série A 2021
times = ('Atlético-MG', 'Palmeiras', 'Flamengo', 'Red Bull Bragantino', 'Fortaleza',
         'Corinthians','Internacional', 'Fluminense', 'Cuiabá', 'Ceará',
         'Athlético-PR', 'América-MG', 'Atlético-GO',
         'São Paulo', 'Bahia', 'Santos', 'Sport',
         'Juventude', 'Grêmio', 'Chapecoense')
print('-=' * 15)
print(f'Lista de times do Brasileirão 2021: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 15)
print(f'Em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'A Chapecoense está na {times.index("Chapecoense")+ 1}ª posição.')

