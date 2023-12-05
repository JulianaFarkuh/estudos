'''
4. Sistema de Classificação de Hotéis:

"Desenvolva um programa que classifique um hotel baseado na avaliação dos hóspedes.
O usuário deve digitar o nome do hotel e três notas referentes aos critérios de conforto,
 limpeza e localização.
O programa deve calcular a média das notas e emitir uma classificação:

Média menor que 4: Hotel de 1 estrela
Média de 4 a 6: Hotel de 3 estrelas
Média de 6 a 8: Hotel de 4 estrelas
Média 9 ou superior: Hotel de 5 estrelas
No final, o programa deve exibir o nome do hotel e sua classificação em estrelas."
'''

Nome = input("Digite Nome do Hotel:\n")
Nota_1 = int(input("Digite Nota referente a conforto de 1 até 5, sendo 5 muito confortável:\n"))
Nota_2 = int(input("Digite Nota referente a limpeza de 1 até 5, sendo 5 muito confortável:\n"))
Nota_3 = int(input("Digite Nota referente a localização de 1 até 5, sendo 5 muito confortável:\n"))

Avaliacao = (Nota_1 + Nota_2 + Nota_3) / 3


if Avaliacao <= 4:
    Classificacao = "Hotel de 1 estrela"
elif Avaliacao <= 6:
    Classificacao = "Hotel de 3 estrelas"
elif Avaliacao <= 8:
    Classificacao = "Hotel de 4 estrelas"
else:
    Classificacao = "Hotel de 5 estrelas"

print("Nome Hotel:", Nome)
# print("Média de avaliação:",Avaliacao)
print("Classificação em estrelas do Hotel:", Classificacao)