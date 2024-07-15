numeros = [2,3,4,11,5,20,50,70,8]
i = 0
#parando/ecerrando loop, se 20 for encontrado
while i < len(numeros):
 print(f'numeros na posiçao {[i]}')
 if numeros[i] == 20:
    print('encontramos o numero 20')
    break
 else:
   i = i + 1