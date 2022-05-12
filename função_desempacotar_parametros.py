# Exercício que utiliza uma função com o parâmetro 'numeros' ilimitado para passa-lo dentro de um loop for e armazena-lo dentro de uma variável 'valor_maior'

def imprime_valor_maior(mensagem, *numeros):
    valor_maior = None
    for item in numeros:
        if valor_maior is None or valor_maior < item:
            valor_maior = item
    print(mensagem, valor_maior)

imprime_valor_maior('Maior valor encontrado:', 5, 4, 3, 7, 9, 0) # utiliza a mensagem e os valores inteiros dentro da função
print('-' * 15)
imprime_valor_maior('O maior valor desta lista é:', *[15, 20, 7, 5, 4, 8, 90, 0, 55, 100]) # utiliza o asterisco na lista para desempacotar a lista e utilizar os valores denrto dela na função

# fim do programa