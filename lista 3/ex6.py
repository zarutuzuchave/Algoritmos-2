# 6 - Construa um programa em Python nativo para ler uma matriz 3x3 de inteiros
# digitados pelo usuário: (a) Preencha a matriz utilizando laços aninhados em listas de
# listas (`list[list]`); (b) Imprima a matriz em formato tabular formatado; (c) Exiba os
# elementos da diagonal principal (onde índice da linha i == coluna j) e da diagonal
# secundária (onde i + j == 2).

def criar_matriz():
    matriz = []
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append(int(input("Valor: ")))
        matriz.append(linha)
    return matriz

def mostrar_matriz(matriz):
    print("\nMatriz:")
    for linha in matriz:
        print(linha)

def mostrar_diagonais(matriz):
    principal = [matriz[0][0], matriz[1][1], matriz[2][2]]
    secundaria = [matriz[0][2], matriz[1][1], matriz[2][0]]
    print("\nPrincipal:", principal)
    print("Secundária:", secundaria)

matriz_3x3 = criar_matriz()
mostrar_matriz(matriz_3x3)
mostrar_diagonais(matriz_3x3)