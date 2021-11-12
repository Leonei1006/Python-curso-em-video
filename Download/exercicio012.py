#o objetivo do código e somar 15% ao salário do funcionário
salario = float(input('Qual o salário do funcionário? R$ '))
novo = salario + (salario * 15 / 100)
print('O seu novo salário é R${:.2f}'.format(novo))