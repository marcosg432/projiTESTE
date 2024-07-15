#elabore um algoritmo para fazer calculo de potencializaçao.Ou seja, x^y. seu algoritmo devera solicitar que o usuario entre com o valor da base (x)
#e do expoente (y) e apresentar o resultado do calculo sem utilizar os operadores. para resolver o problema utilize estrututura de repetiçao
x = int(input('digite um  numero para (x): '))
y = int(input("digite um valor para y: "))
result = 1
cont = 0
while y > cont:
    result *= x
    cont += 1
print(f'base de {x}^{y} eh = {result}')
