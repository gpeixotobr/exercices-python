from math import radians, sin, cos, tan
ângulo = float(input('Digite um ângulo que você deseja: '))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f} e o COSSENO de {:.2f}'.format(ângulo, seno, cosseno))
print('O valor da TANGENTE é de {:.2f}'.format(tangente))



