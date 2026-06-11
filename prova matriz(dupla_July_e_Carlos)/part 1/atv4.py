soma = 0
cont = -1

while True:
    num = int(input("digite um numero: "))
    soma = soma + num
    cont = cont + 1

    if num == 0:
        break

print (f"total de numeros somados: {cont}")
print (f"total da soma dos numeros é: {soma}")