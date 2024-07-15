avaliacao = int(input('digite o numero de avaliaçoes: '))
i = 0
cont = 0
while cont < avaliacao:
    nota = float(input('insira a nota da avaliacao: '))
    i += nota
    cont += 1
media = i / avaliacao
print(media)
