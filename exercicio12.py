tempo = float(input("informe o tempo que ficou em deposito: "))

if tempo >= 5:
    taxa = 0.95
else:
    if tempo >= 4:
        taxa = 0.90
    else:
        if tempo >= 3:
            taxa = 0.85
        else:
            if tempo >= 2:
                taxa = 0.75
            else:
                if tempo >= 1:
                    taxa = 0.65
                else:
                    taxa = 0.55
print(taxa)

