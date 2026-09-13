# 5 - Controle de Qualidade Agrícola: Uma fazenda colhe maçãs e as classifica pelo peso
# (em gramas). Você receberá a lista de pesos, o peso mínimo para exportação e o peso
# máximo.
# Retorno exigido: Uma lista contendo os pesos aprovados, uma segunda lista com
# os pesos descartados, e a porcentagem de perda da safra (número float).
listaPesoA = []
listasPesosM = []
pesosReprovados = []
def pedirPesos():
    for i in range(2):
        pesosAprovados = int(input("Digite o peso mínimo e máximo em gramas: "))
        listaPesoA.append(pesosAprovados)

    minimoPeso = min(listaPesoA)
    maxPeso = max(listaPesoA)

    for i in range(10):
        inserir = int(input("Digite os pesos das maçãs: "))
        if inserir < minimoPeso:
            print("Peso menor do que o permitido  ")
            pesosReprovados.append(inserir)
        elif inserir > maxPeso:
            print("Peso maior do que o permitido ")
            pesosReprovados.append(inserir)
        else:
            listasPesosM.append(inserir)

    print(f"Pesos aprovados: {listasPesosM}")
    print(f"Pesos Reprovados: {pesosReprovados}")
    porcentagemPerda = len(pesosReprovados) * 100 / 10
    print("Perda da safra:",porcentagemPerda,"%")

    
# resultado = pedirPesos()
print(pedirPesos())

