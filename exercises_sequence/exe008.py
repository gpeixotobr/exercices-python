medida = float(input('Distância em metros: '))
cm = medida * 100
mm = medida * 1000
dm = medida * 0.1
hm = medida * 0.01
km = medida * 0.001
print('A medida de {} metros corresponde a {:.0f} centímetros e {:.0f} milímetros.\nA medida em decâmetros é {}, hectômetros é {} e em kilômetros é {}.'.format(medida, cm, mm, dm, hm, km))

