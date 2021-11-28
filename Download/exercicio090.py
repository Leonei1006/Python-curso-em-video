# guardando o nome e média dos alunos usando dicionário
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média do aluno {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)

#for k, v in aluno.items():
 #   print(f'{k} é igual a {v}')
 # temos várias formas de resolver o mesmo problema, aqui estão dua delas,
 #podemos usar o for ou fazer direto com o print formatado entre outras.

print(f'O aluno(a) {aluno["nome"]} teve média {aluno["média"]} e está {aluno["situação"]} ')


