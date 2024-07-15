def dados(**kwargs):
        nome=  'marcos'
        idade= 16
        email = 'sla@gmail.com'
        nacionalidade ='Brasil'
    
        return nome, idade, email, nacionalidade
x = dados()
print(x)

def dados (**dicionario):
        for i,  valor in dicionario.items():
            print(i,':',valor)
dados(nome ='marcos',idade = 16, nacionalidade = 'Brasil', email = 'sla@gmail.com')
        
