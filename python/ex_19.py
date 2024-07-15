h = float(input("digite sua altura: "))
sexo = input("digite seu sexo (M para  masculino, F para feminino): ")
if sexo.upper() == "M":
    pesom = (72.7 * h )-58
    print("seu peso eh", pesom)
elif sexo.uppr() == "F":
    pesof = (62.1 * h)-44,7
    print("seu peso eh", pesof)



