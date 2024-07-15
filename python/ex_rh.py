cargo = input("digite seu cargo: ")
nome = input('nome completo: ')
email = input('email: ')
idade = int(input('digite sua idade: '))
if(idade >= 18):
    print('passou para a proxima fase')
    curso = input('se ela possui curso de quaificaçao na area digite (sim) se nao, digite (nao): ')
    if(curso == 'sim'):
       print('passou para a proxima fase')
       nota = float(input('digite a nota da avaliaçao: '))  
       if(nota >= 7.0):
          print('passou para a etapa final')
       else:
            print('obrigado pela sua participaçao')
    else:
        ('obrigado pela participaçao')
else:
    print('obrigado pela participaçao')