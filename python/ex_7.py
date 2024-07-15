produto = float(input("digite o valor do produto: "))
if(produto > 50.00):
    print("deve ser vendido por 45 por cento")
    valor = produto*0.45
    soma = produto - valor
    print("o valor de venda eh", soma)
else:
    print("deve ser vendido a 30 por cento")
    menor = produto*0.30
    soma = menor + produto
    print ("o valor de venda eh", soma)
    

