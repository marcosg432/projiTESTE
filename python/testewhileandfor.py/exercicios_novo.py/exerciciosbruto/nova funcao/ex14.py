#potencia de energia eletrica, exercicio 14 da lista 
def calcula_valor(consumo,preco):
    valor = consumo * preco
    return valor

def consumo(potencia,horas,preco):
    consumo = potencia * horas / 1000
    conta = calcula_valor(consumo,preco)
    return conta
banho = consumo(4400,40,0.95)
print('R$: ', banho)