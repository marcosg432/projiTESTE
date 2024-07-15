listaA = []
listaB = []
contador = 0
while contador < 5:
    contador += 1
    n = int(input('digite um numero: '))
    listaA.append(n)
    listaB.append(n*5)
print(listaA)
print(listaB)
########com o for
n = int(input('digite: '))
listaA = []
listaB = []
for n in range(1,*6):
    print(n)
