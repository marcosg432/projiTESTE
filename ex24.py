#crie um programa que some todos os numeros abaixo de 1000 que sao multiplos de 3 ou 5
soma= 0
for i in range(1,1000):
    if i% 3 ==0 or i % 5 == 0:
        soma += i
print('a soma dos divisores dos numeros multiplos de 5 e 3 sao',soma)