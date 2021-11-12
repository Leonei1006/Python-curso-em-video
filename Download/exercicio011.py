#o objetivo deste código é receber o valor de um produto e dar um desconto de 5%.
preço = float(input('Qual o preço do produto? R$'))
desc = preço - (preço * 5 / 100)
print('Este produto na promoção com 5% de desconto, esta apenas R${:.2f}'.format(desc))
