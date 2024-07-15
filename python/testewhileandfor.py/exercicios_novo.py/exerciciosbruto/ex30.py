#faça um programa que some os numeros impares contidos em um intervalo definido pelo usuario. O usuario define o valor inicial dp intervalo e o valor
#final deste intervalo e o programa deve somar todos os numeros impares contidos neste intervalo.
soma_impares = 0

for num in range(1, 14):
    if num % 2 != 0:
        soma_impares += num
print(soma_impares)
    