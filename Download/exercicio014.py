#o objetivo desse código e calcular os Km percorridos por um carro alugado e somar
# ao seu valor de aluguel diário
dias = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('Você alugou o carro  por {} dias e rodou {}km, o valor a ser pago é R${:.2f}'.format(dias, km, pago))

