#calculando a área de um terreno com funções

def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {l} x {c} é de {a}m² ')


#programa principal
print('    CONTROLE DE TERRENOS  ')
print('-=' * 20)
l = float(input('Largura (m): '))
c = float(input('Comprimeto (m): '))
área(l, c)



