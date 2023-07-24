def calcular_reajuste_salario(salario):
    if salario <= 280:
        percentual_aumento = 0.2
    elif salario <= 700:
        percentual_aumento = 0.15
    elif salario <= 1500:
        percentual_aumento = 0.1
    else:
        percentual_aumento = 0.05

    aumento = salario * percentual_aumento
    novo_salario = salario + aumento

    return percentual_aumento, aumento, novo_salario



salario_atual = float(input("Digite o salário atual do colaborador: "))


percentual, aumento, novo_salario = calcular_reajuste_salario(salario_atual)

print(f"Salário antes do reajuste: R${salario_atual:.2f}")
print(f"Percentual de aumento aplicado: {percentual * 100:.2f}%")
print(f"Valor do aumento: R${aumento:.2f}")
print(f"Novo salário após o aumento: R${novo_salario:.2f}")