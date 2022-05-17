# Programa que randomiza numeros entre 1 e 10 enquanto o usuário tenta adivinhar qual o número escolhido aleatoriamente.

import random

while True:
    n = random.randint(1, 10)
    x = int(input('Digite um número entre 1 e 10: '))
    if x == n:
        print('Parabéns! Você acertou.')
        break
    else:
        print('Você errou! Tente novamente.')

# fim do programa