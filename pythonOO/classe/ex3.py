class Aluno:
    def __init__(self,nome,ra,n1,n2,n3,n4):
        self.nome = nome
        self.ra = ra
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.media = (n1+n2+n3+n4)/4
    def getNota(self):
        if (self.media >= 7):
            print('aprovado')

        elif (self.media >=5 and self.media < 6.9):
            print('esta de exame')

        else:
            print('aluno reproved')

n1 = float(input('nota 1: '))
n2 = float(input('nota2: '))
n3 = float(input('nota 3: '))
n4 = float(input('nota 4: '))     
avaliacao = Aluno('marcos',123456789,n1,n2,n3,n4)
avaliacao.getNota()


        



        
        


