from datetime import date
nasc = int(input('Qual o seu ano de nascimento? '))
atual = date.today().year
idade = atual - nasc
print('O atleta que nasceu no ano {} tem {} anos.'.format(nasc, idade))
if idade <= 9:
    print('Pertence a categoria MIRIM.')
elif 14 >= idade > 9:
    print('Pertence a categoria INFANTIL.')
elif 19 >= idade > 14:
    print('Pertence a categoria JUNIOR.')
elif 25 >= idade > 19:
    print('Pertence a categoria SÊNIOR.')
elif idade > 25:
    print('Pertence a categoria MASTER.')
