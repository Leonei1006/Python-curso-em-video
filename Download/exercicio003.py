n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print ('A soma é {}, o produto é {} e a divisão é {:.2f} '.format(s, m, d))
print ('divisão inteira {} e potência {}'.format(di,e))