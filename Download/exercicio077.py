#contando vogais
palavras = ('Hoje', 'amanhã', 'Gratis', 'chefe' 'ontem',
            'verei', 'veremos', 'teremos', 'amolecer',
            'arriscar', 'adoecer', 'felicidade', 'simplicidade',
            'carro', 'loja', 'rocha', 'rochedo')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end=' ')
    for letra in p:
        if letra.lower() in 'aáãâeéêiíoôóuú':
            print(letra, end=' ')