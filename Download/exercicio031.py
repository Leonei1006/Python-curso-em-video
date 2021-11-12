#custo de viagem
distância =  float(input('\033[1;32mQual a diastância da sua viagem?\033[m '))
print('\033[1;33mVocê está prestes a começão uma viagem de {:.0f}Km.\033[m'.format(distância))
#forma simplificada
#preço = distância * 0.50 if distância <=200 else distância * 0.45
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45

print('\033[1;34mO valor da vigem será de R${:.2f}\033[m'.format(preço))