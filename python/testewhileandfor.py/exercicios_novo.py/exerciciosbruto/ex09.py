#escreva um programa que imprima 10 numeros, e leia o menor numero e o maior numero
qn = int(input('digite a quantidade de numeros: '))
lista = []
while qn > len(lista):
    lista.append(int(input('digite um  numero: ')))
print(lista)
print(f' o maior numero eh {max(lista)}, o menor numero eh {min(lista)}')