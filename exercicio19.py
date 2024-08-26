nota = int(input("digite a nota: "))

if nota < 5:
    conceito = "D"
else:
    if nota <= 6:
        conceito = "C"
    else:
        if nota <= 8:
            conceito = "B"
        else:
            if nota <= 10:
                conceito = "A"
print(conceito)

