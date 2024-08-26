valor1 = int(input("digite o valor1: "))
valor2 = int(input("digite o valor2: "))

soma = valor1 + valor2

if soma < 8:
    media = (valor1 + valor2) / 2
    print(media)
else:
    if soma == 8:
        produto = valor1 * valor2
        print(produto)
    else:
        if valor1 > valor2:
            divisao = valor1 / valor2
        else:
            divisao = valor2 / valor1
        print(divisao)