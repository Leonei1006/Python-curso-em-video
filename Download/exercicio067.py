# taboada 3.0
cont = num = 1
while True:
    num = int(input('Digite um número para ver a taboada: '))
    print('-=' * 18)
    if num < 0:
        break
    for cont in range(1, 11):
        print(f'{num} x {cont} = {num * cont}')
    print('-=' * 18)
print('\033[1;32mPPROGRAMA DE TABOADA ENCERRADO. VOLTE SEMPRE!\033[m')