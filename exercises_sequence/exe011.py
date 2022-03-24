largura = float(input('Qual a largura da sua parede? '))
altura = float(input('Qual a altura da sua parede? '))
area = largura * altura
print('Sua parede tem uma área de {}m²'.format(area))
tinta = area / 2
print('Para pintar sua parede será necessário {} litros de tinta. '.format(tinta))

