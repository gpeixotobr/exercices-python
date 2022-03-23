valor = float(input('Digite o valor da compra. R$'))
print('FORMAS DE PAGAMENTO')
print('''
    [1] à vista no dinheiro
    [2] à vista no cartão
    [3] 2x no cartão
    [4] 3x ou mais no cartão
    ''')
opcao = int(input('Qual a opção de pagamento? '))
if opcao == 1:
    total = valor - (valor * 10 / 100)
    print('O valor da sua compra de R${:.2f} com desconto será de R${:.2f}'.format(valor, total))
elif opcao == 2:
    total = valor - (valor * 5 / 100)
    print('O valor da sua compra de R${:.2f} com desconto será de R${:.2f}'.format(valor, total))
elif opcao == 3:
    total = valor
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${}'.format(parcela))
    print('O valor final da sua compra será de R${:.2f}'.format(total))
elif opcao == 4:
    total = valor + (valor * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {:.2f}x de R${:.2f} com juros'.format(totalparc,parcela))
    print(r'O valor da sua compra de R${:.2f} terá acréscimo de 20% de juros totalizando R${:.2f}'.format(valor, total))
else:
    print('OPÇÃO INVÁLIDA! Por favor, tente novamente.')
# fim do programa