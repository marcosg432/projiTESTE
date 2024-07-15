#um funcionario recebe aumento anual . em 2019 foi contratadopor 4000 reais. em 2020 recebeu um aumento de 1.5%. A partir de 2021, os aumentos sempre correspondem ao dobro
#do ano anterior . faça um programa que determine o salario anual do funcionario
salario = 4000
aumento = (1.5 / 100) * salario
salario+= aumento
print(f'o salario em 2020 {salario}')

cont = 2020
while cont < 2024:
    aumento = (aumento*2) 
    salario =salario + aumento
    cont += 1
    print('o salario em',cont, 'teve um aumento de', aumento,'o autal salario eh',round(salario))