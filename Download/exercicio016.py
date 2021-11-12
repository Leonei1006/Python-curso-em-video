#o objetivo desse algoritio é fazer a quebra de um número
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format (num, trunc(num)))