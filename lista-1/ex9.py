# 9- Escala Crítica de Plantão Médico: Um hospital fornece uma lista onde cada elemento
# é uma sublista com os dias do mês em que um médico específico pode trabalhar. O
# diretor quer saber qual é o dia do mês que tem a menor cobertura de profissionais.
# Retorno exigido: O dia (número) com a menor quantidade de médicos
# disponíveis e uma lista com os índices (IDs) dos médicos que farão plantão
# nesse dia crítico

escala_medicos = [
    [1, 3, 5, 10, 15, 20],  # Médico 1 
    [2, 4, 6, 12, 18, 24],  # Médico 2 
    [5, 10, 15, 20, 25, 30] # Médico 3 
]

def encontrar_dia_critico(escala_medicos):
    melhor_dia = None
    menor_equipe = None
    for dia in range(1, 32):
        medicos_plantao = []
    
        for id_medico, dias in enumerate(escala_medicos):
            if dia in dias:
                medicos_plantao.append(id_medico)
                
        if len(medicos_plantao) > 0:
            if menor_equipe is None or len(medicos_plantao) < len(menor_equipe):
                menor_equipe = medicos_plantao
                melhor_dia = dia
                
    return melhor_dia, menor_equipe


dia, ids_medicos = encontrar_dia_critico(escala_medicos)

print(f"Dia crítico (menor cobertura): {dia}")
print(f"IDs dos médicos de plantão: {ids_medicos}")

