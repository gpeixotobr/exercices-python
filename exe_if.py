# o programa calcula o valor do imposto de renda com base na renda do usuário, sendo 20% para rendas entre R$1000 e R$3000 e 35% para rendas acima de R$3000.

salario = float(input('Digite o salario para calculo do imposto: '))
base = salario
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
print(f'Salário: R${salario:.2f} Imposto: R${imposto:.2f}')

# fim do programa