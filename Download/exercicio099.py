#Função que descobre o maior

from time import sleep
def maior(* núm):
    cont = maior = 0
    print('-=' * 25)
    print(('\nAnalisando os valores passados...'))
    for valor in núm:
            print(f'{valor}', end=' ', flush=True)
            sleep(0.3)
            if cont == 0:
                maior = valor
            else:
                if valor > maior:
                    maior = valor
            cont += 1
    print(f'Foram informdos {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


#Programa principal
maior(4, 5, 6, 9, 7)
maior(5, 3, 2)
maior(8)
maior()
