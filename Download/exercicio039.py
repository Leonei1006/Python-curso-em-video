#ano de alistamento
from datetime import date
atual = date.today().year
nascimento = int(input('\033[1;34mQual o ano do seu nascimento? \033[m'))
idade = atual - nascimento
print('\033[1;34mQuem nasceu em {} tem {} anos em {}.\033[m'.format(nascimento, idade, atual))
if idade == 18:
    print('\033[1;33Você precisa se alista IMEDIATAMENTE!\033[m'.format(nascimento,idade))
elif idade > 18:
    saldo = idade - 18
    print('\033[1;31mVocê deveria ter se alistado há {} anos.\033[m'.format(saldo))
    ano = atual - saldo
    print('\033[1;31mSeu alistamento foi no ano {}\033[m'.format(ano))
else:
    saldo = 18 - idade
    print('\033[1;32mAinda faltam {} anos para o seu alistamento.\033[m'.format( saldo))
    ano = atual + saldo
    print('\033[1;32mSeu alistamento será no ano {}\033[m'.format(ano))

