#o objetivo deste algoritimo é dizer quantas vezes aparece a letra (A) em uma frase digitada
# pelo usuário, a posição da primeira e última vez que ela aparece
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A apareceu {} vezes'.format(frase.count('A')))
print('A primeira vez foi na posição {}'.format(frase.find('A')+1))
print('A última vez foi na posição {}'.format(frase.rfind('A')+1))