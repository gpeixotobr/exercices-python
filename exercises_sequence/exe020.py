from random import shuffle
n1 = str(input('Digite o nome do primeiro aluno(a): '))
n2 = str(input('Digite o nome do segundo aluno(a): '))
n3 = str(input('Digite o nome do terceiro aluno(a): '))
n4 = str(input('Digite o nome do quarto aluno(a): '))
list = [n1, n2, n3, n4]
shuffle(list)
print(
    'A sequência de apresentação dos alunos será:'
)
print(list)

