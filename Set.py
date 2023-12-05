# SET é uma lista mutável e ordenada

numero = {1,2,4,4,4,6,6,8,9,4,3}

# ele imprime apenas os numeros unicos, ele não tras as repetições e ele ordena os numeros.
print(numero)

# vamos supor que vc pega os dados de uma base e ela vem assim com dados repetidos e desordenados
#além disso, ele vem em um arrey chamado de 'numero'.
# para utilizar o set, basta imprimir usando o 'set' no print.

numero = [1,2,4,4,4,6,6,8,9,4,3]
conjunto = set(numero)
lista_ordenada = sorted(conjunto)
print(lista_ordenada)

