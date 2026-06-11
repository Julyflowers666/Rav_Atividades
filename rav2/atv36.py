def segundo_maior(lista):
    maior = lista[0]
    segundo = lista[0]

    for num in lista:
        if num > maior:
            segundo = maior
            maior = num
        elif num > segundo and num != maior:
            segundo = num

    return segundo

print(segundo_maior([10, 20, 4, 45, 99, 99]))