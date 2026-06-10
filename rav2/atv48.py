def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def mmc(a, b):
    return abs(a * b) // mdc(a, b)

print(mmc(12, 18))