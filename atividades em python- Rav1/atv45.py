Senha = []

for linha in range (6):
    valor = input("digite a senha (em minusculo): ")
    if valor in["a", "e", "i", "o", "u"]:
        Senha.append(valor)
    else:
        print("digito invalido, tente novamente!")
        continue

nova_senha = []

for i in range (len(Senha)):
    if Senha [i] == "a":
        nova_senha.append("z")
    elif Senha [i] == "e":
        nova_senha.append("3")
    elif Senha [i] == "i":
        nova_senha.append("L")
    elif Senha [i] == "o":
        nova_senha.append("0")
    elif Senha [i] == "u":
        nova_senha.append("$")

print(f"senha: {Senha}")
print(f"senha criptografada: {nova_senha}")
