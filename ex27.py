#escreva um algoritmo que leia um valor inicical A e imprima a sequencia de valores do calculo do fatorial  A! e o seu resultado .
i = int(input('digite um  numero: '))
a = 1
cont = 1
while cont <=  i:
    a *= cont
    cont+= 1
print(a)