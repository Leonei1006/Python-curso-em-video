#ano bissexto
from datetime import date
ano = int(input('\033[1;33mQual ano você quer analisar? Coloque 0 para o ano atual.\033[m '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[1;34mO ano {} é Bissexto.\033[m'.format(ano))
else:
    print('\033[1;32mO ano {} não é Bissexto.\033[m'.format(ano))