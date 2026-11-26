# Exercício 3: Contagem Regressiva

# Crie uma função recursiva que receba um número inteiro N 
# e imprima a contagem regressiva de N até 1.

def contagem_regressiva(n):
    if n <= 0:
        return
    else:
        print(n)
        contagem_regressiva(n - 1)

contagem_regressiva(5)