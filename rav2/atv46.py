def mediana(lista):
    lista.sort()
    n = len(lista)

    meio = n // 2

    if n % 2 == 1:
        return lista[meio]
    else:
        return (lista[meio - 1] + lista[meio]) / 2


print(mediana([1, 2, 3, 4, 5]))  
print(mediana([1, 2, 3, 4]))     