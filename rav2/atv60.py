def cortar_lista(lista, posicao):
    nova_lista = []

    for i in range(len(lista)):
        if i > posicao:
            break
        nova_lista.append(lista[i])

    return nova_lista

print(cortar_lista([1, 2, 3, 4, 5], 2))
print(cortar_lista([10, 20, 30, 40], 1))