salário = float(input('Qual o valor do seu salário? R$'))
novo = salário + (salário*15/100)
print('O seu salário no valor de R${:.2f}, com 15% de aumento, passará a ser de R${:.2f}.'.format(salário, novo))
