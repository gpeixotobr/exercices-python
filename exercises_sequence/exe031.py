viagem = float(input('Quantos kilômetros tem a sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(viagem))
if viagem > 200:
    preço = viagem * 0.45
else:
   preço = viagem * 0.50
print('O custo da sua viagem será de R${:.2f}.'.format(preço))


