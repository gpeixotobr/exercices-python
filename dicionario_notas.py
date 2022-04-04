# Programa que cria um loop while com inputs para inserir uma chave e seu valor em um dicionário vazio.

d1 = {}

while True:
    key = str(input('Digite o nome do aluno: ')).title().strip()
    if key in d1: # condição para não entrar chaves repetidas no dicionário
        print('Este nome já está na lista. Por favor, digite outro.')
    else:
        value = float(input('Digite a nota do aluno: ').replace(',','.').replace('-','+')) # replaces de virgula e sinal negativo
        d1[key] = value
        print(d1)
    seguir = str(input('Deseja continuar? S/N: ')).upper().strip()
    if seguir == 'N':
        break