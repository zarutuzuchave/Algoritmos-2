# 10 - Decodificador de Sinais de Satélite: Um satélite envia pacotes de dados como uma
# lista de bits (0s e 1s). Um pacote de informação válido é sempre sinalizado pelo padrão
# exato de um 1 seguido imediatamente por dois 0s.
# Retorno exigido: O número total de pacotes válidos detectados e uma lista de
# índices marcando onde cada pacote válido começa.

def contar_bits(bits):
    indices_inicio = []
    
    for i in range(len(bits) - 2):
        if bits[i] == 1 and bits[i+1] == 0 and bits[i+2] == 0:
            indices_inicio.append(i)
            
    total_pacotes = len(indices_inicio)
    return total_pacotes, indices_inicio

transmissao = [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0]

total, indices = contar_bits(transmissao)

print(f"Total de pacotes válidos: {total}")
print(f"Índices de início dos pacotes: {indices}")