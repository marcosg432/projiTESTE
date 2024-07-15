#escreva um algoritmo que solicite ao usuario a entrada de 5 numeros, e que exiba o somatório desses 5 numeros na tela . Apos exibir a soma , 
#o programa deve mostrar todos os numeros que o usuario digitou, um por linha.

num = int(input('digite a quantidade de numeros: '))
lista = [ ]
while num > len(lista):
    lista.append(int(input('digite um  numero: ')))
print(lista)
print(sum(lista))