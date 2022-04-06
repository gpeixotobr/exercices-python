# Programa que recebe uma lista com 10 pessoas que serão atendidas. Pode-se inserir mais pessoas no meio do processo ou simplesmente sair (encerrar).

ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    print(f'Existem {len(fila)} pessoas na fila.')
    print(f'Fila atual: {fila}')
    print(f'Digite F para adicionar um cliente a fila.')
    print(f'ou digite A para realizar o atendimento. Digite S para sair.')
    operacao = str(input('Digite a sua operação (F, A ou S): ')).upper().strip()
    if operacao == 'A':
        if len(fila) > 0: # Se o comprimento da fila for maior do que zero significa que ainda existe no minimo 1 pessoa na fila
            fila.pop(0)
            print('Você realizou o atendimento de uma pessoa.')
        else:
            print('Não há mais pessoas na fila.') # Se o comprimento da fila não for maior do que zero significa que não existe mais pessoas na fila.
    elif operacao == 'F':
        ultimo += 1 # a ultima pessoa da lista recebe + 1 para adicionar mais pessoas à fila.
        fila.append(ultimo) # adicionamos esse +1 da variável último no final da fila.
        print('Você adicionou mais uma pessoa à fila.')
    elif operacao == 'S':
        break # parar o loop do while
    else: # se qualquer outra coisa que não seja F, A, ou S for digitada, o comando será inválido.
        print('Comando inválido. Digite F, A ou S.')
    
    # fim do programa