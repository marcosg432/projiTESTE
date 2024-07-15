print("1. soma de dois numeros")
print('2. diferenca entre dois numeros(maior pelo  menor)')
print('3. produto entre dois numeros')
print('4. divisao entre dois numeros(o denominador nao pode ser zero)')

opcao = int(input('digite: '))
if (opcao == 1):
    n1 = int(input('digite o numero: '))
    n2 = int(input('numero: '))
    soma = n1 + n2 
    print('a soma eh', soma )

if (opcao == 2):
    n1 = int(input('digite o numero: '))
    n2 = int(input('numero: '))
    soma = n1 - n2 
    print('a diferenca eh', soma )

if (opcao == 3):
    n1 = int(input('digite o numero: '))
    n2 = int(input('numero: '))
    soma = n1 * n2 
    print('o produto eh', soma )
    
if (opcao == 4):
    n1 = float(input('digite o numero: '))
    n2 = float(input('numero: '))
    soma = n1 / n2 
    print('a divisao eh', soma )

    
    


