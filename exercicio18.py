
numero1 = int(input("digite o numero1: "))
numero2 = int(input("digite o numero2: "))
codigo = int(input("digite o codigo: "))

if codigo == 1:
    print(numero1 + numero2)
else:
    if codigo == 2:
        print(numero1 * numero2)
    else:
        if codigo == 3:
            print(numero1 / numero2)
        else:
            print("codigo invalido")

