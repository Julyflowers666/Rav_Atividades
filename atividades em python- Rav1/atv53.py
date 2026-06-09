def gratificacao(salario, mes):

    if mes >= 1 and mes <= 5:
        return salario * 0.30

    elif mes >= 6 and mes <= 11:
        return salario * 0.40

    elif mes == 12:
        return salario * 0.60

    else:
        return 0


salario = float(input("Digite o salário básico: "))
mes = int(input("Digite o mês (1 a 12): "))

valor = gratificacao(salario, mes)

salario_final = salario + valor

print(f"Gratificação: R$ {valor:.2f}")
print(f"Salário final: R$ {salario_final:.2f}")