# Exercício de conversão de string em lista para alterar caracteres como elementos de uma lista e posteriormente converte-la em uma string novamente.

L = list("Hello, World!")
L[0] = 'h'
L[7] = 'w'
print(L)

S = ''.join(L)
print(S)

# fim do programa