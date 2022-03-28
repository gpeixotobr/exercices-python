# o programa visa imprimir os número pares (múltiplos de dois) até o valor digitado pelo usuário.

fim = int(input('Digite o último número a imprimir: '))
x = 1
while x <= fim:
    if x % 2 == 0:
        print(x)
    x = x + 1

# fim do programa