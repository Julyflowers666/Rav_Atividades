matriz = []

for linha in range (3):
    nova = []
    for colunas in range(3):
        valor = float(input("digite valor: "))
        nova.append(valor)
    matriz.append(nova)

print(f"matriz: {matriz}")

soma = 0

for linha in matriz:
    for elemento in linha:
        soma += elemento

print (f"soma das matriz:{soma}")

diagonal = []

for i in range(3): 
    diagonal.append(matriz[i][i])
print(f"elementos diagonal: {diagonal}")

print ("test")