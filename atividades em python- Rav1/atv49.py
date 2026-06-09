
def vogal(letra):
    vogal = ["a", "e", "i", "o", "u"]
    if letra in vogal:
        print("é uma vogal")
    else:
        print("é uma consoante")

while True:
    letra = input("Informe uma letra: ")
    vogal(letra)
    opcao = input("Deseja continuar? (s/n): ")
    if opcao.lower() == "n":
        break
