salario_atual = float(input("informe o salario: "))
tempo_servico = int(input("informe o tempo de serviço: "))

salario_reajustado1 = salario_atual * 0.10
salario_reajustado2 = salario_atual * 0.20

if tempo_servico <= 1:
    print(salario_reajustado1 + salario_atual)
else:
    print(salario_reajustado2 + salario_atual)

