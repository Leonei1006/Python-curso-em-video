# desconsiderando o flag
n = c = s = 0
while True:
    n = int(input('Digite um número [999]  Parar parar: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Você digitou {c} números, e a soma entre eles é {s}.')
print('Acabou!')