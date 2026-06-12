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
        elif op == 3:
            consultar()
        elif op == 4:
            salvar_dados()
        elif op ==5:
            arquivo()
        elif op == 6:
            print ("saindo do sistema")
            exit

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
        #"certo"

def Lnotas ():
    try:
        nome = input("Nome do aluno: ")

        if nome in cadastros_alunos:

            for i in range(1):
                linha = []

                for j in range(4):
                    valor = float(input(f"Digite a nota do aluno {i+1}: "))
                    linha.append(valor)

                notas.append(linha)

            for i in range(len(notas)):
                soma = 0

                for j in range(1):
                    soma += notas[i][j]

                    media = soma / 4
                    print(f"Média: {media}")

        else:
            print("Aluno não encontrado!")

    except:
        print("Error")
        #+or-

def consultar ():
    nome = input("Nome do aluno: ")

    if len(cadastros_alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    if nome not in cadastros_alunos:
        print("Aluno não encontrado.")
        return

    aluno = cadastros_alunos[nome]
    media = Lnotas(aluno["notas"])

    print("\n----- DADOS DO ALUNO -----")
    print("Nome:", aluno["nome"])
    print("Idade:", aluno["idade"])
    print("Turma:", aluno["turma"])
    print("Notas:", aluno["notas"])
    print("Média:", media)

def situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

def salvar_dados():

    if len(cadastros_alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    soma_medias = 0

    for aluno in cadastros_alunos:

        media = Lnotas(aluno["notas"])
        soma_medias += media

        if media >= 7:
            print("aprovados") 
        elif media >= 5:
            print("recuperacao")
        else:
            print("reprovados")

        if media > maior_media:
            maior_media = media

        if media < menor_media:
            menor_media = media

def arquivo ():
    try:
        if len(cadastros_alunos) == 0:
            print("Nenhum aluno cadastrado.")
            menu()

        arquivo = open('C:/Users/vboxuser/Documents/cadastros_Alunos.txt', 'w', encoding='utf-8')

        for aluno in cadastros_alunos:
            linha = (
            aluno["nome"] + ";" +
            str(aluno["idade"]) + ";" +
            aluno["turma"] + ";"
            )

        for nota in aluno["notas"]:
            linha += str(nota) + ","

            linha = linha[:-1] + "\n"

            arquivo.close()

    except:
        print("Erro ao salvar chamado!!!")
        
    finally:
        print("Processo salvo com sucesso")

menu ()

#desisto, esse foi o meu limte