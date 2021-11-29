# Função para Fatorial

def fatorial(n, show=False):
    '''
     => Cálucula o Fatorial de um número.
    :param n:O número a ser cálculado
    :param show: Mostra o fatoramento do número
    :return: Retorna com o valor solicitado o Fatorial (n)
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
        if c > 1:
            print('! x ', end=' ')
        else:
            print('! = ', end=' ')
        f *= c
    return f


# Programa Principal
núm = int(input('Digite um número para ver o seu fatorial: '))
print(fatorial(núm, show=True))
print('=-=' * 20)
help(fatorial)