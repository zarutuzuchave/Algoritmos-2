# 4 - Merge de Listas Ordenadas: Desenvolva uma função que receba duas listas que já
# estão ordenadas de forma crescente. A função deve retornar uma única lista contendo
# todos os elementos de ambas, também ordenada. Não é permitido concatenar e aplicar
# algoritmo de ordenação depois.


def juntar(lista,lista2):
    resultado = []
    while lista and lista2:
        if lista[0] < lista2[0]:
            resultado.append(lista.pop(0))
        else:
            resultado.append(lista2.pop(0))

    resultado = resultado + lista + lista2
    return resultado

lista = [1,2,3,4]
lista2 = [5,6,7,8]
resultado = juntar(lista,lista2)
print(resultado)