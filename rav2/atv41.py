def contar_caracteres(texto):
    cont = {}

    for caract in texto:
        if caract in cont:
            cont[caract] += 1
        else:
            cont[caract] = 1

    return cont

print(contar_caracteres("abacaxi"))