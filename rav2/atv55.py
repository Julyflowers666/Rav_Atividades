def menor_numero(lista):
    menor = lista[0]

    for numero in lista:
        if numero < menor:
            menor = numero

    return menor

print(menor_numero([3, 5, 7, 2, 8]))
print(menor_numero([10, 20, 30]))