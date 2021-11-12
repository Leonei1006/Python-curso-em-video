from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pes in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pes)))
    idade = atual - nasc
    if idade >= 21:
        totalmaior += 1
    else:
       totalmenor += 1
print('Desse total temos {} pessoas maiores de idade.' .format(totalmaior))
print('E também {} pessoas menores de idade.'.format(totalmenor))
