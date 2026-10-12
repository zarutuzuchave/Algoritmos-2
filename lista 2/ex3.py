# 3 - O sistema do caixa gera um recibo na forma de uma lista de tuplas (codigo_produto,
# quantidade, preco_unitario).
# Você deve multiplicar valores internos da tupla para criar dados novos (valor total do
# item), acumular um montante geral e guardar o registro do maior valor calculado.
# Retorno Exigido: O valor total da compra e uma tupla (codigo_produto,
# valor_total_do_item) representando exclusivamente o item que teve o maior custo
# absoluto na nota fiscal.
# Na Main: Monte uma lista de tuplas representando o "carrinho" de um cliente com 3 ou
# mais itens diferentes. Execute a função recebendo os retornos e imprima no terminal o
# valor total da nota fiscal (formatado com R$ e duas casas decimais) e os detalhes do
# produto que saiu mais caro na conta final.
def processar_recibo(carrinho):
    total_compra = 0
    maior_custo= 0
    codigo_caro = ""
    
    for codigo, quantidade, preco in carrinho:
        custo_item = quantidade * preco
        total_compra += custo_item
        
        if custo_item > maior_custo:
            maior_custo = custo_item
            codigo_caro = codigo
            
    return total_compra, (codigo_caro, maior_custo)

carrinho_cliente = [
    ("001", 3, 15.00),
    ("002", 1, 50.00),
    ("003", 5, 12.00),
    ("004", 2, 8.50)  
]

total, mais_caro = processar_recibo(carrinho_cliente)

print(f"Valor total da nota fiscal: R$ {total:.2f}")
print(f"Produto mais caro na conta: Código {mais_caro[0]} total: R$ {mais_caro[1]:.2f}")