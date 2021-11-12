#aprovando empréstimo
casa = float(input('Qual o valor da casa? R$'))
salário = float(input("Qual o seu salário? R$"))
anos = int(input('Em quantos anos você quer pagar? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('\033[1;34mPara pagar uma casa de R${:.2f} em {} anos \n'
      'A prestação será de R${:.2f}\033[m'.format(casa, anos, prestação))
if prestação <= mínimo:
    print('\033[1;32mA prestação de R${:.2f} fica dentro do seu orçamento, empréstimo \n'
          'APROVADO, PARABÉNS!!\033[m'.format(prestação))
else:
    print('\033[1;31mA prestação de R${:.2f} compromete a sua renda, EMPRÉSTIMO NEGADO!\033[m'.format(prestação))
