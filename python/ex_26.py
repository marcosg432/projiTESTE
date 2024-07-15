
a = float(input('digite um valor: '))
b = float(input('digite valor: '))
c = float(input('digite valor: '))

if (a + b > c and a + c > b and b + c > a ):
    if(a == b == c):
       print("equilatero")
    elif(a==b or a==c or b == c ): 
         print('isosceles')
    else: 
        print('escaleno')
else:
        print('o valores fornecidos nao formam um triangulo')