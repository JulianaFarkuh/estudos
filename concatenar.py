a = "Juliana"
b = "Farkuh"
c = "Scivittaro"

#formato 1
nome_completo = a +" "+ b +" "+ c
print(nome_completo)

#formato 2
nome_completo2 = "{} {} {}".format(a,b,c)
print(nome_completo2)

#formato 3
nome_completo3 = f"{a} {b} {c}"
print(nome_completo3)
print(nome_completo3[0:4])

#COMO USAR REPLACE -- É PARA SUBSTITUIR UMA VARIÁVEL POR OUTRA
nome_alterado = nome_completo3.replace("Farkuh","Fiochi")
print(nome_alterado)

# COMO USAR STRIP -- SERVE PARA ELIMINAR "ESPAÇOS" OU OUTRAS COISAS INDESEJADAS
nome_strip = "  Joana de Lima   "
nome_strip = nome_strip.strip()
# lstrip serve para tirar apenas da esquerda,
# rstrip serve para tirar apenas da direita e da esquerda,
# stip serve para tirar da esquerda e da direita,
print(nome_strip)

# strip é super importante para usarmos com input de senha, por exemplo.

