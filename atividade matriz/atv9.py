matriz = [[23, 54, 81],
        [12, 45, 67],
        [90, 12, 34]]

soma = 0
media = 0

for i in range(3):
        for j in range(3):
                soma += matriz[i][j]
                
media = soma / 9
print(f"A média dos elementos da matriz é: {media:.2f}")