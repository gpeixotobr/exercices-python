salário = float(input('Digite o valor do seu salário: R$'))
if salário > 1250.00:
    aumento = salário + (salário * 10 / 100)
else:
    aumento = salário + (salário * 15 / 100)
print('O seu salário no valor de R${:.2f} passa a ser de R${:.2f}.'.format(salário, aumento))
