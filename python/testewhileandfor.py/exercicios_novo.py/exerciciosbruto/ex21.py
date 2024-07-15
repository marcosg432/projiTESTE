#crie um programa que calcule dois numero. calcule e mostre:
#a soma dos numeros pares desse intervalo de numeros, incluindo os numeros digitados;
#a multiplicaçao dos numeros impares desse intervalo, incluindo os digitados:
n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))
pares = 0
impares = 1
for num in range(n1, n2 +1 ):
    if num % 2 == 0:
     pares += num
    else:
        impares *= num

print('a soma dos pares sao',pares)
print('a multiplicaçao do impar é:',impares)


