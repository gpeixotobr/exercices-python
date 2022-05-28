# Programa que cria arquivos txt com numeros pares e impares a partir de um range e condições

with open('impares.txt', 'w') as impares:
    with open('pares.txt','w') as pares:
        for linha in range(0, 101):
            if linha % 2 == 0:
                pares.write(f'{linha}\n')
            else:
                impares.write(f'{linha}\n')

# fim do programa