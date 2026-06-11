print("insira a nota")

not1 = float(input("digite a 1º nota: "))
not2 = float(input("digite a 2º nota: "))
not3 = float(input("digite a 3º nota: "))
not4 = float(input("digite a 4º nota: "))

media = (not1 + not2 + not3 + not4) / 4

if media >7:
    print ("aprovado")
    print (media)
elif media >=6:
    print ("recuperação")
    print (media)
elif media <5:
    print ("reprovado")
    print (media)