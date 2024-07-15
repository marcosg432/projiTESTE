#ler uma sequencia de numeros inteiros determina se eles sao pares ou nao. devera ser informado numero de dados lidos e valores pares. 
#o proceso termina quando for digitado o numero 0
nump = 0
totaln = 0
while True:
    numero = int(input('digite um numero: '))
    if numero == 0:
        break
    totaln += 1
    if numero % 2 == 0:
     nump += 1
print('foram lidos',totaln)
print('valores pares sao', nump)
    