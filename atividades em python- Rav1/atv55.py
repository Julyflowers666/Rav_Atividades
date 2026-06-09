def reajustaGasolina(gasolina, reajuste):
    gasolina += reajuste
    return gasolina


def reajustaEtanol(gasolina, etanol, reajuste):
    etanol += reajuste
    gasolina += reajuste * 0.27
    return gasolina, etanol


gasolina = float(input("Valor atual da gasolina: "))
etanol = float(input("Valor atual do etanol: "))
reajuste = float(input("Valor do reajuste: "))
combustivel = input("Combustível do reajuste (G/E): ").upper()

if combustivel == "G":
    gasolina = reajustaGasolina(gasolina, reajuste)

elif combustivel == "E":
    gasolina, etanol = reajustaEtanol(gasolina, etanol, reajuste)

else:
    print("Combustível inválido!")

print(f"Valor final da gasolina: R$ {gasolina:.2f}")
print(f"Valor final do etanol: R$ {etanol:.2f}")