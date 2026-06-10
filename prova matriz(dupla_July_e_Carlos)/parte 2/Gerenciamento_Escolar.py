cadastros_alunos = []
total_cont = []

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

        while True:
            print(f"insira a nota do aluno(a): ")
            not1 = float(input("digite a 1º nota: "))
            not2 = float(input("digite a 2º nota: "))
            not3 = float(input("digite a 3º nota: "))
            not4 = float(input("digite a 4º nota: "))

    except:
        print("kfas")

menu ()