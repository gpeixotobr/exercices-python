# programa que lê as notas digitadas pelo usuário, insere as mesmas em uma lista e calcula a média entre elas.

notas = [0, 0, 0, 0, 0]
soma = 0
x = 0

while x <= 4:
    notas[x] = float(input(f'Digite o valor da nota {(x + 1)}.'))
    soma += notas[x]
    x += 1
x = 0

while x <= 4:
    print(f'Nota {x + 1} é: {notas[x]:.2f}')
    x += 1
print(f'A média das notas é {(soma / x):.2f}')

# fim do programa
