class Pessoa:
    def __init__(self,id=0,nome=''):
        self.id = id
        self.nome = nome

    def hello(self):
        print(f"ola {self.nome}")



print(pes1.id)

print('bomdia')
name = input('digite seu nome: ')
pes1.nome = name
pes1.hello()
pes1 = Pessoa()
pes1.id = 1