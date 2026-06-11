def soma_digitos(num):
    soma = 0

    for digito in str(num):
        soma += int(digito)

    return soma

print(soma_digitos(12345))