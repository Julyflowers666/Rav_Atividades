def string_mais_longa(lista):
    mais_longa = lista[0]

    for palavra in lista:
        if len(palavra) > len(mais_longa):
            mais_longa = palavra

    return mais_longa

print(string_mais_longa(["casa", "carro", "avião"]))