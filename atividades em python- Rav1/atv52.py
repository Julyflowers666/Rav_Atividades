valor = float(input("Informe o valor da compra: "))
dias = ["1 - 3 dias úteis", "2 - 5 dias úteis", "3 - 7 dias úteis", "4 - 10 dias úteis"]

print("\nPrazo de entrega")

for dia in dias:
    print(dia)

opcao = int(input("Escolha uma opção: "))

def entrega3dias(valor):
    return valor + 25

def entrega5dias(valor):
    return valor + 20

def entrega7dias(valor):
    return valor + 15

def entrega10dias(valor):
    return valor + 10

if opcao == 1:
    total = entrega3dias(valor)

elif opcao == 2:
    total = entrega5dias(valor)

elif opcao == 3:
    total = entrega7dias(valor)

elif opcao == 4:
    total = entrega10dias(valor)

else:
    print("Opção inválida!")

print(f"Valor final: R$ {total:.2f}")