#ex 4.2
class Funcionario: 
    def __init__(self,nome,sobrenome,horast,valorh):
        self.nome = nome 
        self.sobrenome = sobrenome 
        self.horast = horast
        self.valorh = valorh
        self.calcular = horast * valorh

    def nomecompleto(self):
        print(f'ola {self.nome} {self.sobrenome}')

    def calcularS(self):
       print(f'o valor de seu salario: {self.calcular}' )
    
    def icrementar(self,adc):
        self.horast += adc
        self.calcular = self.horast * self.valorh
        print(f'o seu novo saldo eh: {self.calcular}')

salario = Funcionario('Marcos', 'Toledo', 100,50)
salario.nomecompleto()
salario.calcularS()
salario.icrementar(20)




    
