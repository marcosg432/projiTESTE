n1 = int(input("digite um numero: "))
n2 = int(input("digite um numero: "))
if(n1 > n2):
    mnumero = n1
    d = n1 - n2
elif(n2 > n1):
     mnumero = n2
     d = n2 - n1
     print(f"o maior numero eh {mnumero}")
     print(f"a diferenca eh {d} ")

else:
     print("os numeros sao iguais")
     
     