class Aluno_academia: 
    def __init__(self,nome,idade,peso,altura,mensalidade = 120):
        self.nome = nome 
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade 

    
    def desconto(self):
        if self.idade < 18:
          desc = self.mensalidade - 30
          self.mensalidade = desc

    def calcular_IMC(self):
       return self.peso / (self.altura**2)
    


aluno.desconto()
print(f'a massa corporal do meu relikia eh de {aluno.calcular_IMC()}')
aluno = Aluno_academia('marcos',16,86,1.80,'mensalidade')