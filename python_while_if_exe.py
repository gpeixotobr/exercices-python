# programa tipo máquina registradora que soma o valor dos itens com base no seu código.

compra_1 = 0.50
compra_2 = 1.00 
compra_3 = 4.00 
compra_4 = 7.00 
compra_5 = 8.00 
compra_final = 0

while True:
    buy = int(input('Digite o código do seu produto ou 0 para sair: '))
    if buy == 1:
        compra_final += compra_1
    elif buy == 2:
        compra_final += compra_2
    elif buy == 3:
        compra_final += compra_3
    elif buy == 5:
        compra_final += compra_4
    elif buy == 9:
        compra_final += compra_5
    elif buy == 0:
        break
    else:
        print('Código inválido.')
print(f'O valor total da sua compra é de R${compra_final}.')

# fim do programa