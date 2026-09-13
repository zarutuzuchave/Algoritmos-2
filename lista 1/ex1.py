# 1 - Média Móvel: Escreva uma função que receba uma lista de números e um número
# inteiro k (tamanho da janela). A função deve retornar uma lista com as médias de cada
# sublista contígua de tamanho k.

    
lista_num = [10,12,14,15,13]
k = 5
def media_movel(lista_num, k):
    medias_num = []
    for i in range(len(lista_num) - k + 1):
        soma = 0
        for j in range(i, i + k):
            soma = soma + lista_num[j]

        media = soma / k
        medias_num.append(media)

    return medias_num  

resultado = media_movel(lista_num, k)
print(resultado)
