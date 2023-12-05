# EXERCÍCIO CONDICIONAL

'''Crie uma aplicação para calcular a média de um aluno
Você vai digitar o nome do aluno e 3 notas. 
No final do programa você vai mostrar se o aluno está aprovado, reprovado ou recuperação.

Critério:
média < 5 - reprovado
5 <= média <=6.9 - recuperação
média >= 7 - aprovado'''

teste = "134"
print ("teste: {0}".format(teste))

# forma de concatenar:
# print ("teste: {0} - {1}".format(teste, 123))

Nome = input("Digite o nome do aluno:\n")
Nota1 = float(input(f"Digite a nota 1 do {Nome}:\n")) # o f na frente do "Digite..." significa que é pra concatenar
Nota2 = float(input(f"Digite a nota 2 do {Nome}:\n"))
Nota3 = float(input(f"Digite a nota 3 do {Nome}:\n"))

Media = (Nota1+Nota2+Nota3) / 3

print (f"Media do aluno: {Media}")

if Media < 5:
    print(f"O aluno {Nome} está reprovado")
elif Media >= 5 and Media < 7:
    print(f"O aluno {Nome} está em recuperação")
else:
    print(f"O aluno {Nome} está aprovado")

