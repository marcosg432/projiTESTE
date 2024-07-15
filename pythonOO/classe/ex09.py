class Carro:
    def __init__(self,modelo,cor,ano,valor,consumo,nivel = 0):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano 
        self.valor = valor 
        self.consumo = consumo 
        self.nivel = nivel

    def abastecer(self): 
        litros = int(input('digite quantos litros quer abastecer: '))
        self.nivel += litros
        andar = float(input('valor de km rodado: '))
        self.consumo += andar
        print(f'abastecidos {litros} litros. nivel atual: {self.nivel} litros')

    def andar(self):
        distancia = int(input('distancia percorrida: '))
        litros_necessarios = distancia / self.consumo
        if litros_necessarios <= self.nivel:
            self.nivel -= litros_necessarios
            print(f'percorridos {distancia} km. nivel atual: {self.nivel} litros.')

        else:
            print('combustive insuficiente')

    def verificar_nivel(self):
        print(f'nivel atual do tanque {self.nivel}')


    
    def calcular_imposto(self):
        imposto = (self.valor*2.5) / 100
        print(f'o imposto ser pago eh de R${imposto}')
        return imposto


automovel = Carro('ferrari','vermelho',1992,3900000,15)
automovel.abastecer()
automovel.andar()
automovel.verificar_nivel()
automovel.calcular_imposto
