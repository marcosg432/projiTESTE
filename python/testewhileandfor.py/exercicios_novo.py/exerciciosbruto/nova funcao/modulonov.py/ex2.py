amigos = {
    'amigo_1' : 'leandro',
    'amigo_2': 'arthur',
    'amigo_3': 'maycon',
    'amigo_4': 'matheus',
    'amigo_5':'rafael'
}
for amg in amigos.keys():
    print(f'{amg} : {amigos}')
nome = input('digite um nome: ')
if nome == amigos:
    print('este nome esta na lista')
else:
    print('este nome nao esta na lista')
