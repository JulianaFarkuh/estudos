
# se nao apertar ctrl+c, vai ficar dando olá pra sempre.
#while True:
#    print("Olá")

#Como fazer então?
while True:
    opcao = input("Digite 1 para continuar e 0 para sair\n")
    try:
        opcao = int(opcao)

        if opcao == 0:
            break
    
        if opcao == 3:
            continue

        print(f"Você digitou o numero {opcao} e vamos perguntar novamente")
    except:
        print("Aceito somente números")