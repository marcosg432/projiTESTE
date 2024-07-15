##ex 08
estoque = {
    'comida':'5',
    'bebida' : '3',
    'limpezas': '8'
}

compra = input('digite o produto a comprar: ')
if  compra in estoque:     
    print(f'produto {estoque[compra]}')    
else:
    print('produto fora de estoque')



