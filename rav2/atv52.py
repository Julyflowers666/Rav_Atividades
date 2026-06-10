def eh_anagrama(str1, str2):
    if len(str1) != len(str2):
        return False

    contagem = {}

    for letra in str1:
        if letra in contagem:
            contagem[letra] += 1
        else:
            contagem[letra] = 1

    for letra in str2:
        if letra not in contagem:
            return False
        contagem[letra] -= 1

    for valor in contagem.values():
        if valor != 0:
            return False

    return True

print(eh_anagrama("amor", "roma"))
print(eh_anagrama("python", "java"))