# Analisando e gerando Dicionários

def notas(*n, sit=False):
    '''
    ->Função para analisar notas e situações de vários alunos.
    :param n:uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indica se deve ou não expor a  situação do aluno
    :return: dicionário com várias informções do aluno
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
           r['situação'] = 'Boa!'
        elif r['média'] >= 5:
            r['situação'] = 'Regular!'
        else:
            r['situação'] = 'Ruim!'
        return  r


# Programa Principal
resp = notas(6.5, 7.5, 9.5, 6.5, sit=True )
print(resp)
help(notas)