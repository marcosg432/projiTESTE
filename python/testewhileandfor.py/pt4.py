numeros = [28,11,2,4,6,99,55,56,57,27,68,40]
cont = 0
while cont < len(numeros):
 print(f'valor do contador',cont, 'item da lista', numeros[cont])
if numeros [cont] == 55:
    print('achamos o numero 55')
    break
else:
  cont = cont + 1 
