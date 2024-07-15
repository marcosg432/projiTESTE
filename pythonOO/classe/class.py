class Estudante: 
    def __init__(self,matricula,idade,nome,nota): #sempre colocar na ordem
        self.matricula = matricula #atributo
        self.idade = idade #atributo
        self.nome = nome #atributo
        self.nota = nota #atributp

    def hello(self): #método
        print(f'ola {self.nome}') 

aluno = Estudante(1412, 16, 'Marcos', 10) #sempre colocar na ordem 
print(aluno.nome)
aluno.hello()
