##   OPERAÇÕES MATEMÁTICAS

x = 1
y = 6

r = x + y   # soma
r = x - y   # subtração
r = x / y   # divisão
r = x * y   # multiplicação
r = x % y   # módulo
r = x ** y  # potência
r = x // y  # arred para baixo

##   OPERAÇÕES DE COMPARAÇÃO

x = 1
y = 6

print (x == y)  # ==  igual
print (x != y)  # !=  diferente
print (x > y)   # >   maior
print (x < y)   # <   menor
print (x >= y)  # >=  maior igual
print (x <= y)  # <=  menor igual

##   OPERAÇÕES LÓGICAS

x = 6
y = 6
h = 9

c = 10

print (c >= 5 and c <= 20)
print (x == y)
print (h == x)
print (x == y and h == x)
print (x == y or h == x)
print ((x == y or h == x) and h > 10)

print (not True)
print (not x == y)

# if é igual ao "se". É o operador cndicional para que a gente consiga escolher um caminho.

if x == y:
    print ("x é igual a y")
else:
    print ("x é diferente de y")


 if x == h:
    print ("x é igual a h")
elif x == y:
    print ("x é igual a y")
else:
    print ("x é diferente de y")

# if = se
# else = caso contrário
# elif = se dentro do caso contrário
