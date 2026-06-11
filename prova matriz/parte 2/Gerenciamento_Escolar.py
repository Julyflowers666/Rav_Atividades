cadastros_alunos = {}
notas = []

def menu ():
    try:
        
        print ("----menu---")
        print ("1- Cadastrar alunos")
        print ("2- lançar notas")
        print ("3- consultar")
        print ("4- relatorio geral")
        print ("5- salvar dados")
        print ("6- sair\n")

        op = int(input("Escolha a opção desejada: "))

        if op == 1:
            cadastro()
        elif op == 2:
            Lnotas ()

    except ValueError:
        print("Erro! Digite apenas números. Tente novamente.")

def cadastro ():
    try:

        while True:

            nome = input("digite o nome do aluno: ")
            idade = int(input("digite a idade do aluno: "))
            turma = input("digite a turma desse aluno: ")
            cadastros_alunos[nome] = {"idade": idade,"turma": turma}

            op = input("Deseja cadastrar outro aluno? (s/n): ").lower()

            if op == "n":
                print(cadastros_alunos)
                print(f"Quantidade de alunos: {len(cadastros_alunos)}")
                break

    except ValueError:
        print("Valor inválido. Tente novamente.")
    finally:
        menu ()

def Lnotas ():
    try:
        if nome in cadastros_alunos:
            nome = input("Nome do aluno: ")

        else:
            print("Aluno não encontrado!")

            for i in range(1):
                linha = []

                for j in range(4):
                    valor = float(input(f"Digite a nota do aluno {i+1}: "))
                    linha.append(valor)

                notas.append(linha)

            for i in range(len(notas)):
                soma = 0

                for j in range(4):
                    soma += notas[i][j]

                    media = soma / 4
                    print(f"Média: {media}")

    except:
        print("kfas")

menu ()