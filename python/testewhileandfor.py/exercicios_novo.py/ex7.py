n = int(input('digite um numero: '))#declara até o infinito
cont = 1
while n > 0 :
    print(cont)
    cont += 2
    n -= 1
#fazer com for 
#puxa quantos numeros impares tem até os numeros digitados
n = int(input("digite um numero: "))
for impar in range(1,n,2):
    print(impar)
    