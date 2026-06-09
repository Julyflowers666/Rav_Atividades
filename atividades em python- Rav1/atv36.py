contador = 0

while contador < 5:
    num_bolinhas = int(input("quandas bolinhas de gude tem no pode de vidro?: "))

    if num_bolinhas == 82:
        print("Parabéns, você acertou!")
    elif num_bolinhas < 82:
        print("vc errou! tem mais bolinhas")
    elif num_bolinhas > 82:
        print("vc errou! tem menos bolinhas")
    contador = contador + 1

else:
    print("acabou suas chances!")
