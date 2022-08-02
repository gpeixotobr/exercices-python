# Definição de classe e métodos

class Televisão():
    def __init__(self, min, max):
        self.ligada = False
        self.canal = 2
        self.cmin = min
        self.cmax = max
    
    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
    
    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1

# Codigo para teste do funcionamento dos métodos

tv = Televisão(1, 120) # parâmetros min e max foram inseridos no método

for x in range (1, 120):
    tv.muda_canal_para_cima()
    print(tv.canal)

print('---' * 10)

for x in range (1,120):
    tv.muda_canal_para_baixo()
    print(tv.canal)

# fim do exercício