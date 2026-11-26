# 8 - Apuração de Urna Eletrônica: Recebemos uma lista gigantesca embaralhada 
# contendo  os  IDs  dos  candidatos  que  receberam  votos.  O  voto  em  branco  é  o  ID  0.  O 
# sistema não sabe previamente quais são os IDs válidos. 
# Retorno exigido: Uma estrutura em formato de lista de listas (ex: [[id, 
# total_votos], ...]) resumindo a eleição, o ID do candidato vencedor e a 
# porcentagem de votos em branco. 


candidatos_politicos = [
    {
        "numero_urna": 13,
        "nome": "Luiz Inácio Lula da Silva",
        "cargo": "Presidente da República",
        "partido": "PT"
    },
    {
        "numero_urna": 22,
        "nome": "Flávio Bolsonaro",
        "cargo": "Candidato / Cargo Majoritário",
        "partido": "PL"
    },
    {
        "numero_urna": 55,
        "nome": "Ronaldo Caiado",
        "cargo": "Presidente",
        "partido": "PSD"
    },
    {
        "numero_urna": 30,
        "nome": "Romeu Zema",
        "cargo": "Presidente",
        "partido": "NOVO"
    },
    {
        "numero_urna": 40,
        "nome": "Geraldo Alckmin",
        "cargo": "Vice-Presidente",
        "partido": "PSB"
    },
    {
        "numero_urna": 14,
        "nome": "Renan Santos",
        "cargo": "Presidente da República",
        "partido": "Missão"
    }
]

def eleicao(candidatos):
    votos = []
    contador_branco = 0
    
    for _ in range(6):
        inserir_votos = int(input("Digite o número do candidato ou 0 para branco: "))
        votos.append(inserir_votos)
        
        if inserir_votos == 0:
            contador_branco += 1
            print("Voto em branco registrado.")
            continue
            
        encontrou = False
        for candidato in candidatos:
            if candidato["numero_urna"] == inserir_votos:
                print(f"Voto registrado para: {candidato['nome']}, {candidato['partido']}")
                encontrou = True
                break
                
        if not encontrou:
            print("Voto nulo (candidato não encontrado).")

    print("\n--- FIM DA VOTAÇÃO ---")

    ganhador = max(set(votos), key=votos.count)
    total_de_votos = votos.count(ganhador)
    
    if ganhador == 0:
        print(f" Votação anulada! Vote novamente.")
    else:
        nome_ganhador = ""
        for cand in candidatos:
            if cand["numero_urna"] == ganhador:
                nome_ganhador = cand["nome"]
                break
        print(f"O mais votado foi: {nome_ganhador} Número {ganhador} Partido {candidato['partido']}, com {total_de_votos} votos!")
        
    porcentagem = contador_branco * 100 / len(votos)
    print(f"Porcentagem de votos em branco = {porcentagem:.0f}%") 

eleicao(candidatos_politicos)
