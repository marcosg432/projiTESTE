precoant = float(input('preço antigo: '))
if(precoant < 50):
    aumento = precoant * 0.05
    soma = precoant + aumento
    print(f'preço novo eh {soma}')
elif(precoant >= 50 and precoant <= 100):
    aumento = precoant * 0.10
    soma = precoant + aumento
    print(f'preco novo eh {soma}')
if(precoant > 100):
    aumento = precoant * 0.15
    soma = precoant + aumento
    print(f'o valor atual eh {soma}')