#o objetivo desse código é receber as dimensões de uma parede e calcular a quantos litros de tinta serão
#nescessários para fazer a pintura, estou levando em consideração que cada litro de tinta cobre 2m².
largura = float(input('Qual a largura da sua parede?'))
altura = float(input('Qual a altura da sua parede?'))
dimensão = largura * altura
tinta = dimensão / 2
print('Sabendo que a dimenãso da sua parede é {}x{} e sua área é de {:.2f}m².'
      '\nVocê precisará de {:.1f}l de tinta para pinta-la.'.format(largura, altura, dimensão,tinta))
