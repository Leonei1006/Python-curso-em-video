núm = cont = soma = 0
núm = int(input('Digite um número [999 pra parar] '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 pra parar] '))
print('Você digitou {} números e a soma é {}.'.format(cont, soma))
print('ACABOU')