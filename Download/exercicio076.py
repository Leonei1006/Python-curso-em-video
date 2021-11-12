# o objetivo desse algorítimo é criar uma tupla e captar os valores e itens digitados pelo usuário
print('-' * 40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-' * 40)
listagem = ('Lápis', 1.75,
            'Borracha', 2.50,
            'Lapiseira', 19.90,
            'Caderno', 39.90,
            'Taboada', 9.90,
            'Livro', 49.90,
            'Caneta', 3.90,)
for pos in  range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)