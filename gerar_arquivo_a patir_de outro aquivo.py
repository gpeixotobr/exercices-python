# Programa que gera um arquivo 'pares.txt' a partir de outro arquivo pré-existente 'arquivo_linhas.txt' e pega apenas os valores pares de um e acrescenta no outro.

with open('pares.txt','w') as pares:
    with open('arquivo_linhas.txt','r') as numeros:
        for linhas in numeros.readlines():
            if int(linhas) % 2 == 0:
                pares.write(f'{linhas}')


# fim do programa