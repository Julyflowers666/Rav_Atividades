total = 0
num = 0
cont =0

while True:
    num = int(input("digite um numero: "))
    total = total + num
    cont = cont + 1
    print (cont)
    
    if total >= 100:
        print (f"resultado da soma: {total}")
        print (f"tentativas feitas: {cont}")
        break