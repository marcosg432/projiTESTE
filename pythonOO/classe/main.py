from Estudante import Estudante
from Professor import Professor

matricula = input('MATRICULA: ')
idade = input('IDADE: ')
nome = input('NOME: ')
nota = input('NOTA: ')

aluno1 = Estudante(matricula, idade, nome, nota)
aluno1.hello()
