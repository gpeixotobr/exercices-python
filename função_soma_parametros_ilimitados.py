# Exercicio que cria uma função soma sem limite de parâmetros

def soma(*parametros):
    s = 0
    for x in parametros:
        s += x
    return print(f'O valor da soma é igual a {s}')
    

soma(9, 10, 20, 55, 30, 45, 50)
soma(*list(range(1,100))) # utiliza um '*' para desempacotar os valores de uma lista com range de 1 a 99 (o 100 não é incluído) e aplica-los dentro da função soma

# fim do programa