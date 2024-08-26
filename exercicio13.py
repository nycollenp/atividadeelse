ano = int(input("digite o ano: "))
peso = float(input("digite o peso: "))


if ano <= 1970:
    if peso < 1200:
        classe = 1
        taxa_de_registro = 16.50
    else:
        if peso <= 1700:
            classe = 2
            taxa_de_registro = 25.50
        else:
             classe = 3
             taxa_de_registro = 46.50
else:

    if ano <= 1979:
        if peso < 1200:
            classe = 4
            taxa_de_registro = 27.00
        else:
            if peso <= 1700:
                classe = 5
                taxa_de_registro = 30.50
            else:
                classe = 6
                taxa_de_registro = 52.50
    else:

        if ano >= 1980:
            if peso < 1600:
                classe = 7
                taxa_de_registro = 19.50
            else:
                classe = 8
                taxa_de_registro = 55.50
print(classe)
print(taxa_de_registro)
