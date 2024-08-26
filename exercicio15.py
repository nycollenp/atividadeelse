numero1 = int(input("digite o numero: "))
numero2 = int(input("digite o numero: "))
numero3 = int(input("digite o numero: "))
numero4 = int(input("digite o numero: "))

if numero1 <= numero2:
    if numero1 <= numero3:
        if numero1 <= numero4:
            print(numero1)
        else:
            print(numero4)
    else:
        if numero3 <= numero4:
            print(numero3)
        else:
            print(numero4)
else:
    if numero2 <= numero3:
        if numero2 <= numero4:
            print(numero2)
        else:
            print(numero4)
    else:
        if numero3 <= numero4:
            print(numero3)
        else:
            print(numero4)