def eh_numero_perfeito(n):
    soma = 0

    for i in range(1, n):
        if n % i == 0:
            soma += i

    return soma == n

print(eh_numero_perfeito(6))
print(eh_numero_perfeito(28))
print(eh_numero_perfeito(12))