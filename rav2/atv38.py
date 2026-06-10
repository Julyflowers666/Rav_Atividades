def inverter_palavras(frase):
    palavra_atual = ""
    resultado = ""

    for caract in frase:
        if caract != " ":
            palavra_atual = caract + palavra_atual
        else:
            resultado += palavra_atual + " "
            palavra_atual = ""

    resultado += palavra_atual

    return resultado

print(inverter_palavras("Olá mundo"))