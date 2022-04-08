from xml.dom.expatbuilder import ElementInfo
# Código que retorna o valor máximo de uma lista utilizando for e if:

lista = list(range(1,101,5))
maximo = lista[0]

for element in lista:
    if element > maximo:
        maximo = element

print(maximo)

# fim do programa