class Triangulo:
    def __init__(self,ladoA,ladoB,ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB 
        self.ladoC = ladoC

    def calcular_perimetro(self):
        print(self.ladoA + self.ladoB + self.ladoC) 
    
    def getmaior_lado(self):
        if self.ladoA > self.ladoB and self.ladoA > self.ladoC:
            print(f'o maior lado eh {self.ladoA}')

        elif self.ladoB > self.ladoA and self.ladoB > self.ladoC:
            print(f'o maior lado eh {self.ladoB}')

        else:
           print(f'o maior lado eh {self.lado}')


ladoA = int(input('digite o valor do lado A: '))
ladoB = int(input('valor: '))
ladoC = int(input('valor C:' ))
calculo = Triangulo(ladoA,ladoB,ladoC)
calculo.calcular_perimetro()
calculo.getmaior_lado()

        