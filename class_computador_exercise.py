# Programa que cria uma classe chamada Computador, tendo a sua configuração como parâmetros dos objetos, adicionando-os em uma lista.

class Computador():
    def __init__(self, processador, memoria, ssd, fonte, placamae):
        self.processador = processador
        self.memoria = memoria
        self.ssd = ssd
        self.fonte = fonte
        self.placamae = placamae
    def __str__(self): # A função __str__ deve obrigatoriamente usar "return" para que a função __repr__ funcione sem problemas.
        return f'O seu computador é: {self.processador}, {self.memoria}gb, {self.ssd}tb, {self.fonte} watts e placa mãe {self.placamae}.'
    def __repr__(self): # A função __repr__ deve ter um return como self.__str__() para que seja possível imprimir o(s) objeto(s) da classe dentro de uma lista.
        return self.__str__()

lista = []

while True:
    processador_pessoal = str(input(f'Qual o seu processador? ')).strip().capitalize()
    memoria_pessoal = int(input(f'Quantos giga de memória? '))
    ssd_pessoal = int(input(f'Quantos tera de ssd? '))
    fonte_pessoal = int(input(f'Quantos watts de potência sua fonte possui? '))
    placamae_pessoal = str(input(f'Qual o modelo da sua placa mãe? ')).strip().upper()

    computador_pessoal = Computador(processador_pessoal, memoria_pessoal, ssd_pessoal, fonte_pessoal, placamae_pessoal)
    lista.append(computador_pessoal)

    continuar = str(input(f'Deseja continuar? S/N: ')).strip().upper()
    if continuar == 'N':
        break

for item in lista:
    print(item)

# fim do programa