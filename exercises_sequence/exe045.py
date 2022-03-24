import time
from random import randint
from time import sleep
itens = ('Pedra','Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
jogador = int(input('Qual é a sua jogada? '))
print('-'* 20)
t = 1
print('JO')
time.sleep(t)
print('KEN')
time.sleep(t)

print('PO!!!')
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-' * 20)
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('O jogador ganhou!')
    elif jogador == 2:
        print('O computador ganhou!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('O computador ganhou!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('O jogador ganhou!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: #computador jogou PEDRA
    if jogador == 0:
        print('O jogador ganhou!')
    elif jogador == 1:
        print('O computador ganhou!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')