'''
1. Calculadora de Imposto de Renda:

"Crie um programa que calcule o Imposto de Renda devido por um contribuinte.
O usuário deve inserir o nome do contribuinte e o salário mensal. 
O programa deve calcular o imposto com base nas seguintes faixas:

Até R$ 1.903,98: isento
De R$ 1.903,99 até R$ 2.826,65: 7.5%
De R$ 2.826,66 até R$ 3.751,05: 15%
De R$ 3.751,06 até R$ 4.664,68: 22.5%
Acima de R$ 4.664,68: 27.5%

Apresente o nome do contribuinte e o valor do imposto a pagar."

''' 

## PQ ASSIM NAO DA CERTO? TIRAR ESSA DÚVIDA COM O TUTOR.


# Nome = input("Digite Nome:\n")
# Salario = float(input("Digite o salário mensal: \n"))

# Faixa_1 = print (Salario <= 1903.98)  
# Faixa_2 = print (Salario >= 1903.99 and Salario <= 2826.65)  
# Faixa_3 = print (Salario >= 2826.66 and Salario <= 3751.05)
# Faixa_4 = print (Salario >= 3751.06 and Salario <= 4664.68)
# Faixa_5 = print (Salario > 4664.68)

# if Salario == Faixa_1:
#     imposto = 0
# elif Salario == Faixa_2:
#      imposto = 0.075
# elif Salario == Faixa_3:
#      imposto = 0.15
# elif Salario == Faixa_4:
#      imposto = 0.225
# else:
#     imposto = 0.275

# print("Nome:", Nome)
# print("perc. imposto:", imposto )
# print("Imposto devido:", Salario * imposto)



Nome = input("Digite Nome:\n")
Salario = float(input("Digite o salário mensal: \n"))

if Salario <= 1903.98:
    imposto = 0
elif Salario <= 2826.65:
     imposto = 0.075
elif Salario <= 3751.05:
     imposto = 0.15
elif Salario <= 4664.68:
     imposto = 0.225
else:
    imposto = 0.275

print("Nome:", Nome)
print("perc. imposto:", imposto )
print("Imposto devido:", Salario * imposto)
