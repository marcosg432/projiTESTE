def somaimposto(taxaimposto,custo):

    imposto = custo*(taxaimposto/100)
    total = custo + imposto
    return(total)

taxaimposto = 10
custo = float(input('digite o valor: '))
novocusto = somaimposto(taxaimposto,custo)
print(f'o valor atual eh {novocusto}')

    

