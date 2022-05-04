# Programa que cria uma classe de Cachorros, define parâmetros e um método de impressão na tela.

class Cachorro():
    def __init__(self, name, race, weight, height):
        self.name = name
        self.race = race
        self.weight = weight
        self.height = height
        print('Objeto adicionado a classe "Cachorro" com sucesso!')
    def imprime(self, name, race, weight, height):
        print(f'Seu cachorro se chama {name}, é da raça {race}, tem {weight} quilos e mede {height} centímetros de altura.')

while True:
    animal_name = str(input('Qual o nome do seu cachorro? ')).strip().capitalize()
    animal_race = str(input('Qual a raça? ')).strip().capitalize()
    animal_weight = abs(float(input('Qual o peso em quilos? ').replace(',','.')))
    animal_height = abs(float(input('Qual a altura em centímetros? ').replace(',','.')))

    cachorro_input = Cachorro(animal_name, animal_race, animal_weight, animal_height)
    cachorro_input.imprime(animal_name, animal_race, animal_weight, animal_height)

# fim do programa