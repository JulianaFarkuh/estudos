'''
4. Calculadora de Consumo de Combustível:
"Crie um aplicativo para calcular o consumo médio de combustível de um veículo.

O usuário deve inserir o nome do motorista, a quantidade de quilômetros percorridos e 
a quantidade de combustível gasto em litros. O programa deve calcular o consumo médio
 (quilômetros por litro) e classificar a eficiência do veículo conforme a tabela:

Menos de 8 km/l: Venda o carro!
Entre 8 e 12 km/l: Econômico
Mais de 12 km/l: Super econômico

Apresente o nome do motorista e a classificação de eficiência do veículo."
'''

Nome = input("Digite Nome:\n")
Qtde_km = float(input("Digite a quantidade de quilômetros percorridos: \n"))
Consumo_litro = float(input("Digite a quantidade de combustível gasto, em litros: \n"))

Eficiencia = Qtde_km / Consumo_litro

if Eficiencia <= 8:
    Classificacao = "Venda o Carro"
elif Eficiencia <= 12:
    Classificacao = "Econômico"
else:
    Classificacao = "Super econômico"

print("Nome Motorista:", Nome)
# print("Km/l do veículo:",Eficiencia)
print("Classificação de eficiência do veículo:", Classificacao)