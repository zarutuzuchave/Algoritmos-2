# 3 - Concatenação Alternada: Desenvolva uma função que receba duas listas (de
# tamanhos possivelmente diferentes) e retorne uma única lista intercalando os elementos
# de ambas até o fim da menor, adicionando o restante da maior ao final.


def listas(list1,list2):
    novaLista = []

    menor = min(len(list1), len(list2))
    maior = max(len(list1), len(list2))

    for i in range(menor):
        novaLista.append(list1[i])
        novaLista.append(list2[i])

    if len(list1) > len(list2):
        for i in range(menor,maior):
            novaLista.append(list1[i])
    else:
        for i in range(menor,maior):
            novaLista.append(list2[i])

    return novaLista

list1 = [12,23,43,5,65]
list2 = [11,13,33,45,55,20]
resultado = listas(list1,list2)
print(resultado)

