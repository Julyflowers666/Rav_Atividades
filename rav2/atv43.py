def transposta(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    resultado = []

    for j in range(colunas):
        nova_linha = []
        for i in range(linhas):
            nova_linha.append(matriz[i][j])
        resultado.append(nova_linha)

    return resultado

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

print(transposta(matriz))