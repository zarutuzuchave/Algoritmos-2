# 6 - Sistema de Alerta de Manutenção de Frota: Um ônibus transmite diariamente a
# quilometragem percorrida. Você receberá uma lista com esses trajetos diários e o limite
# de quilometragem para a revisão do motor.
#     Retorno exigido: A quilometragem total acumulada, o dia (índice da lista) em
# que o limite foi ultrapassado, e um booleano (True ou False) indicando se o
# ônibus precisa ser recolhido imediatamente.

km = [26,26,25,22]
limite = [24]
def somaKM(km,limite):
    soma = 0
    limite_valor = limite[0]
    recolher = False
    dia_excedido = 0
    for i in range(len(km)):
        soma += km[i]
        print(f"Dia {i+1} => Quilometragem Total Acumulada: {soma}")    
        if km[i] > limite_valor:
            dia_excedido += 1
            print(f"Limite de km excedido no dia: {i+1} ")
        else:
            print("Continue Rodando")

        if dia_excedido >= 3:
            recolher = True
            print("Frota pescisa ser recolhida imediatamente")
            break

    return recolher
somaKM(km,limite)



            
        

       


