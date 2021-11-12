#refazendo a taboada com for
num = int(input('Digite um número pra ver a sua taboada:'))
from time import sleep
for c in range(1, 11):
   print("{} x {:2} = {} ".format(num, c, num * c))
   sleep(0.5)
print('FIM!!')