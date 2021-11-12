somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = 0
totalmulher20 = 0
for p in range(1, 5):
    print('------- {}ª PESSOA -------'.format(p))
    nome = str(input('Nome: ')) .strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')) .strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        totalmulher20 += 1
médiaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(médiaidade))
print('O homem mais velho do grupo tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo temos {} mulheres com menos de 20 anos'.format(totalmulher20))
