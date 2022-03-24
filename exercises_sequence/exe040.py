nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print('Com as notas {:.1f} e {:.1f} você obteve média {:.1f}.'.format(nota1, nota2, média))
if média >= 7:
    print('Sua média foi maior do que 7.0. Parabéns, você está APROVADO.')
elif 7 > média >= 5:
    print('Sua média foi abaixo de 7.0. Você está em RECUPERAÇÃO.')
elif média < 5:
    print('Sua média foi muito baixa. Estude mais! Você está REPROVADO.')
