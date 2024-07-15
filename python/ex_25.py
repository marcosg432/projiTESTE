print("bem vindo a mini calculadora")
print("escolha a operacao que deseja realizar")
print('1. soma')
print('2. subtracao')
print('3. divisao')
print('4. multiplicacao')

opcao = int(input('digite o numero da operacao: '))
if (opcao == 1):
    n1 = float(input('digite o primeiro numero: '))
    n2 = float(input('digite o segundo numero: '))
    resultado = n1 + n2
    print("o resultado da soma eh", resultado)

elif(opcao == 2):
    n1 = float(input('digite o primeiro numero: '))
    n2 = float(input('digite o segundo numero: '))
    result = n1 - n2
    print('o resultado eh', result)

elif(opcao == 3):
    n1 = float(input('digite o primeiro numero: '))
    n2 = float(input('digite o segundo numero: '))
    res = n1 / n2
    print('o resultado eh', res)

elif(opcao == 4):
    n1 = float(input('digite o primeiro numero: '))
    n2 = float(input('digite o segundo numero: '))
    re = n1 * n2
    print('o resultado', re)
    
else:
    print('numero invalido')
