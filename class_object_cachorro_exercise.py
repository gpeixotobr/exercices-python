# Programa que cria uma classe de Cachorros, define parâmetros e um método de impressão na tela.

class Cachorro():
    def __init__(self, name, race, weight, height): # Função que define parametros de uma classe
        self.name = name
        self.race = race
        self.weight = weight
        self.height = height
        print('Objeto adicionado a classe "Cachorro" com sucesso!')
    def imprime(self):
        print(f'Seu cachorro se chama {self.name}, é da raça {self.race}, tem {self.weight} quilos e mede {self.height} centímetros de altura.')
    def __str__(self): # Função especial que rasteriza o objeto em string
        return f'Seu cachorro se chama {self.name}, é da raça {self.race}, tem {self.weight} quilos e mede {self.height} centímetros de altura.'
    def __repr__(self): # Função especial que rasteriza o objeto em string quando esta dentro de uma lista
        return self.__str__()

lista = []

while True:
    animal_name = str(input('Qual o nome do seu cachorro? ')).strip().capitalize()
    if animal_name == '0':
        break
    animal_race = str(input('Qual a raça? ')).strip().capitalize()
    animal_weight = abs(float(input('Qual o peso em quilos? ').replace(',','.')))
    animal_height = abs(float(input('Qual a altura em centímetros? ').replace(',','.')))

    cachorro_input = Cachorro(animal_name, animal_race, animal_weight, animal_height)
    cachorro_input.imprime()
    lista.append(cachorro_input)

print(lista)
# fim do programa