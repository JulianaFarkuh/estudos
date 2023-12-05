'''
3. Sistema de Bonificação de Funcionários:

"Elabore um programa que calcule a bonificação anual de um funcionário.
Peça o nome do funcionário, o salário e o tempo de serviço em anos na empresa.
A bonificação é dada da seguinte forma:

Menos de 1 ano de serviço: sem bonificação
De 1 a 3 anos de serviço: 10% do salário
De 4 a 6 anos de serviço: 15% do salário
De 7 a 10 anos de serviço: 20% do salário
Mais de 10 anos de serviço: 25% do salário

O programa deve mostrar o nome do funcionário e o valor da bonificação que ele receberá."

'''

Nome = input("Digite Nome:\n")
Salario = float(input("Digite o salário mensal: \n"))
Tempo_servico = int(input("Digite o tempo de empresa: \n"))

if Tempo_servico <= 1:
    Bonus = 0
elif Tempo_servico <= 3:
    Bonus = 0.10
elif Tempo_servico <= 6:
    Bonus = 0.15
elif Tempo_servico <= 10:
    Bonus = 0.20
else:
    Bonus = 0.25

print("Nome_funcionário:", Nome)
print("perc. bonus:", Bonus )
print("Valor da bonificação a ser recebida:", Salario * Bonus)