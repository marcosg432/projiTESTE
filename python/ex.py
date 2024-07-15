areap = float(input('area a ser pintada(em metros quadrados): '))
cobertura = areap * 1.1
latas = int(cobertura / 18)
if (cobertura % 18 != 0):
    latas += 1
galoes = int(cobertura/3.6)
if(cobertura % 3.6 != 0):
    galoes += 1
precolatas = latas * 80
precogaloes = galoes * 25
mistura = (precolatas * precogaloes) / 21.6
misturan = round(mistura, 2)
print(f' area a a ser pinta {areap}')
print(f'sao necessario {latas} latas ou {galoes} galoes de tinta')
print(f'preço ser pago latas {precolatas}')
print(f'preço ser pago galao {precogaloes}')
print(f'o preço a ser pago da mistura eh {misturan}')