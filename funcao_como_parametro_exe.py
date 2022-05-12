# Exercício que utiliza uma função como parâmetro em outra função sem o uso do foper

def imprime_lista(L, function_impressao, function_condicao):
    for item in L:
        if function_condicao(item):
            function_impressao(item)

def impressao(item):
    print(f'Valor: {item}')

# A partir daqui, vamos definir duas funções simples para serem passadas como parâmetro dentro da função imprime_lista

def par(x):
    if x % 2 == 0:
        return x

def impar(x):
    if x % 2 != 0:
        return x

L = [1, 7, 9, 2, 0, 15, 24, 50]

imprime_lista(L, impressao, par)
print('-' * 10)
imprime_lista(L, impressao, impar)

# fim do programa