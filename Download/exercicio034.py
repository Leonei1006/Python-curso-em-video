#aumentos múltiplos
salário = float(input('\033[1;33mQual o salário do funconário? R$\033[m '))
if salário <= 1200:
    novo = salário + (salário * 15 / 100)
    print('\033[1;32mSeu salário atual é de R${:.2f}. Seu novo salário será de R${:.2f}\033[m'.format(salário, novo))
else:
    novo = salário  + (salário * 10 / 100)
    print('\033[1;32mSeu salário atual é de R${:.2f}. Seu novo salário será de R${:.2f}\033[m'.format(salário, novo))


