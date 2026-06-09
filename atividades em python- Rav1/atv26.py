print ("----verificação----")
idade = int(input("Informe sua idade: "))
print("informe seu tipo de carteira: ")
print("1 - Carteira B")
print("2 - Carteira C")
op = int(input("Informe o tipo: "))
if op == 1:
    print("esta habilidado por pelo menos 2 anos?")
    res = input("[S/N]: ")
elif op == 2:
    print("esta habilidado por pelo menos 1 ano?")
    res = input("[S/N]: ")
    
print("obtem alguma infração nos ultimos 12 meses?")
res2 = input("[S/N]: ")
    
if (idade >= 21 and res == "S" and res2 == "N"):
    print("Esta apto")
    print("Esta apto")
else:
    print("Não esta apto")
