nome_aluno = input("digite o nome: ")
prova1 = float(input("informe a nota: "))
prova2 = float(input("informe a nota: "))
trabalho = float(input("informe a nota: "))
frequencia = int(input("informe as faltas: "))

media = (prova1 * 3 + prova2 * 5 + trabalho * 2) / 10

if frequencia > 15:
    print("reprovado por falta")
else:
    if media >= 6.0:
        print(media)
        print("aprovado")
    else:
        print(media)
        print("prova final")




