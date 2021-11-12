# analisando a média das notas
n1 = float(input("Digite a primeira nota: "))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2) / 2
print('\033[34mCom as notas {} e {} sua média é {:.1f}\033[m'.format(n1, n2, média))
if média >= 7:
    print('\033[1;32mPARABÉNS! VOCÊ ESTÁ APROVADO!\033[m')
elif 7 > média >= 5:
    print('\033[1;33mVocê está em RECUPERAÇÂO!\033[m')
else:
    print('\033[1;31mVocê foi REPROVADO!\033[m')
