valorp = float(input("valor a ser pago: "))
desconto = valorp * 0.1
valor = valorp - desconto
parcela = valor / 3
avista = valor * 0.05
parcelado = valorp * 0.05
print(f"o total a pagar com 10% de desconto: {valor}")
print(f"o valor de cada parcela: {parcela}")
print(f"a comissao do vendedor, caso a venda seja a vista: {avista}")
print(f"a comissao do vendedeor, caso a venda seja parcelada: {parcelado}")