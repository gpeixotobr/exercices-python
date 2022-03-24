velocidade = float(input('Qual a velocidade do seu carro? '))
if velocidade > 80:
    print('Você excedeu o limite de velocidade de 80Km/h.')
    multa = (velocidade-80) * 7
    print('O valor da sua multa é R${:.2f}.'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')
