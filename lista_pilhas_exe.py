# Programa que utiliza filas como pilhas de pratos, adicionando e retirando do topo (Last in, First Out)

from time import sleep

prato = 5
pilha = list(range(1, prato + 1))
t = 1

while True:
    print(f'Existem {len(pilha)} pratos nesta pilha.')
    sleep(t)
    print(f'Pilha atual: {pilha}')
    sleep(t)
    print(f'Digite E para empilhar um novo prato na pilha.')
    print(f'Digite D para desempilhar um prato da pilha ou digite S para sair.')
    sleep(t)
    operacao = str(input('Qual a sua operação? Digite E, D ou S: ')).upper().strip()
    if operacao == 'D': 
        if len(pilha) > 0: # Se o comprimento da lista for maior do que zero, deve-se retirar um prato do topo/final da fila.
            pilha.pop(-1) # O comando para retirar usa a última posição (topo) da fila.
            print('Você retirou um prato do topo da pilha.')
            sleep(t)
        else: # Se o comprimento da lista for zero, significa que não há mais pratos para serem retirados.
            print('A pilha está vazia. Não há mais pratos disponíveis.')
            sleep(t)
    elif operacao == 'E': 
        prato += 1 # Para empilhar um novo prato na pilha, utiliza-se o contador prato para somar mais 1 elemento.
        pilha.append(prato) # Adiciona-se prato (recém somado com mais 1) na pilha para atualizar o valor da lista.
        print('Você adicionou mais um prato na pilha.')
        sleep(t)
    elif operacao == 'S': # Comando para sair do loop do while
        break
    else: # Se qualquer outra coisa que não seja E, D ou S for digitiada, deve-se ignorar e reiniciar o loop,
        print('COMANDO INVÁLIDO! Digite uma operação válida com E, D ou S.')
        sleep(t)