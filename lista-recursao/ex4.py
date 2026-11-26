# Exercício 4: Algoritmo de Euclides (MDC)

# Implemente de forma recursiva o algoritmo de Euclides para calcular 
# o Maior Divisor Comum (MDC) entre dois números inteiros positivos 'a' e 'b'.

def div1(a,b):
    if b == 0:
        return a
    else:
        return div1(b, a % b)

print(div1(48, 18))
