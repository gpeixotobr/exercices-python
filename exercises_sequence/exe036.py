casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você gostaria de pagar? '))
prestação = casa / (anos * 12)
print('Para pagar uma casa no valor de R${:.2f} no período de {} meses,'.format(casa, anos * 12), end='')
print(' a prestação será de R${}.'.format(prestação))
if prestação > salario * (30/100):
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo CONSEDIDO!')
