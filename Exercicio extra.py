'''
Geraldo tem uma venda de sapatos.
Ele anota os seus pedidos em um papel.
Precisamos criar para ele um programa para ajudar.
O que precisamos ter nesse programa?

- Capturar o nome do Cliente
- Marca do Sapato do Cliente
- Quantidade de sapatos no pedido do Cliente
- Valor a pagar

Se o cliente adquirir mais de 1 sapato, mostrar o valor total a pagar'''

Nome = input("Digite o nome do cliente:\n")
Marca = input("Digite a marca do sapato:\n")
Qtde = int(input("Digite qtde de itens do pedido:\n"))
Valor = float(input("Digite valor dos sapatos:\n"))

Valor_Compra = Qtde * Valor
print("o valor total a pagar é de: R$", Valor_Compra)