#escreva um numero algoritmo que leia um numero inteiro entre 100 e 9999 e imprima na saida cada um dos algarismos que compoe o numero

numero = int(input('digite um numero entre 100 e 999: '))
while not ( 100 <=  numero <= 9999):
    print('numero invalido. digite outro numero')
    numero = int(input('digite um numero entre 100 e 9999: '))
milhar = numero / 1000
centena = (numero % 1000) // 100
dezena = (numero % 100) // 10
unidade = numero % 10
print('milhar: ', milhar )
print('centena: ',centena)
print('dezena:', dezena)
print("unidade: ", unidade ) 
