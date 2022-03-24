peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (metros) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif 18.5 <= imc < 30:
    print('Você está em SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE. Cuide-se melhor.')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA. Tome cuidado!')
