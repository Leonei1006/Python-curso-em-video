# dados para previdência
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Em que ano você nasceu? '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('Nº da Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 25)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')