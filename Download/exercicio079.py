# criando uma lista com valores indicados pelo usuário sem repetir valores
números = list()
while True:
    n = int(input('Digite um número: '))
    if n not in números:
           números.append(n)
           print('Número adionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    r = str(input('Quer continuar? [S|N] '
                  '')).strip().upper()
    if r in 'Nn':
        break
print('-=' * 25)
números.sort()
print(f'Você digitou os valores {números}.')
