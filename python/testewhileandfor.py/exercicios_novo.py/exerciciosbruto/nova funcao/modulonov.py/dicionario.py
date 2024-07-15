info = {
    'nome': 'marcos',
    'idade': '16',
    'cidade_natal': 'campo grande',
    'profissao': 'estudante',
}
print(info)
nome = info['nome']
idade = info['idade']
print(idade)
print(nome)

info['cidade_natal'] = 'xique-xique'
print(f'atualizado{info}')
info['email']= 'sla@gmail.com '
info['numero'] = '123456789'
print(info)
