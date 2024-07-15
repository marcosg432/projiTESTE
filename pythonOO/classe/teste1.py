class Professor:
    def __init__(self,nome,idade,salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def hello(self):
        print(f'ola {self.nome} o melhor')

professor = Professor('thiago', 35, 10)
professor.hello()
