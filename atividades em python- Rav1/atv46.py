nomes = []

for linha in range (11):
    nome = input("digite o nome do jogador: ")
    for colunas in range(1):
        gols = int(input("digite a quantidade de gols: "))

    nomes.append([nome, gols])

print(f'nomes dos jogadores e quantidade de gols: {nomes}')