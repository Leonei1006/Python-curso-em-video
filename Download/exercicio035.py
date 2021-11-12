# formando um triângulo
print("\033[32m-=\033[m" * 30)
print('\033[1;33mAnalisador de triângulos\033[m')
print('\033[32m-=\033[m'* 30)
r1 = float(input('\033[1;33mPrimeiro segmento:\033[m '))
r2 = float(input('\033[1;33mSegundo segmento: \033[m'))
r3 = float(input('\033[1;33mTerceiro segmento:\033[m '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[1;32mPodemos  formar um TRIÂNGULO.\033[m')
else:
    print('\033[1;31mNão podemos formar um TRIÂNGULO.\033[m')

