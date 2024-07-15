class Pessoa:
    def __init__(self,nome,idade,endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def bbzinho(self):
        print(f'ola {self.nome}')

    def bb(self,idade):
       self.idade = idade
       print(self.idade)

    def b(self):
        print(f'ola {self.endereco}')
sla = Pessoa('marcos',18,'ruatchurusbango')
sla.bbzinho()
sla.bb(16)
sla.b()



    

