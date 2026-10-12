# 2 - Um serviço de streaming tem seu catálogo representado por uma lista de tuplas
# (titulo_filme, ano_lancamento, genero, avaliacao_usuarios). Você também receberá
# como parâmetro um genero_alvo (string) e uma nota_corte (float).
# Você deve extrair dados com base em múltiplos parâmetros de entrada e encontrar o
# "menor valor" (mais antigo) dentro de um subconjunto específico.
# Retorno Exigido: Uma lista apenas com os títulos dos filmes que batem com o gênero
# alvo e possuem nota igual ou superior ao corte, e uma tupla com o (titulo_filme,
# ano_lancamento) do filme mais antigo dessa lista filtrada.
# Na Main: Construa uma lista estática com pelo menos 4 filmes misturando gêneros e
# notas. Defina variáveis para o seu gênero alvo e sua nota de corte. Invoque a função e
# imprima a lista final de filmes aprovados, seguida de uma mensagem informando qual é
# o filme mais antigo dentre os que foram filtrados.


def filtrar_filmes(catalogo, genero, nota):
    titulos_aprovados = []
    filme_mais_antigo = " "
    menor_ano = 9999
    
    for titulo, ano, genero, nota in catalogo:
        if genero == genero and nota >= nota:
            titulos_aprovados.append(titulo)
            
            if ano < menor_ano:
                menor_ano = ano
                filme_mais_antigo = titulo
                
    return titulos_aprovados, (filme_mais_antigo, menor_ano)

catalogo_filmes = [
    ("Matrix", 1999, "Ficcao", 8.7),
    ("De Volta para o Futuro", 1985, "Ficcao", 8.5),
    ("Gravidade", 2013, "Ficcao", 7.7),
    ("O Poderoso Chefao", 1972, "Drama", 9.2),
    ("Blade Runner", 1982, "Ficcao", 8.1)
]

alvo = "Ficcao"
corte = 8.0

titulos, mais_antigo = filtrar_filmes(catalogo_filmes, alvo, corte)

print(f"Filmes aprovados: {titulos}")
print(f"O filme mais antigo entre os aprovados é: {mais_antigo[0]} do ano de {mais_antigo[1]}")