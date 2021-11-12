# par ou ímpar
num = int(input('\033[32mDigite um número e te direi se ele é par ou ìmpar:\033[m '))
resultado = num % 2
if resultado == 1:
    print('\033[31mO número {} é ÍMPAR\033[m'.format(num))
else:
    print('\033[33mO número {} é PAR\033[m'.format(num))

