#tradutor portugues para o ingles
tradutor = {
    'ola' : 'hello',
    'homem' : 'boy'
}    

resp = input('digite uma palavra: ')
if resp in tradutor:
    print(f'a traducao eh {tradutor[resp]}')
else:
    print('palavra nao conrrespondente')