#análise de desempenho de um jogador de futebol
jogador = dict()
partidas = list()
jogador['nome'] = str(input(('Qual o nome do Jogador? ')))
total = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou? '))
for c in range(0, total):
    partidas.append(int(input(f'  Quantos gols na partida {c+1}? ')))
jogador['gols'] = partidas[:]
jogador['total de gols'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'  O jagador {jogador["nome"]} jogou {len(partidas)} partidas')
for v, i in enumerate(jogador["gols"]):
    print(f'   => NA {v+1}ª PARTIDA FEZ {i} GOLS <=')