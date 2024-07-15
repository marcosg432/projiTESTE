#escreva um programa que calcule e escreva o valor de S  
# S = 1/1 + 3/2 + 5/3 + 7/4 ... 99/50
soma = 0
s = 1
denominador = 0
for i in range(1,99+1,2):
    s += 2 * i - 1
    denominador += 1
    resultado = s / denominador 
    soma += resultado
    result= round(resultado,2)
    print(f' para i = {i}/{denominador}, o valor de S eh {result}')