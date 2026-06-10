nomes = []

while True:
    nome = input("Digite o nome do aluno ('0' para encerrar): ")

    if nome.lower() == "0":
        break

    nomes.append(nome)

arquivo = open('C:/Users/vboxuser/Documents/nomes_Alunos.txt', 'w', encoding='utf-8')

for nome in nomes:
    arquivo.write(nome + '\n')

arquivo.close()

print("Gravação realizada com sucesso!")