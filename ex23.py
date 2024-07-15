#escreva um programa que leia numero inteiro e calcule a soma de todos os numeros divisores desse numero, com excessao dele próprio.
n = int(input('digite um numero: '))
soma= 0
for i in range(1,n):
    if n % i ==0:
        soma += i
print('a soma dos divisores de ',n, 'eh',soma)

