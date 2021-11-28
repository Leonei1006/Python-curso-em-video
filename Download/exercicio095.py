#aprimorando dicionários
#análise de desempenho de um jogador de futebol
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input(('Qual o nome do Jogador? '))).upper()
    total = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, total):
        partidas.append(int(input(f'  Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total de gols'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S|N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('Cod ', end='')
for i in jogador.keys():
    print(f' {i:<13} ', end='')
print()
print('-' * 50)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f' {str(d):<13} ', end='')
    print()
print('-' * 50)
while True:
    busca = int(input('Mostrar os dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'   No jogo {i+1} fez {g} gols')
    print('-' * 40)
print('<<< VOLTE SEMPRE >>>')


