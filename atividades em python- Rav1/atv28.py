print("--calculo de média--")
n1 = float(input("Informe a nota do primeiro teste: "))
n2 = float(input("Informe a nota da prova: "))
qnt = int(input("Informe a quantidade de faltas: "))
media = (n1 + n2) / 2
if media >= 7.0 and qnt <= 10:
    print("Aprovado")
elif media >= 5.0 and media < 6.9 and qnt <= 10:
    print("Recuperação")
elif media < 5.0 and qnt >= 10:
    print("Reprovado")
