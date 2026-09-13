# 2 - Deslocamento (Shift) à Direita: Crie uma função que receba uma lista e um inteiro n.
# A função deve retornar uma nova lista com os elementos deslocados n posições para a
# direita. Os elementos que "saírem" do final devem reaparecer no início.

def shift(lista_num, n):
    novaLista = []
    n = n % len(lista_num)

    for i in range(len(lista_num) - n, len(lista_num)):
        novaLista.append(lista_num[i])
    for i in range(0,len(lista_num) - n):
        novaLista.append(lista_num[i])

    return novaLista
lista_num = [1,2,3,4,5]
n = 3
resultado = shift(lista_num,n)
print(resultado)
