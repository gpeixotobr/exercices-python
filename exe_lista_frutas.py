# Programa que adiciona frutas a uma lista dentro de um loop while com outro loop for

from time import sleep
lista = ['Maçã', 'Banana', 'Uva', 'Pera', 'Abacaxi']
t = 1
contador = 5

while True:
    for i in range(0,len(lista)):
        print(lista[i])
        sleep(t)

    compra = str(input('Qual fruta você deseja adicionar a lista? Para sair digite "sair": ')).strip().title()

    if compra == 'Sair':
        break

    if compra in lista:
        print('Esta fruta já está na lista. Tente novamente!')
        sleep(t)

    else:
        lista.append(compra)
        print('Fruta adicionada à lista com sucesso!')
        contador += 1
        sleep(t)
        

print(f'Sua lista tem um total de {contador} frutas.')
sleep(t)
print(f'A sua lista de frutas final é: {lista}')
