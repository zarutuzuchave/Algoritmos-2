# 1 - Escreva um programa em Python que solicite ao usuário a quantidade N de números
# inteiros que deseja cadastrar. Construa uma lista vazia e preencha-a dinamicamente em
# tempo de execução utilizando o método append(). Em seguida, percorra a lista e exiba:
# (a) o maior e o menor valor digitados; (b) a média aritmética dos elementos; e (c) a
# quantidade de números pares

def pedir_num():  
    numeros = int(input("Insira a quantidade de números que deseja cadastrar: "))
    lista = []
    for i in range(numeros):
        num = int(input(f"Digite o {i + 1} número: "))
        lista.append(num)
    if len(lista)> 0:
        maior = lista[0]
        menor = lista[0]
        soma = 0
        pares = 0
        
        
        for numero in lista:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero
                
            soma += numero
            
            if numero % 2 == 0:
                pares += 1 
        media = soma / len(lista)
        
    print(f"Lista cadastrada: {lista}")
    print(f"O maior valor é {maior} e o menor valor é {menor}.")
    print(f"A média dos números é {media:.2f}.")
    print(f"A quantidade de números pares é {pares}.")         
                
pedir_num()