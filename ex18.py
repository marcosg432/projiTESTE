#escreva um algoritmo que leia certa quantidade de numeros e imprima o maior deles. Quantidade de numeros a serem lidos deve ser fornecida pelo usuario
qn = int(input('digite a quantidade de numeros: '))
lista = []
while qn > len(lista):
    lista.append(int(input('digite um  numero: ')))
print(lista)
print(f' o maior numero eh {max(lista)}')