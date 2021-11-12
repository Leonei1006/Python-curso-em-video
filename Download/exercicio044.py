#calcurando os juros nas compras  parceladas
print('{:=^100}' .format (' LOJAS GOMES '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO:
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
    print('A sua compra de R${:.2f} terá um desconto de 10% e sairá por R${:.2f}'.format(preço, total))
elif opção == 2:
    total = preço - (preço * 5 / 100)
    print('A sua  de R${:.2f} terá um desconto de 5%, e sairá por R${:.2f}'.format(preço, total))
elif opção == 3:
    total = preço
    parcela = total / 2
    print('O valor final da sua compra é R${:.2f} e será parcelada em 2x de R${:.2f} SEM JUROS.'.format(preço, parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcelas = total / totparc
    print('A sua compra de R${:.2f} terá um acréscimo de 20% e ficará com valor final de R${:.2f}'.format(preço, total))
    print('Este valor será dividido em {} parcelas de R${:.2f}'.format(totparc,parcelas))
else:
    total = preço
    print('\033[1;31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE E DIGITE UMA OPÇÃO VÁLIDA!\033[M')

print('{:=^100}'.format('AGRADECEMOS À PREFERÊNCIA!!!'))