# aluno = {
#     'nome': 'rogerio',
#     'nota': 7
#     }
# print (aluno['nome'])
# print (aluno['nota'])


##adicionando novas chaves e valor
# aluno['nota2'] = 8
# aluno['nota3'] = 6
# print(aluno)


##dicionario vazio 
# aluno = {}
# aluno['nome'] = 'rogério'
# aluno['nota'] = 7
# print(aluno)

# aluno['nota'] = 9
# print(aluno)

##deletar usando del
# del aluno['nota']
# print(aluno)


##retorna chave e valor do dict
# ifms = {'tads': 'python','engenharia_comp': 'c', 'tsi': 'java',}
# print(ifms)

# for key, value in ifms.items():
#     print("\nkey: " + key)
#     print("Value: " + value)

# for curso, linguagem in ifms.items():
#     print(curso.title() + " estuda " + linguagem.title())




##percorre só as chaves
# for curso in ifms.keys():
#     print(curso.title())

# #é o mesmo que pq é o padrão
# for curso in ifms:
#     print(curso.title())



##verifica se tem cursos iguais em dois dict
# ufms = ['tads', 'tsi']
# for curso in ifms.keys():
#     #print(curso.title())
#     if curso in ufms: #poderia ser not in
#         print(curso.title() + ' existe nas duas instituições')


##ordena enquanto percorre
# for curso in sorted(ifms.keys()):
#     print(curso.title())



# ifms = {'tads': 'python', 'engenharia2': 'python', 'engenharia_comp': 'c', 'tsi': 'java',}
# print(ifms)
# print()

# for linguagem in ifms.values():
#     print(linguagem.title())

# print()    

##elimina os q estão repetidos, sendo a primeira ocorrência
# for linguagem in set(ifms.values()):
#     print(linguagem.title())


# aluno = {'nome': 'rogerio', 'nota': 7}
# aluno1 = {'nome': 'ana', 'nota': 9}
# aluno2 = {'nome': 'josé', 'nota': 9}

# alunos = [aluno, aluno1, aluno2]
# for a in alunos:
#     print(a)


# # print()

# alunos= []
# for i in range(10):
#     novo_aluno = {'nome': 'teste', 'nota': 6}
#     alunos.append(novo_aluno)

# print("Total de alunos: " + str(len(alunos)))
# print()

# for a in alunos[:3]:
#     print(a)


# ifms = {
#     'curso': 'tads',
#     'disciplinas': ['algoritmos', 'banco de dados', 'empreendedorismo'],
# }
##percorre a lista dessa chave
# for disc in ifms['disciplinas']:
#     print(disc)


# ifms = {
#     'tads': ['algoritmos', 'banco de dados', 'empreendedorismo'],
#     'inf': ['português', 'matemática', 'química'],
# }

# for curso, disciplinas in ifms.items():
#     print('\n' + curso.title())
#     for d in disciplinas:
#         print('\t' + d.title())


# instituicoes = {
#     'ifms': {
#         'nome_curso': 'tads',
#         'tipo_curso': 'superior',
#     },
#     'ufms': {
#         'nome_curso': 'medicina',
#         'tipo_curso': 'superior',
#     }
# }

# for local, informacoes in instituicoes.items():
#     print("\nLocal: " + local)
#     print("Curso: " + informacoes['nome_curso'])
#     print("Curso: " + informacoes['tipo_curso'])