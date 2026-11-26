# 1 - Uma estufa inteligente possui vários sensores. O microcontrolador envia uma lista
# de tuplas no formato (id_sensor, temperatura, umidade). As regras de segurança dizem
# que a temperatura não pode passar de 35°C e a umidade não pode ficar abaixo de 20%.
# Você precisa rastrear simultaneamente o maior valor de uma variável e o menor de
# outra, enquanto filtra dados.
# Retorno Exigido: Uma lista contendo apenas os id_sensor que dispararam algum
# alarme de perigo, e uma tupla (maior_temperatura, menor_umidade) registrada em todo
# o período.
# Na Main: Crie uma lista simulando pelo menos 4 sensores (certifique-se de forçar pelo
# menos um alerta de temperatura e um de umidade). Chame a função passando essa lista.
# Imprima no terminal quais sensores entraram em alerta e exiba os picos máximos e
# mínimos.

def monitorar_estufa(dados_sensores):
    sensores_alerta = []
    
    maior_temperatura = 0
    menor_umidade = 100
    
    for id_sensor, temperatura, umidade in dados_sensores:
        if temperatura > maior_temperatura:
            maior_temperatura = temperatura
            
        if umidade < menor_umidade:
            menor_umidade = umidade
            
        if temperatura > 35 or umidade < 20:
            if id_sensor not in sensores_alerta:
                sensores_alerta.append(id_sensor)
                
    return sensores_alerta, (maior_temperatura, menor_umidade)


dados = [
    (1, 30.0, 45.0),
    (2, 38.0, 50.0), 
    (3, 25.0, 15.0), 
    (4, 40.0, 10.0)  
]

ids_alerta, picos = monitorar_estufa(dados)

print(f"Sensores em alerta: {ids_alerta}")
print(f"Maior temperatura: {picos[0]}")
print(f"Menor umidade: {picos[1]}")