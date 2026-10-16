#  10 - Um sistema acadêmico armazena as notas de 4 alunos em 3 avaliações através de
# uma matriz NumPy 4x3: (a) Dado a matriz de notas iniciais `notas = np.array([[5.0, 7.5,
# 6.0], [8.0, 9.0, 4.0], [3.5, 5.0, 6.5], [7.0, 6.0, 8.5]])`, calcule e exiba a média final de
# cada aluno; (b) Identifique qual avaliação (coluna) obteve a maior média geral da turma
# usando `np.argmax()`; (c) Aplique um reajuste automático atribuindo a nota mínima
# `6.0` a todas as avaliações com nota inferior a 6.0; (d) Remova a última coluna
# (Avaliação 3) da matriz utilizando `np.delete(..., axis=1)`.

import numpy as np

def processar_sistema():
    notas = np.array([
        [5.0, 7.5, 6.0],
        [8.0, 9.0, 4.0],
        [3.5, 5.0, 6.5],
        [7.0, 6.0, 8.5]
    ])

    medias_alunos = notas.mean(axis=1)
    print(medias_alunos)

    melhor_avaliacao = np.argmax(notas.mean(axis=0))
    print(melhor_avaliacao)

    notas[notas < 6.0] = 6.0
    print(notas)

    notas_finais = np.delete(notas, 2, axis=1)
    print(notas_finais)

processar_sistema()