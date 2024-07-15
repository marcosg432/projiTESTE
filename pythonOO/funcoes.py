def soma(n1,n2):
    s = n1 + n2
    return s

def mult(n1,n2):
    s = n1 * n2
    return s

def div(n1,n2):
    s = n1 / n2
    return s

def subtracao(n1,n2):
    sub = n1 - n2 
    return sub

def potencia(n1,n2):
    total = n1**n2
    return total

x = soma(10,20) #chamada de funçao
y = mult(20,5)
z = potencia(4,2)
print(x,y,z)
print(x + y + z)
