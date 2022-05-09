# Função que calcula o fatorial de um número n - e atua como uma função recursiva (que chama a si mesma)

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fat = n * fatorial(n - 1)
        return fat

# Fim do programa