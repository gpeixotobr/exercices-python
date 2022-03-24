a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificando quem é maior
maior = b
if a > b and a > c:
    maior = a
if c > b and c > a:
    maior = c
print('O menor valor digitado é {}.'.format(menor))
print('O maior valor digitado é {}.'.format(maior))
