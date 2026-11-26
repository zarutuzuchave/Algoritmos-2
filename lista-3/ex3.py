# 3 - Crie um vetor com 10 números inteiros de 1 a 10. Utilizando a técnica de fatiamento
# (slicing) do Python: (a) Gere uma sublista contendo apenas os elementos localizados
# nos índices pares; (b) Gere uma sublista contendo apenas os números ímpares (por
# valor); (c) Crie uma cópia da lista inteira invertida sem utilizar o método `.reverse()`.

def processar_vetor():
    vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    indices_pares = vetor[::2]
    
    impares = vetor[0:10:2]
    
    invertida = vetor[::-1]

    print(f"Lista original: {vetor}")
    print(f"Apenas os índices pares: {indices_pares}")
    print(f"Apenas os números ímpares (por valor): {impares}")
    print(f"Lista invertida: {invertida}")

processar_vetor()