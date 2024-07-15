#crie um programa que leia um numero determinado de idades de individuos(pare quando for informado idade 0), e calcule a idade media desse grupo
lista = []
idade = int(input("digite sua idade: "))

while idade != 0:
    lista.append(idade)
    idade = int(input('digite idade: '))
    if lista:
     media = sum(lista)/ len(lista)
     print('a media de idade eh', media)
     break
else:
   print('nenhuma idade informada')