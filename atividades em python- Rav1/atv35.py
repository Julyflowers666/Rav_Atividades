contador = 0
notas1 = 0
notas2 = 0
notas3 = 0
maior = 0
media = 0
menor = 0

while contador < 25:
    notas = float(input("Digite a nota dos alunos: "))

    if notas >= 8:
        notas1 = notas1 + 1
        maior = notas

    elif notas >= 6:
        notas2 = notas2 + 1
        media = notas

    elif notas < 6:
        notas3 = notas3 + 1
        menor = notas

    contador = contador + 1 

print("de 25 alunos,os que tem notas maiores é:", notas1)
print("maior nota é:", maior)
print("de 25 alunos,os que tem notas medias é:", notas2)
print("media é:", media)
print("de 25 alunos,os que tem notas menores é:", notas3)
print("menor nota é:", menor)
