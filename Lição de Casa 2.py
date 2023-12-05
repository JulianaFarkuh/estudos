'''
2. Verificador de elegibilidade para votação:

"Desenvolva um programa que determine se uma pessoa está apta a votar.
O usuário deve informar o nome e a idade. 
As regras para determinar a elegibilidade são:

Menos de 16 anos: não pode votar
De 16 a 17 anos: voto facultativo
De 18 a 70 anos: voto obrigatório
Mais de 70 anos: voto facultativo

O programa deve informar o nome da pessoa e se ela deve votar, não pode votar ou se o voto
é facultativo."

'''

Nome = input("Digite Nome:\n")
Idade = int(input("Digite a idade:\n"))

if Idade <= 16:
    Voto = "NÃO PODE VOTAR"
elif Idade <= 17:
     Voto = "VOTO FACULTATIVO"
elif Idade <= 70:
     Voto = "VOTO OBRIGATÓRIO"
else:
     Voto = "VOTO FACULTATIVO"

print("Nome:", Nome)
print("O voto é:", Voto)
