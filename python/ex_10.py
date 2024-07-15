import math

n = float(input("digite um numero real: "))
if (n >= 0):
    raiz = math.sqrt(n)
    print(f"a raiz  quadrada de {n} eh {raiz}")
else: 
    n2q = n **2
    print(f"o quadrado de {n} eh {n2q}")