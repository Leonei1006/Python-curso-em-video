#o objetivo desse algoritimo é ler o nome digitado e dizer o primeiro e último nome do usuário
n = str(input('Qual o seu nome completo? ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
