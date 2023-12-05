# Crie um programa que solicite uma tabuada.
# Após digitar o número, mostre a tabuada completa na tela.

# "Exemplo: 

# Digite o número: 1

# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 1 x 4 = 4
# 1 x 5 = 5
# 1 x 6 = 6
# ...
# 1 x 10 = 10"

num = input("informe um número: ")

cont = 10
while cont >= 1:
    mult = int(num)*cont
    print("{} x {} = {}".format(num, cont, mult))
    cont = cont -1