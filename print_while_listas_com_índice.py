# programa que adiciona valores a uma lista e depois escolhe quais valores imprimir com base no seu índice

numeros = [0, 0, 0, 0, 0]
x = 0

while x < 5:
    numeros[x] = int(input(f'Digite o número {(x + 1)} da lista: ')) # adicionou 1 ao índice da lista para não começar em zero
    x += 1 # variável que funciona como contador da condição, além de índice temporário da lista
while True:
    tamanho_lista = len(numeros)
    escolhido = int(input('Digite a posição que você quer imprimir ou digite 0 para sair: '))
    if escolhido == 0:
        break
    elif escolhido > 0 and escolhido < len(numeros) + 1: #a condição impede que quaquer número (mesmo negativo) menor que 0 e maior que a quantidade de itens na lista seja ignorado
        print(f'O valor que você escolheu foi: {numeros[escolhido - 1]}') # o índice da lista foi o (escolhido - 1) para compensar o adicional de 1 no input inicial
    else:  
        print('ERRO! \nEscolha uma opção válida de 1 a 5.')
    
# fim do programa