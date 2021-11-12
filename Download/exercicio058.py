#melhorando o jogo do exercicio 28
from random import randint
computador = randint(0, 10)
print('Sou seu computador...Acabei de pensar em um número entre 0 e 10.')
print('Será que consegue adivinhar? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
       acertou = True
    else:
       if jogador < computador:
        print('Mais... Tente mais uma vez.')
       elif jogador > computador:
        print('Menos...Tente mais uma vez.')
print('\033[1;32mAcertou com {} tentativas. PARABÉNS!!!\033[m'.format(palpites))


