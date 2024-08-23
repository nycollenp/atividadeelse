horas_trabalhadas = int(input("informe o numero de horas: "))


if horas_trabalhadas <= 40:
    salario = horas_trabalhadas * 15.00
    print(salario)
else:
    salario = 600.00 + (horas_trabalhadas - 40) * 21.00
    print(salario)
