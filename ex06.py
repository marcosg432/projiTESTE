#escreva um programa que peça para om usuario digitar 10 valores e some-o
soma = 0
c = 0
while c <= 10:
    num = float(input('digite um valor: '))
    soma += num
    c +=1
    print(soma)

