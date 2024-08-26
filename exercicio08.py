ano_atual = int(input("digite o ano atual: "))
ano_nascimento = int(input("digite o ano de nascimento: "))

idade = ano_atual - ano_nascimento

if idade <= 3:
    print("bebe")
else:
    if idade <= 11:
        print("criança")
    else:
        if idade <= 17:
            print("adolescente")
        else:
            if idade <= 64:
                print("adulto")
            else:
                print("idoso")