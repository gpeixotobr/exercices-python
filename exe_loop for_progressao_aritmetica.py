# Programa que cria uma Progressão Aritmética com base em inputs do usuário

print('Vamos descobrir qual os 10 primeiros termos de uma progressão geométrica?')
primeiro = abs(int(input('Digite o primeiro termo da PA: ')))
razao = abs(int(input('Digite a razão da PA: ')))
decimo = primeiro + 10 * razao # fórmula para cacular o enésimo termo de uma PA, no caso o décimo.

for elemento in range(primeiro, decimo, razao):
    print(elemento, end=' ')
print('ACABOU!')

# fim do programa