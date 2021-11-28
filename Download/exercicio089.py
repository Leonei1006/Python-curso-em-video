#boletim de notas com histórico dos alunos
ficha = list()
while True:
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    média = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], média])
    resp = str(input('Quer continuar? [S|N] '))
    if resp in 'Nn':
        break
print('-=' * 25)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-=' * 25)
for i,a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-=' * 25)
    opc = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'As notas de {ficha[opc][0]} são {ficha[opc][1]}')
