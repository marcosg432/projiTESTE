#ex 12 
def media(lista):
    soma = 0
    for num in lista:
        soma += num
    total = sum(lista) / len(lista)
    return total

listaN = [5,8,3,1,9]
x = media(listaN)
print(x)