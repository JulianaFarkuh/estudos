## LISTA

# Usado para armazenar variáveis
# arrey é uma coleção de variáveis

# nome1 = input("Digite o nome do aluno 1\n")
# nome2 = input("Digite o nome do aluno 2\n")
# nome3 = input("Digite o nome do aluno 3\n")
# nome4 = input("Digite o nome do aluno 4\n")

nome1 = "Marco"
nome2 = "Roseli"
nome3 = "Mariana"
nome4 = "Marcelo"

alunos = [nome1, nome2, nome3, nome4]

print(len(alunos))
print(alunos[0])
print(alunos)

# construindo uma matriz para nomes e notas de alunos:

#nome1 = "Marco"
#notas_aluno1 = [6,7,8]

#nome2 = "Roseli"
#notas_aluno2 = [8,7,8]

#nome3 = "Mariana"
#notas_aluno3 = [3,7,10]

#nome4 = "Marcelo"
#notas_aluno4 = [8,8,9]

#matriz
#aluno1 = ["Marco",6,7,8]
#aluno2 = ["Roseli",8,7,8]
#aluno3 = ["Mariana",3,7,10]
#aluno4 = ["Marcelo",8,8,9]

#alunos = [aluno1,aluno2,aluno3,aluno4]

#print(f"Nome: {alunos[1][0]}")
#print(f"Nome 1: {alunos[3][2]}")

# existe uma forma muito mais simples de criar uma matriz, criando um dicionário, como sendo:

alunos = [
    { "nome":"Marco", "Notas": [6,7,8] },
    { "nome":"Roseli", "Notas": [8,7,8] },
    { "nome":"Mariana", "Notas": [3,7,10] },
    { "nome":"Marcelo", "Notas": [8,8,9] }
]
print(alunos)
print(alunos[1]["nome"])
print(alunos[1]["Notas"])
