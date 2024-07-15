nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
if(nota1 < 0.0 and nota2 > 10.0 or nota2 < 0.0 or nota2 > 10.0):
    print("uma ou ambas as notas sao validas. as notas devem estar entre 0 e 10")
    media =(nota1+nota2) / 2.0
    
    print(f"a nota eh{media}")