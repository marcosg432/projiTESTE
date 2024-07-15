#considerando o intervalo de 0 100. Crie um programa que calcule a soma dos primeiros 50 numeros pares
soma = 0
for item in range(0,101,2):
    soma += item  
print('o total é',soma)