# classificando os nadadores
from datetime import date
atual = date.today().year
nascimento  = int(input('Em que ano o atleta nasceu? '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if 9 >= idade:
    print('Classificação: MIRIM.')
elif idade <= 14:
    print('Classificação: IFANTIL.')
elif idade <= 19:
    print('Classificação: JÚNIOR.')
elif idade <= 25:
    print('Classificação: SÊNIOR.')
else:
    print('Classificação: MASTER.')





