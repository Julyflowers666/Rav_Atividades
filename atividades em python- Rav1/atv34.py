contador = 0
maior = 0

while contador < 12:
    altura = float(input("Digite a altura do atleta: "))

    if altura >= 1.90:
        maior = maior + 1

    contador = contador + 1 

print("de 12 atletas,os que tem altura igual a 1.90m ou mais é:", maior)
