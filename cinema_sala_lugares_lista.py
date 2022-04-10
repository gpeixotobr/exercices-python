# Programa que escolhe a sala de um cinema e a quantidade de lugares desejadas para comprar com base em elementos de uma lista.

from time import sleep

t = 1
lugares_vagos = [10, 5, 8, 3, 2, 2, 0]

while True:
    sleep(t)
    print('Utilização das salas:')
    sleep(t)
    for x, l in enumerate(lugares_vagos):
        print(f'Sala {(x + 1)}: {l} lugares disponíveis.') # Enumeração das salas e respectivos lugares com base num loop for com enumerate.

    sala = int(input('Digite o número da sala que deseja efetuar a compra (Salas de 1 a 7) ou digite 0 para encerrar: '))
    
    if sala == 0:
        break
    if sala > len(lugares_vagos) or sala < 1:
        print('Sala inválida. Digite um número de sala válido.')
    elif lugares_vagos[sala - 1] == 0:
        print('A sala está lotada. Por favor, escolha outra sala.')
    else:
        lugares = int(input(f'Quantos lugares você deseja comprar? {lugares_vagos[sala - 1]} lugares disponíveis: ')) # Após passar por todas as condiçoes de sala, incrementamos as condições de lugares disponíveis para compra.
        
        if lugares > lugares_vagos[sala - 1]:
            print(f'Esta sala só possui {lugares_vagos[sala - 1]} lugares disponíveis.')
        elif lugares_vagos[sala - 1] == 0:
            print('Esta sala está esgotada. Não há mais lugares disponíveis.')
        elif lugares == 0 or lugares < 0:
            print('Número inválido.')
        else:
            print(f'Você comprou {lugares} lugares para a sala {sala}.')
            lugares_vagos[sala - 1] -= lugares

# fim do programa