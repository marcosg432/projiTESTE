notas = {



}
n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a primeira segunda nota: "))
n3 = float(input("digite a primeira terceira nota: "))
n4 = float(input('digite a quarta nota: '))
for i in range(1,10):
   notas = (n1 + n2 + n3 + n4) / 4
print(f'a media eh {notas}')