def maior_sequencia(s):
    if not s:
        return ""

    maior_inicio = 0
    maior_tam = 1

    atual_inicio = 0
    atual_tam = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            atual_tam += 1
        else:
            atual_inicio = i
            atual_tam = 1

        if atual_tam > maior_tam:
            maior_tam = atual_tam
            maior_inicio = atual_inicio

    return s[maior_inicio:maior_inicio + maior_tam]

print(maior_sequencia("aabbccdddde"))
print(maior_sequencia("aaabbbcccc"))