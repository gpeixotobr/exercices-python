# Programa que busca uma chave e um valor em um dicionário dentro de outro dicionário.

d1 = {
    1 : {'Dept' : 'Matematica','Prof':'Dr Massao'},
    2 : {'Dept' : 'Física','Prof':'Dr Arimateia'},
    3 : {'Dept' : 'Engenharia Civil','Prof':'Dra Isis'},
    4 : {'Dept' : 'Ciencia da Computacao','Prof':'Dr Thiago'}
}

d2 = {
    5 : {'Dept' : 'Ciencia de Dados','Prof':'Dr Felipe'},
    6 : {'Dept' : 'Sistemas para internet','Prof':'Dra Juliana'},
    7 : {'Dept' : 'Engenharia Eletrica','Prof':'Dra Tatiana'},
    8 : {'Dept' : 'Engenharia de Petróleo','Prof':'Dr Marcos'}
}

d1.update(d2)
while True:
    key = int(input('Digite o número do índice buscado de 1 a 8: ').replace('-','+'))
    if not 1 <= key <= 8:
        print('VALOR INVÁLIDO! Digite um valor entre 1 e 8.')
    else:
        value = str(input('Digite "Dept" para departamento ou "Prof" para professor para acessar a informção: ' )).title().strip()
        print(d1[key][value])
    seguir = str(input('Deseja continuar? S/N: ')).upper().strip()
    if seguir == 'N':
        break

# fim do programa