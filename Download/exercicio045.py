#jogando JOKENPÔ contra o computador!!
from random import randint
from time import sleep
itens = ('Pedra',' Papel ', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' *15)
print('O computador escolheu: {}'.format(itens[computador]))
print('O jogador escolheu: {}'.format(itens[jogador]))
print('-=' *15)
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR GANHOU!!!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!!!')
    else:
        print('JOGADA INVÁLIDA!!')

elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU!!!')
    elif jogador == 1:
        print('EMPATE!!!')
    elif jogador == 2:
        print('JOGADOR VENCEU!!!')
    else:
        print('JOGADA INVÁLIDA!!!')

elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU!!!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!!!')
    elif jogador == 2:
        print('EMPATE!!!')
    else:
        print('JOGADA INVÁLIDA!!!')
