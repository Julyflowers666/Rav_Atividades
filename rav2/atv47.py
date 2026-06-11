def soma_acumulada(lista):
    resultado = []
    soma = 0

    for n in lista:
        soma += n
        resultado.append(soma)

    return resultado


print(soma_acumulada([1, 2, 3, 4]))