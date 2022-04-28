# Exercício com startswith, endswith, in e not in com strings

nome = 'Gustavo André Falcão Peixoto'

print(nome.startswith('Gustavo'))
print(nome.startswith('gustavo'))
print(nome.endswith('Peixoto'))
print(nome.endswith('André'))

print('Silva' not in nome)
print('peixoto' in nome.lower())
print('Falcão' not in nome)
print('FALCÃO' in nome.upper())

# fim do programa