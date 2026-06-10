def gerar_primos(n):
    primos = []

    for num in range(2, n + 1):
        gerar_primo = True

        for i in range(2, num):
            if num % i == 0:
                gerar_primo = False
                break

        if gerar_primo:
            primos.append(num)

    return primos

print(gerar_primos(20))