while True:
    dia = int(input("digite o dia que deseja pagar o boleto: "))

    if dia == 2 or dia == 3 or dia == 5:
        print("dia disponivel, registrado!")
        break
    else:
        print(f"O dia {dia} n esta disponivel!")