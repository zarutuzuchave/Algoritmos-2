# 2 - Dada a lista estática de salários `salarios = [2500.0, 3200.0, 1800.0, 4500.0,
# 2100.0]`: (a) Atualize o salário no índice 2 para 2300.0; (b) Peça ao usuário um valor de
# salário para buscar e verificar se existe na lista usando o operador `in`; (c) Se existir,
# remova-o usando `.remove()`; (d) Extraia e remova o último elemento da lista utilizando
# `.pop()` e exiba o elemento removido.

def processar_salarios():
    salarios = [2500.0, 3200.0, 1800.0, 4500.0, 2100.0]

    salarios[2] = 2300.0

    busca = float(input("Digite o salário para buscar: "))

    if busca in salarios:
        salarios.remove(busca)

    ultimo = salarios.pop()

    print(ultimo)
    print(salarios)

processar_salarios()