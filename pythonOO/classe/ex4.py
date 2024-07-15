class Conta: 
    def __init__(self,nome,cpf,numero,saldo):
        self.nome = nome 
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo 

    def depositar(self,valor):
        if(self.saldo > 0):
            self.saldo += valor
            print('saque efetuado')
            


    def sacar(self,valor):
        self.valor -= valor
        if (self.saldo < 0):
            print('saque nao autored')

            
    def imprimir(self):
          print(f'o seu saldo eh de: {self.saldo}')
          


saldo = float(input('digite o saldo: '))
while saldo < 0:
    saldo = float(input('saldo invalido, digite outro saldo: '))



dados = Conta('marcos',987654321,'123456',saldo)





