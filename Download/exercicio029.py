#radar eletrônico
velocidade = float(input('\033[1;36mQual a sua velocidade Km/h? \033[m'))
if velocidade > 80:
    print('\033[1;31mMULTADO!, excedeu o limite permitido que é de 80Km/h.\033[m')
    multa = (velocidade - 80) * 7
    print('\033[1;31mO valor da multa é de R${:.2f}\033[m'.format(multa))
else:
    print('\033[1;32mTenha um bom dia! Dirija com segurança!\033[m')

