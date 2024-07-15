#escreva um algoritmo que leia um vetor com 10 posiçoes de numeros inteiros. em seguida receba um novo valor do usuario e verifique se este valor se encontra no vetor
num = int(input('digite a quantidade de numeros inteiros: '))
lista = [ ] 
while num > len(lista):
 lista.append(int(input('digite um  numero: ')))
print(lista)

num2 = int(input('digite um novo valor:  '))
if num2 == lista:
  print('numero ja inserido')