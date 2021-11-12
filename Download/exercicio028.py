#jogo da adivinhação
from random import randint
from time import sleep
computador = randint(0,5) #faz o computador pensar
print('\033[;34m-=\033[m' *30)
print('\033[;33mVou pensar em um número entre 0 e 5, tente adivinhar...\033[m' )
print('\033[;34m-=\033[m'*30)
jogador = int(input('\033[35m Em que número eu pensei?\033[m ')) #jogador tenta adivinhar
print('\033[35m PROCESSANDO...\033[m')
sleep(3)
if jogador == computador:
    print('\033[;32m PARABÉNS! Você ganhou!')
else:
    print('\033[1;31m GANHEI! Eu pensei no número {} e não no {}.\033[m'.format(computador, jogador))

