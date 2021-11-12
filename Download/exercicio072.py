# o objetivo desse código é criar uma Tupla que faça uma contagem de 0 a 20
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
        'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num  <= 20:
        break
    print('Tente novamente. ', end='')
print(f'O digitou o número {cont[num]}')

