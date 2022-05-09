# Função que atua como validação dos dados inseridos nos parâmetros através de condições.

def faixa_valor(valor, min, max):
    if valor < min or valor > max:
        print(f'Valor inválido. Digite um valor entre {min} e {max}.')
    else:
        return valor

# fim do programa