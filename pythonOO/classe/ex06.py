class Circulo:
    def __init__(self,raio,pi):
        self.raio = raio
        self.pi = pi

    def imprimir_raio(self):
        print(f'o valor do raio eh {self.raio}')
    
    def calcular_area(self):
        return self.pi * (self.raio **2)
    
    def calcular_circun(self):
        return 2 * self.raio * self.pi

calculo = Circulo(6,3.14)
calculo.imprimir_raio()
print(f'a area do circulo eh de {calculo.calcular_area()}')
print(f'circunferencia: {calculo.calcular_circun()}')