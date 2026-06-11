def soma_divisores_proprios(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    return soma

def sao_amigos(a, b):
    return soma_divisores_proprios(a) == b and soma_divisores_proprios(b) == a

print(sao_amigos(220, 284))
print(sao_amigos(1184, 1210))
print(sao_amigos(30, 42))