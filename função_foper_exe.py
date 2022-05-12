# Exercício que utiliza uma função como parâmetro em outra função

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def imprime(a, b, foper): # foper recebe uma função como parâmetro dentro de outra função
    print(foper(a, b)) # comando: imprima uma função (foper) usando os parâmetros 'a' e 'b'

imprime(2, 3, soma)
imprime(5, 5, subtracao)

# fim do programa