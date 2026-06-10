def romano_para_inteiro(romano):
    valores = {"I": 1, "V": 5, "X": 10, "L": 50,"C": 100, "D": 500, "M": 1000}

    total = 0

    for i in range(len(romano)):
        atual = valores[romano[i]]

        if i + 1 < len(romano) and atual < valores[romano[i + 1]]:
            total -= atual
        else:
            total += atual

    return total


print(romano_para_inteiro("XIV"))