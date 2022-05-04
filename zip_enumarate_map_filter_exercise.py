# Programa que utiliza as funções zip, enumarate, map e filter em duas listas com funções específicas.

lista = [1, 2, 3, 4, 5]
lista_dois = [5, 6, 7, 8, 9, 10]

lista_index = list(enumerate(lista)) # retorna uma lista de tuplas com o índice e o item da lista
print(lista_index)

lista_zip = list(zip(lista, lista_dois)) # retorna uma lista de tuplas com os itens das duas listas até o limite de itens da lista menor.
print(lista_zip)

def função_par(valor):
    if valor % 2 == 0:
        return valor

lista_filtrada = list(filter(função_par, lista_dois)) # retorna apenas os valores que forem True para a função.
print(lista_filtrada)

def função_soma(a, b):
    return a + b

lista_mapeada = list(map(função_soma, lista, lista_dois)) # retorna os elementos de uma ou mais listas após ter aplicado a função em todos os elementos.
print(lista_mapeada)

#fim do programa