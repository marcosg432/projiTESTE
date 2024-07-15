def numeros(*args):
    media = 0
    for i in args:
        media += i / len(args)
    return media
x = numeros(5.5,6,1.7,9)
print(x)