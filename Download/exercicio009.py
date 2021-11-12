#o objetivo desse algorítimo e perguntar o usuário quanto $ ele possui na carteira
# e dizer quantos dolares ele pode compra, considerando o dolar R$ 3,27
real = float(input("Quantos reais você tem na carteira? R$"))
dolar = real / 5.53
euro = real / 6.38
print ('Com R${:.2f}, você consegue comprar U$${:.2f} ou €{:.2f} '.format(real, dolar, euro))
