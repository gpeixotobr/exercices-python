from random import randint
from time import sleep
computador = randint(0, 5) #faz uma randomização entre os números 0 e 5
print('-=-' * 15)
print('Vou pensar em um número de 0 a 5. Tente adivinhar.')
print('-=-' * 15)
sleep(2) #cria um delay de 2 segundos
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2) #cria um delay de 2 segundos
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))

