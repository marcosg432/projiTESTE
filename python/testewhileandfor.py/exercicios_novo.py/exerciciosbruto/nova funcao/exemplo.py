# *args para adicionar valores na tupla 
#**kwargs cria valores e salva e um dicionario
def soma (*args):
    soma = 0
    for i in args:
        soma += i
    return soma 
x = soma(1,2,3,4,5)
print(x)
