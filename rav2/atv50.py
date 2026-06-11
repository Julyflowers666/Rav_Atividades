def multiplicacao(a, b):
    resultado = 0
    negativos = 0

    if a < 0:
        a = -a
        negativos += 1

    if b < 0:
        b = -b
        negativos += 1

    for _ in range(b):
        resultado += a

    if negativos == 1:
        resultado = -resultado

    return resultado


print(multiplicacao(6, 7))
print(multiplicacao(-6, 7))
print(multiplicacao(6, -7))
print(multiplicacao(-6, -7))
print(multiplicacao(0, 5))