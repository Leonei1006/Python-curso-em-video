#esse algoritimo tem por objetivo ler o nome de uma pessoa e dizer se ele tem Silva no nome
nome = str(input('Qual o seu nome completo? ')).strip()
print('Seu nome tem silva? {}'.format('silva' in nome.lower()))