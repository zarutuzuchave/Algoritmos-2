# 4 - Em um motor gráfico, os obstáculos circulares são uma lista de tuplas (pos_x, pos_y,
# raio). Você recebe também a tupla do jogador (jog_x, jog_y, jog_raio).
# A colisão ocorre se a distância entre os centros (use a soma das diferenças absolutas de
# X e Y como simplificação) for menor que a soma dos raios.
# Retorno Exigido: Um booleano True ou False indicando se o jogador colidiu com
# algum obstáculo e a quantidade exata de obstáculos com os quais ele está colidindo
# simultaneamente.
# Na Main: Defina uma lista com vários obstáculos espalhados pelo mapa e uma variável
# separada para as coordenadas do jogador, forçando uma posição onde ele encoste em
# pelo menos dois obstáculos ao mesmo tempo. Chame a função e exiba uma mensagem
# de status ("Impacto Detectado!" ou "Caminho Livre") e a quantidade de objetos
# atingidos.

def verificar_colisao(obstaculos, jogador):
    qtd_colisoes = 0
    jog_x, jog_y, jog_raio = jogador
    
    for pos_x, pos_y, raio in obstaculos:
        dif_x = jog_x - pos_x
        if dif_x < 0:
            dif_x = -dif_x  
            
        dif_y = jog_y - pos_y
        if dif_y < 0:
            dif_y = -dif_y  
            
        if (dif_x + dif_y) < (jog_raio + raio):
            qtd_colisoes += 1
            
    return qtd_colisoes > 0, qtd_colisoes

obstaculos_mapa = [
    (10, 10, 2),
    (12, 10, 2),
    (30, 30, 5)
]

jogador_atual = (11, 10, 2)

bateu, atingidos = verificar_colisao(obstaculos_mapa, jogador_atual)

if bateu:
    print("Impacto Detectado!")
else:
    print("Caminho Livre")
    
print(f"Objetos atingidos: {atingidos}")