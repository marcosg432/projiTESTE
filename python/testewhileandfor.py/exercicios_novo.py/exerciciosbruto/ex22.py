#escreva um programa que permita a qualquer aluno introduzir,pelo teclado, uma sequencia de notas(validas no intervalo de 0 a 10)
#e que mostre na tela, como resultado, a correspondente media aritmética. o numero de notas com  o aluno pretende efetuar um calculo
#nao fornecido ao programa,o qual terminara um programa introduzido um valor que nao seja valido como nota de aprovaaçao
notas = float(input('digite as notas: '))
cont = 0
soma= 0
while cont < notas:
    total = float(input('digite o total de notas: '))
    if total < 0 and total > 10:
        print('numero invalido')
        break
    else:
        print(total)
        soma += total
        cont += 1
        media = soma / notas
print('a media das notas eh: ', media)