# Programa que inverte a sequência de itens de uma lista através do loop while utilizando um contador reverso (len(lista) - 1)

lista = [66, 78, 2, 45, 97, 17, 34, 105, 44, 52]
x = len(lista) - 1
nova_lista = []

while x >= 0:
    nova_lista.append(lista[x])
    x -= 1
print(nova_lista)

# fim do programa