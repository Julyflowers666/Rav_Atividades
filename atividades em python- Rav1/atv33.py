total_num = 0
contador = 0
maior = 0

while contador < 10:
    num = int(input("Digite um número: "))

    if num >50:
        maior = num

    total_num = total_num + num

    contador = contador + 1 

print("de 10 numeros lidos, o maior é:", maior)
print("O total é:", total_num)
