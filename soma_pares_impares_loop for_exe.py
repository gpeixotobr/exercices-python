# Programa que recebe 6 valores de input dentro de um loop for com range e soma os valores pares, os valores ímpares e a soma total.

from time import sleep

t = 1
pares = 0
impares = 0
total = 0
contador = 0
contador_par = 0
contador_impar = 0

for numero in range(1,7): # um input dentro de um loop com for e range repete a quantidade de vezes equivalente a quantidade de repetições do loop.
    num = int(input(f'Digite o {numero}º número: '))
    if num % 2 == 0: # condição para se o valro do input for par.
        pares += num
        print(f'O {numero}º valor é par.')
        contador_par += 1
    else: #senão for par, logo é impar.
        impares += num
        print(f'O {numero}º valor é impar.')
        contador_impar += 1
    total += num # soma total de todos os valores digitados
    contador += 1 # contador da quantidade de todas as repetições e inputs.

print(f'A soma de todos os {contador_par} números pares é {pares}.')
sleep(t)
print(f'A soma de todos os {contador_impar} números ímpares é {impares}.')
sleep(t)
print(f'A soma de todos os {contador} números digitados é {total}.')

# fim do programa