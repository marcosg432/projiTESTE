class Livro:
    def __init__(self,nome,autor,editora,paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas 

    def get_livraria(self): #ger mostra na tela
        print(f'nome do livro {self.nome}')

    def get_escritor(self):
       print(f'ola {self.autor}')

    def set_edit(self,editora): #set altera
        self.editora = editora
        print(self.editora)

    def get_pag(self):
        print(f'nome do livro {self.paginas}')

biblioteca = livro('diario de um banana','Jeff Kinny','sla123',252)

biblioteca.livraria()
biblioteca.escritor()
biblioteca.edit('Diary of a Wimpy Kid')
biblioteca.pag()

    
    



