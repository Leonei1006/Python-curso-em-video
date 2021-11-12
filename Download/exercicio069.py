total18 = totalM20 = totalH = totalM = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
       sexo = str(input('Sexo: [M/F ')).strip().upper()[0]
    if idade >= 18:
        total18 += 1
    if sexo =='M':
        totalH += 1
    if sexo == 'F':
        totalM += 1
    if sexo == 'F' and idade < 20:
        totalM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos : {total18}')
print(f'Total de homens cadastrados {totalH}.')
print(f'Total de mulheres cadastradas {totalM} e {totalM20} são menores de 20 anos.')
