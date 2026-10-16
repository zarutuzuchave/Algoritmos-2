# 7 - Dada a matriz nativa 3x2 `matriz = [[1, 2], [3, 4], [5, 6]]`: (a) Permita que o usuário
# atualize o valor da linha 1, coluna 0 para 99; (b) Escreva uma função que construa e
# retorne a matriz transposta (tamanho 2x3), onde as linhas da matriz original viram
# colunas.

def transpor(matriz):
    transposta = []
    for j in range(2):
        linha = []
        for i in range(3):
            linha.append(matriz[i][j])
        transposta.append(linha)
    return transposta

def processar_matriz():
    matriz = [[1, 2], [3, 4], [5, 6]]

    matriz[1][0] = int(input("Digite o novo valor para a linha 1, coluna 0: "))
    print(matriz)

    matriz_transposta = transpor(matriz)
    print(matriz_transposta)

processar_matriz()