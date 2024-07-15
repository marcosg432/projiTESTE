venda = float(input('valor de venda: '))

if(venda >= 100000):
    comissao = (venda * 16 / 100) + 700
    print(f' a comissao eh {comissao}')

elif(venda < 100000 and venda >= 80000):
    comissao = (venda * 16 / 100) + 650
    print(f'a comisa eh {comissao}')

if(venda < 80000 and venda >= 60000):
    comissao = (venda * 14 / 100) + 600 
    print(comissao)

elif(venda < 60000 and venda >= 40000):
    comissao = (venda * 14 / 100) + 550
    print(f'comissao da venda {comissao}')

if(venda < 40000 and venda >= 20000):
    comissao = (venda * 14 / 100) + 500
    print(f'a comissao eh {comissao}')

elif(venda >= 20000):
    comissao = (venda * 14 / 100)
    print(f'comissao eh {comissao}')