# Crie um sistema de cadastro de alunos utilizando dicionários em Python. Para cada aluno, o sistema deverá armazenar seu nome e quatro notas.

# O sistema deverá apresentar um menu de opções para que o usuário possa realizar as seguintes operações:

# -Adicionar um aluno: permitir que o usuário cadastre um novo aluno, informando seu nome e suas quatro notas.
# -Remover um aluno: permitir que o usuário escolha e remova um aluno já cadastrado.
# -Calcular a média de todos os alunos: exibir a média das notas de cada aluno cadastrado.
# -Identificar o aluno com a maior média: informar o nome do aluno que possui a maior média.
# -Exibir todos os alunos: imprimir o nome, as quatro notas e a média de cada aluno cadastrado.
# -Sair do sistema: disponibilizar uma opção para encerrar a execução do programa.

# O programa deverá continuar apresentando o menu e permitindo novas operações até que o usuário escolha a opção de sair.

alunos = {
    "José": [10, 8, 7, 5],
    "Maria": [9, 6, 8, 7],
    "João": [5, 6, 7, 8],
    "Ana": [10, 9, 8, 7]
}

def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    notas = []
    for i in range(4):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)
    alunos[nome] = notas
    print(f"Aluno {nome} adicionado com sucesso!")

def remover_aluno():
    nome = input("Digite o nome do aluno a ser removido: ")
    if nome in alunos:
        del alunos[nome]
        print(f"Aluno {nome} removido com sucesso!")
    else:
        print(f"Aluno {nome} não encontrado.")

def calcular_media():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    for nome, notas in alunos.items():
        media = sum(notas) / len(notas)
        print(f"Média de {nome}: {media:.2f}")

def maior_media():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    melhor_aluno = None
    melhor_media = None

    for nome, notas in alunos.items():
        media = sum(notas) / len(notas)
        if melhor_aluno is None or media > melhor_media:
            melhor_aluno = nome
            melhor_media = media

    print(f"Aluno com a maior média: {melhor_aluno} (Média: {melhor_media:.2f})")

def exibir_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for nome, notas in alunos.items():
        media = sum(notas) / len(notas)
        print(f"Aluno: {nome}, Notas: {notas}, Média: {media:.2f}")

def sair():
    print("Saindo do sistema...")
    exit()

def exibir_menu():
    print("\nMenu de opções:")
    print("1. Adicionar um aluno")
    print("2. Remover um aluno")
    print("3. Calcular a média de todos os alunos")
    print("4. Identificar o aluno com a maior média")
    print("5. Exibir todos os alunos")
    print("6. Sair")

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_aluno()
    elif opcao == "2":
        remover_aluno()
    elif opcao == "3":
        calcular_media()
    elif opcao == "4":
        maior_media()
    elif opcao == "5":
        exibir_alunos()
    elif opcao == "6":
        sair()
    else:
        print("Opção inválida. Tente novamente.")