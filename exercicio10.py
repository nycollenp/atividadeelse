salario = float(input("informe o salario: "))
financiamento = float(input("informe o financiamento: "))

if financiamento <= (5 * salario):
    print("financiamento concedido")
else:
    print("financiamento negado")
