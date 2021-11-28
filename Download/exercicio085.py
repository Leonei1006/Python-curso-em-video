#lista com pares e ímpares
núm = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)

print('-=' * 25)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitados são : {núm[0]}')
print(f'Os valores ímpares digitados são: {núm[1]}')