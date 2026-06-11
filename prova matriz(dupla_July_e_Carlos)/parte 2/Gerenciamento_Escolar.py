cadastros_alunos = []
total_cont = []
notas = []

def total_alunos():
    for i in total_alunos:
        soma = soma + i
        print (soma)

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

        elif op == 4:

        elif op == 5:
            salvar_arquivo ()
        else:
            print("saindo ...")
            break

    except ValueError:
        print("Erro! Digite apenas números. Tente novamente.")

def cadastro ():
    try:
        cont = 0
        while True:

            nome = input("digite o nome do aluno: ")
            idade = int(input("digite a idade do aluno: "))
            turma = input("digite a turma: ")
            op = input("Deseja cadastrar outro aluno? (s/n): ").lower()

            aluno ={"nome": nome,"idade": idade,"turma": turma,"notas": [0, 0, 0, 0]}
            cadastros_alunos.append(aluno)
            cont = cont + 1

            if op == "n":
                    print ("cadastro realizado!")
                    print(f"quantidades de alunos cadastrados: {cont}")
                    total_cont.append(cont)
                    break

    except ValueError:
        print("Valor inválido. Tente novamente.")
    finally:
        menu ()

def Lnotas ():
    try:
        nome = input("Nome do aluno: ")
        for aluno in cadastros_alunos:
            if aluno["nome"].lower() == nome.lower():

                not1 = float(input("digite a 1º nota: "))
                not2 = float(input("digite a 2º nota: "))
                not3 = float(input("digite a 3º nota: "))
                not4 = float(input("digite a 4º nota: "))

            media = (not1 + not2 + not3 + not4) / 4
            notas.append(media)

            aluno["notas"] = notas

            print("Notas registradas!")
            return

    except:
        print("Aluno não encontrado!")

def salvar_arquivo():
    try:
        arquivo_chamado = open('C:/Users/vboxuser/Documents/cadastro_chamado.txt', 'w', encoding='utf-8')
        
        for aluno in cadastros_alunos:

            linha = (
                f"{aluno['nome']};"
                f"{aluno['idade']};"
                f"{aluno['turma']};"
                f"{','.join(map(str, aluno['notas']))}\n")

        arquivo_chamado.write(linha)

        arquivo_chamado.close()
        
    except:
        print("Erro ao salvar chamado!!!")
        
    finally:
        print("Processo salvo com sucesso")

menu ()