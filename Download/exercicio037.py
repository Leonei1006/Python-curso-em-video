#conversor de base numéricas
num = int(input('\033[1;34mDigite um número inteiro: \033[m'))
print('''\033[1;34mEscolha uma das bases de conversão:
[1] converter para  BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL\033[m''')
opção = int(input('\033[1;35mSua opção: \033[m'))
if opção == 1:
    print('\033[1;32mO numéro {} em BINÁRIO é {}.\033[m'.format(num, bin(num)[2:]))
elif opção == 2:
    print('\033[1;32mO número {} em OCTAL é {}\033[m'.format(num, oct(num)[2:]))
elif opção == 3:
    print('\033[1;32mO número {} em HEXADECIMAL é {}\033[m'.format(num, hex(num)[2:]))
else:
    print('\033[1;31mOpção inválida, escolha outra opção.\033[m')