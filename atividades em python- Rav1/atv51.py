def soma(a, b):
    soma = a + b
    return soma

def subtracao(a, b):
    subtracao = a - b
    return subtracao

def multiplicacao(a, b):
    multiplicacao = a * b
    return multiplicacao

def divisao(a, b):
    divisao = a / b
    return divisao

def menu():
    try:
        contador = 0
        while contador < 4:
            a = float(input("Informe o 1º Numero: "))
            b = float(input("Informe o 2º Numero: "))
            contador += 1

        resultado1 = soma(a, b)
        resultado2 = subtracao(a, b)
        resultado3 = multiplicacao(a, b)
        resultado4 = divisao(a, b)

        print("Soma:", resultado1)
        print("Subtração:", resultado2)
        print("Multiplicação:", resultado3)
        print("Divisão:", resultado4)

        total = resultado1 + resultado2 + resultado3 + resultado4

        print("Soma dos retornos:", total)
        
    except:
        print("Dados incorretos!")
        
menu()