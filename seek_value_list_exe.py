# Programa que pesquisa valores digitados pelo usuário dentro de uma lista

L = list(range(1, 100, 4)) # Uma lista foi gerada por um range de 1 a 100 pulando de 4 em 4 valores.
x = 0
seek = abs(int(input('Digite o valor que deseja buscar na lista: ')))
encontrado = False # A variável encontrado foi criada inicialmente com o valor False para facilitar a implementação da condição False no final do código.

while x < len(L):
    if L[x] == seek:
        encontrado = True # Caso encontre, a variável encontrado muda de valor para True.
        break
    x += 1
if encontrado == True:
    print(f'O número {seek} foi encontrado na posição {x + 1}.')
else:
    print(f'O número {seek} não foi encontrado.')

# fim do programa