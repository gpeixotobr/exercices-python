# Função de Fibonacci que atua como uma função recursiva (que chama a si mesma)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# fim do programa