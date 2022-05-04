# Programa que converte a temperatura de graus Celsius para Fahrenheit.

def fahrenheit(temp):
    return (temp * 1.8) + 32

temperatura = []

while True:
    graus = int(input('Digite um valor para temperatura em graus Celsius: '))
    temperatura.append(graus)
    continua = str(input('Deseja continuar? S/N: ')).upper()
    
    if continua == 'N':
        break
    else:
        continue

nova_temperatura = list(map(fahrenheit, temperatura))
print(f'Os valores convertidos para Fahrenheit são: {nova_temperatura}')

# fim do programa