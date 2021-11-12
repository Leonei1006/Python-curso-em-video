# detector de palídromo
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = "" .join(palavras)
inverso = junto[:: -1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('Não temos um PALÍNDROMO!')
