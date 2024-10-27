# Lista de armas
armas = ["espada curta", "arco longo", "katana", "arco curto", "espada longa", 
         "machado grande", "machado duplo", "cajado", "grimorio", "adaga", "besta leve", "besta pesada", "cimitarra",
         "maça","maça pesada","maça estrela", "mangual", "lança curta", "lança longa", "martelo combate","martelo de guerra", "espada larga"]

armaduras = ["Armadura acolchoada", "Corselete de couro", "Couro batido", "Camisa de cota de Malha", "Gibão de peles",
            "Brunea", "Cota de malha", "Peitoral de aço", "Armadura de Gladiador", "peitoral de Bronze", "Cota de talas",
            "Loriga segmentada", "Meia-armadura","Armadura completa"]
escudos = ["Escudo leve", "Escudo pesado", "Escudo de corpo"]

# Dicionário para armazenar os valores de ataque e chance de crítico
valores_armas = {
    "espada curta": {"atk": 10, "crit_chance": 0.15, "maos": 1},
    "espada longa": {"atk": 12, "crit_chance": 0.1, "maos": 1},
    "espada larga": {"atk": 15, "crit_chance": 0.1, "maos": 2},
    "arco longo": {"atk": 18, "crit_chance": 0.15, "maos": 2},
    "arco curto": {"atk": 14, "crit_chance": 0.1, "maos": 2},
    "katana": {"atk": 12, "crit_chance": 0.2, "maos": 2},
    "machado grande": {"atk": 15, "crit_chance": 0.25, "maos": 2},
    "machado duplo": {"atk": 14, "crit_chance": 0.2, "maos": 2},
    "martelo combate": {"atk": 16, "crit_chance": 0.2, "maos": 1},
    "cajado": {"atk": 6, "crit_chance": 0.05, "maos": 2},
    "grimorio": {"atk": 9, "crit_chance": 0.1, "maos": 1},
    "adaga": {"atk": 5, "crit_chance": 0.3, "maos": 1},
    "maça": {"atk": 10, "crit_chance": 0.1, "maos": 1},
    "maça pesada": {"atk": 14, "crit_chance": 0.15, "maos": 2},
    "maça estrela": {"atk": 13, "crit_chance": 0.15, "maos": 1},
    "mangual": {"atk": 13, "crit_chance": 0.15, "maos": 1},
    "lança curta": {"atk": 7, "crit_chance": 0.1, "maos": 1},
    "lança longa": {"atk": 9, "crit_chance": 0.05, "maos": 2},
    "besta leve": {"atk": 10, "crit_chance": 0.1, "maos": 2},
    "besta pesada": {"atk": 14, "crit_chance": 0.1, "maos": 2},
    "cimitarra": {"atk": 11, "crit_chance": 0.2, "maos": 1},
    "martelo de guerra": {"atk": 17, "crit_chance": 0.15, "maos": 2}
}


# Dicionario para as armaduras e os valores de defesa de cada uma.
valores_armaduras = {
    "Armadura acolchoada": {"defesa": 1, "tipo": "leve"},
    "Corselete de couro": {"defesa": 2, "tipo": "leve"},
    "Couro batido": {"defesa": 3, "tipo": "leve"},
    "Camisa de cota de Malha": {"defesa": 4, "tipo": "leve"},
    "Gibão de peles": {"defesa": 3, "tipo": "media"},
    "Brunea": {"defesa": 4, "tipo": "media"},
    "Cota de malha": {"defesa": 5, "tipo": "media"},
    "Peitoral de aço": {"defesa": 5, "tipo": "media"},
    "Armadura de Gladiador": {"defesa": 5, "tipo": "pesada"},
    "peitoral de Bronze": {"defesa": 4, "tipo": "media"},
    "Cota de talas": {"defesa": 6, "tipo": "pesada"},
    "Loriga segmentada": {"defesa": 6, "tipo": "pesada"},
    "Meia-armadura": {"defesa": 7, "tipo": "pesada"},
    "Armadura completa": {"defesa": 10, "tipo": "pesada"}
}

valores_escudos = {
    "Escudo leve": {"defesa": 1, "tipo": "escudos"},
    "Escudo pesado": {"defesa": 2, "tipo": "escudos"},
    "Escudo de corpo": {"defesa": 4, "tipo": "escudos"}
}


# Função para exibir os valores de defesa das armaduras
def exibir_armaduras_defesas(armaduras, valores_armaduras):
    for armadura in armaduras:
        defesa = valores_armaduras.get(armadura, "Valor não encontrado")
        print(f"Armadura: {armadura}, Classe de Armadura (CA): {defesa}")

# Chamar a função para exibir as armaduras e suas defesas
exibir_armaduras_defesas(armaduras, valores_armaduras)

print("-" * 40)# print para separar linhas

# Função para exibir os valores de defesa das armaduras
def exibir_escudos_defesas(escudos, valores_escudos):
    for escudos in escudos:
        defesa = valores_escudos.get(escudos, "Valor não encontrado")
        print(f"Escudos: {escudos}, Classe de Armadura (CA): {defesa}")

# Chamar a função para exibir as armaduras e suas defesas
exibir_escudos_defesas(escudos, valores_escudos)

print("-" * 40)# print para separar linhas

# Criação de um personagem
equipamentos = {    
    "armadura": None,
    "escudo": None,
    "arma": None,
    "defesa": 0,
    "ataque": 0,
    "crit_chance": 0
}

# Função para equipar armadura e arma ao equipamentos
# Função para equipar armadura e arma ao equipamentos
def equipar_equipamentos(equipamentos, armadura, arma):
    # Equipar armadura
    if armadura in armaduras:
        equipamentos["armadura"] = armadura
        equipamentos["defesa"] = valores_armaduras[armadura]["defesa"]
    
    # Equipar arma
    if arma in valores_armas:
        equipamentos["arma"] = arma
        equipamentos["ataque"] = valores_armas[arma]["atk"]
        equipamentos["crit_chance"] = valores_armas[arma]["crit_chance"]

        # Verificar se a arma é de 1 ou 2 mãos
        if valores_armas[arma]["maos"] == 1:
            escudo_escolhido = equipar_escudo()  # Pergunta se deseja equipar um escudo
            if escudo_escolhido:
                equipamentos["escudo"] = escudo_escolhido
                # Adiciona a defesa do escudo ao valor de defesa total
                equipamentos["defesa"] += valores_escudos[escudo_escolhido]["defesa"]
        else:
            equipamentos["escudo"] = None  # Sem escudo para armas de 2 mãos
            print(f"\n{arma.capitalize()} é uma arma de duas mãos. Não é possível usar escudo.")


# Função para exibir os status do equipamentos
# Função para exibir os status do equipamentos
# Função para exibir os status do equipamentos
def exibir_status_equipamentos(equipamentos):
    crit_chance_percent = equipamentos["crit_chance"] * 100
    print("\nEquipamentos:")
    if equipamentos['armadura']:
        print(f"Armadura: {equipamentos['armadura']} (Defesa: {equipamentos['defesa']})")
    else:
        print("Armadura: Nenhuma")

    if equipamentos.get("escudo"):
        defesa_escudo = valores_escudos[equipamentos['escudo']]["defesa"]
        print(f"Escudo: {equipamentos['escudo']} (Defesa adicional: {defesa_escudo})")
    else:
        print("Escudo: Nenhum")
    
    arma_nome = equipamentos['arma'].capitalize() if equipamentos['arma'] else "Nenhuma"
    print(f"Arma: {arma_nome} (Ataque: {equipamentos['ataque']}, Chance de Crítico: {crit_chance_percent:.0f}%)")




# Função para escolher armadura
def escolher_armadura():
    print("\nVocê deseja usar uma armadura? (s/n)")
    resposta = input().lower()
    if resposta == "s":
        print("\nEscolha uma armadura:")
        for i, armadura in enumerate(armaduras, start=1):
            print(f"{i}. {armadura}")
        escolha = int(input("Digite o número da armadura que deseja equipar: ")) - 1
        if 0 <= escolha < len(armaduras):
            return armaduras[escolha]
        else:
            print("Escolha inválida!")
            return None
    else:
        print("Você optou por não usar uma armadura.")
        return None

# Função para escolher arma
def escolher_arma():
    print("\nEscolha uma arma:")
    for i, arma in enumerate(valores_armas.keys(), start=1):
        print(f"{i}. {arma}")
    escolha = int(input("Digite o número da arma que deseja equipar: ")) - 1
    lista_armas = list(valores_armas.keys())  # Gera uma lista das chaves do dicionário
    if 0 <= escolha < len(lista_armas):
        return lista_armas[escolha]
    else:
        print("Escolha inválida!")
        return None

def equipar_escudo():
    print("\nVocê pode equipar um escudo. Deseja equipar um? (s/n)")
    resposta = input().lower()
    if resposta == "s":
        print("\nEscolha um escudo:")
        for i, escudo in enumerate(valores_escudos.keys(), start=1):
            print(f"{i}. {escudo}")
        escolha = int(input("Digite o número do escudo que deseja equipar: ")) - 1
        if 0 <= escolha < len(valores_escudos):
            return list(valores_escudos.keys())[escolha]
        else:
            print("Escolha inválida!")
            return None
    else:
        print("Você optou por não usar um escudo.")
        return None

# Código principal
armadura_escolhida = escolher_armadura()  # Chamar a função para escolher armadura
arma_escolhida = escolher_arma()  # Chamar a função para escolher arma

# Equipar personagem
equipar_equipamentos(equipamentos, armadura_escolhida, arma_escolhida)

# Exibir status do personagem
exibir_status_equipamentos(equipamentos)