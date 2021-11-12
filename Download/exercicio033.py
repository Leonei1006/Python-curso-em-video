# menor e maior valores
a = int(input('\033[1;35mPrimeiro valor:\033[m '))
b = int(input('\033[1;35mSegundo valor: \033[m'))
c = int(input('\033[1;35mTerceiro valor:\033[m'))
# verificando o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('\033[1;34mO menor valor é {}\033[m'.format(menor))
# verificando maior valor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('\033[1;33mO maior valor é {}\033[m'.format(maior))

