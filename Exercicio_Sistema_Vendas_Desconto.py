# Sistema de Vendas e Descontos

# Objetivo: Desenvolver um programa que calcula o total de uma venda, aplicando descontos
# quando aplicável.

# Variáveis: Armazene preços dos produtos e o total da venda.
# Looping: Use um loop para adicionar cada produto à venda.
# Condicionais: Aplique descontos com base em certas condições (por exemplo, desconto para compras acima de um certo valor).
# Array: Use uma lista para armazenar os itens da venda.
# Dict: Use um dicionário para armazenar informações dos produtos, como preço e taxa de desconto.


produtos = [
    {'id':1,
     'nome':"Arroz Camil",
     'preco':7.58,
     'tam/qtd':'1k'
     },
     {'id':2,
      'nome':"Feijão São joão",
      'preco':10.24,
      'tam/qtd':'1k'
      }     
]

lista_venda = []
print("Produtos:",produtos)
print("\n ### 0 - para encerrar venda ### \n")
encerra = False
preco_total = 0

while encerra == False:
    p = input("Informe o código do produto: ")
    
    # Encerra compra
    if int(p) == 0:
        encerra = True
        desconto = None
        
    # Adiciona desconto
    if preco_total >= 100.00 and preco_total <= 200:
        desconto = preco_total - 20
        
        print("Valor total {}, Valor com desconto: {}".format(preco_total, desconto))
        print(lista_venda)
        
    # adiciona na lista de compra
    else:
        for prod in produtos:
            if prod['id'] == int(p):
                add = '{}, {}, {}'.format(prod['nome'],prod['tam/qtd'],prod['preco'])
                preco_total = preco_total + prod['preco']
                lista_venda.append(add)
                print("Soma: {}".format(preco_total))
