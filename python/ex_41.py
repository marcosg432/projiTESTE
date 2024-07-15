a = 2
b = 4**2
c =1 
delta = b - 4 * a * c
print(f' delta igual a {delta}')
x1 = (-b + (delta **(1/2))) / 2*a
x1n = round(x1, 2)
print(f'o x1 é {x1n}')
x2 = (-b - (delta **(1/2))) / 2*a
x2n = round(x2, 2)
print(f'o x2 é {x2n}')
if(delta < 0):
    print('nao existe delta')
elif(delta == 0):
    print('raiz unica')
if(delta >- 0):
    print('duas raizes reais')