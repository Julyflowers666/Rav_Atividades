def calcular_media (nota1, nota2):
    total = nota1 + nota2
    return total/2

def principal ():
    nota1 = int(input("digite a primeira nota: "))
    nota2 = int(input("digite a segunda nota: "))
    
    media = calcular_media(nota1, nota2)

    print (f"media do aluno: {media}")

principal ()