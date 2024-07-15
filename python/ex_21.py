n1 = float(input("digite n1: "))
n2 = float(input("nota 2: "))
n3 = float(input("nota 3: "))

media = (n1*2+n2*3+n3*5)/10
print('a media eh', media)
if(media >= 0 and media <= 2.9):
    print("reprovado")
elif(media >= 3 and media <= 5.9):
    print("recuperaçao")
else:
    print('aprovado')