#o objetivo desse algorítimo é ler o primeiro nome da cidade e falar se o primeiro
# nome corresponde ao solicitado
cidade = str(input('Qual o nome da cidade que você nasceu? ')).strip()
print(cidade[:5].upper() == 'SANTO')

