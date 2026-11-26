# Exercício 1: Soma Recursiva de Lista

# Escreva uma função recursiva que receba uma lista de números inteiros
#  e retorne a soma de todos os seus elementos sem utilizar o comando 'sum()'
#  nem laços 'for/while'.

lista = [1, 2, 3, 4, 5]
def soma_recursiva(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0]+ soma_recursiva(lista[1:])
    
print(soma_recursiva(lista))