def remover_duplicados(s):
    res = ""
    for c in s:
        if c not in res:
            res += c
    return res

print(remover_duplicados("banana"))