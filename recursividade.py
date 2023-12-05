# com essa função vc consegue fazer um looping tbm de uma lista.


def ler_lista(index,numero):
    if [index +1] >= len(numero):
        return
    print(f"Numero: {numero[index]}")
    ler_lista(index + 1 , numero)


numero = [6,7,3,4,7,10,8]

ler_lista(0, numero)

