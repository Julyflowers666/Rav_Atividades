estacionamento = []

for i in range(2):
    linha = []
    for j in range(9):
        linha.append("Livre")
    estacionamento.append(linha)

while True:

    print("\n===== MENU =====")
    print("1 - Exibir vagas")
    print("2 - Estacionar veículo")
    print("3 - Retirar veículo")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        print("\nLADO A")
        print(estacionamento[0])

        print("\nLADO B")
        print(estacionamento[1])

    elif opcao == "2":

        placa = input("Digite a placa: ")

        contador = 0

        for i in range(2):
            for j in range(9):

                if estacionamento[i][j] == "Livre":

                    estacionamento[i][j] = placa

                    print(f"Veículo estacionado na vaga [{i}][{j}]")

                    contador = 1 #contador para verificar quantidade de vagas ocupadas
                    break

            if contador == 1: 
                break
        #tratamento de erro
        if contador == 0:
            print("Estacionamento lotado!")

    elif opcao == "3":

        placa = input("Digite a placa do veículo: ")

        contador = 0

        for i in range(2):
            for j in range(9):

                if estacionamento[i][j] == placa:

                    print(f"Veículo encontrado na vaga [{i}][{j}]")

                    estacionamento[i][j] = "Livre"

                    print("Vaga liberada!")

                    contador = 1
                    break

            if contador == 1: #para o if
                break

        if contador == 0: #tratamento de erro
            print("Veículo não encontrado!")

    elif opcao == "4":
        break

    else:
        print("Opção inválida!")
