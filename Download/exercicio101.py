# Funções para votação

def voto(ano):
    from datetime import  date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'


# Programa Principal
nascimento = int(input('Em que anos você nasceu? '))
print(voto(nascimento))