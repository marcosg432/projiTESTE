numeros = [12,15,20,50,70,92,910,50,94]
frutas = ['pera','maça','uva','amora' ]

for item in frutas:
    print(item)
print(len(numeros))
print(numeros[0])
print(numeros[1])
print(frutas[2])
print(frutas[1]) 

print(numeros[3] + numeros[2])
print(sum(numeros))
print(max(numeros))
print(min(numeros))
print('media: ',sum(numeros) / len(numeros))


lista_ordenada = sorted(numeros)
lista_decrescente = sorted(numeros, reverse=True)
print(lista_ordenada)
print(lista_decrescente)

indice = numeros.index(20)
print(indice)

numeros.pop()
numeros.pop()
print(numeros)
print(len(numeros))

numeros.insert(0, '11 de setembro')
print(numeros)

numeros.append(1945)
numeros.append('torres gemeas')
print(numeros)
numeros.append([1,2,3,4,5])
print(numeros)
print(numeros[10])
 