diaria = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos kilômetros foram rodados com o carro? '))
valor = 60 * diaria
gas = 0.15 * km
print('O valor pago será R${:.2f}.'.format(valor + gas))


