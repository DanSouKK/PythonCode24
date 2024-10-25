# Lista de armas
armas = ["espada", "arco longo", "katana", "arco curto", "espada longa", 
         "machado grande", "machado duplo", "cajado", "grimorio", "adaga", 
         "maça", "mangual", "lança curta", "lança longa", "martelo combate", "espada larga"]

armaduras = ["Armadura acolchoada", "Corselete de couro", "Couro batido", "Camisa de cota de Malha", "Gibão de peles",
            "Brunea", "Cota de malha", "Couraça", "Armadura de Gladiador", "Couraça de Bronze", "Cota de talas",
            "Loriga segmentada", "Meia-armadura", "O-Yoroi", "Armadura completa", "Escudo leve", "Escudo pesado",
            "Escudo de corpo"]


# Dicionário para armazenar os valores de ataque e chance de crítico
valores_armas = {
    "espada": {"atk": 10, "crit_chance": 0.15},       # 15% de chance de crítico
    "espada longa": {"atk": 12, "crit_chance": 0.1}, # 10% de chance de crítico
    "espada larga": {"atk": 15, "crit_chance": 0.1},     # 10% de chance de crítico
    "arco longo": {"atk": 8, "crit_chance": 0.15},   # 15% de chance de crítico    
    "arco curto": {"atk": 7, "crit_chance": 0.1},     # 10% de chance de crítico 
    "katana": {"atk": 12, "crit_chance": 0.2},       # 20% de chance de crítico   
    "machado grande": {"atk": 15, "crit_chance": 0.25}, # 25% de chance de crítico
    "machado duplo": {"atk": 14, "crit_chance": 0.2},  # 20% de chance de crítico
    "martelo combate": {"atk": 16, "crit_chance": 0.2}, # 20% de chance de crítico
    "cajado": {"atk": 6, "crit_chance": 0.05},         # 5% de chance de crítico
    "grimorio": {"atk": 9, "crit_chance": 0.1},        # 10% de chance de crítico
    "adaga": {"atk": 5, "crit_chance": 0.3},           # 30% de chance de crítico
    "maça": {"atk": 10, "crit_chance": 0.1},           # 10% de chance de crítico
    "mangual": {"atk": 13, "crit_chance": 0.15},       # 15% de chance de crítico
    "lança curta": {"atk": 7, "crit_chance": 0.1},     # 10% de chance de crítico
    "lança longa": {"atk": 9, "crit_chance": 0.05}    # 5% de chance de crítico 
    
}
# Dicionario para as armaduras e os valores de defesa de cada uma.
valores_armaduras = {
    "Armadura acolchoada": 1,
    "Corselete de couro": 2,
    "Couro batido": 3,
    "Camisa de cota de Malha": 4,
    "Gibão de peles": 3,
    "Brunea": 4,
    "Cota de malha": 5,
    "Couraça": 5,
    "Armadura de Gladiador": 5,
    "Couraça de Bronze": 4,
    "Cota de talas": 6,
    "Loriga segmentada": 6,
    "Meia-armadura": 7,
    "Armadura completa": 10,
    "Escudo leve": 1,
    "Escudo pesado": 2,
    "Escudo de corpo": 4,
}

# Função para exibir os valores de defesa das armaduras
def exibir_armaduras_defesas(armaduras, valores_armaduras):
    for armadura in armaduras:
        defesa = valores_armaduras.get(armadura, "Valor não encontrado")
        print(f"Armadura: {armadura}, Classe de Armadura (CA): {defesa}")

# Chamar a função para exibir as armaduras e suas defesas
exibir_armaduras_defesas(armaduras, valores_armaduras)

# Chamando a função da armadura

# Função para exibir os valores de ataque e chance de crítico
def exibir_armas_com_atk_e_crit(armas, valores_armas):
    for arma in armas:
        stats = valores_armas.get(arma, {"atk": 0, "crit_chance": 0})  # Pega os valores ou retorna 0
        atk = stats["atk"]
        crit_chance = stats["crit_chance"] * 100  # Convertendo para porcentagem
        print(f"Arma: {arma}, ATK: {atk}, Chance de Crítico: {crit_chance:.1f}%")

# Chamando a função da arma
exibir_armas_com_atk_e_crit(armas, valores_armas)

personagem_criado = {
    "nome": "personagem_criado Valente",
    "armadura": None,
    "arma": None,
    "defesa": 0,
    "ataque": 0,
    "crit_chance": 0,
}

# Função para equipar armadura e arma ao personagem_criado
def equipar_personagem_criado(personagem_criado, armadura, arma):
    # Equipar armadura
    if armadura in armaduras:
        personagem_criado["armadura"] = armadura
        personagem_criado["defesa"] = valores_armaduras[armadura]
    
    # Equipar arma
    if arma in valores_armas:
        personagem_criado["arma"] = arma
        personagem_criado["ataque"] = valores_armas[arma]["atk"]
        personagem_criado["crit_chance"] = valores_armas[arma]["crit_chance"]

# Função para exibir os status do personagem_criado
def exibir_status_personagem_criado(personagem_criado):
    crit_chance_percent = personagem_criado["crit_chance"] * 100
    print(f"Nome: {personagem_criado['nome']}")
    print(f"Armadura: {personagem_criado['armadura']} (Defesa: {personagem_criado['defesa']})")
    print(f"Arma: {personagem_criado['arma']} (Ataque: {personagem_criado['ataque']}, Crítico: {crit_chance_percent:.1f}%)")

# Função para escolher armadura
def escolher_armadura():
    print("\nEscolha uma armadura:")
    for i, armadura in enumerate(armaduras, start=1):
        print(f"{i}. {armadura}")
    escolha = int(input("Digite o número da armadura que deseja equipar: ")) - 1
    if 0 <= escolha < len(armaduras):
        return armaduras[escolha]
    else:
        print("Escolha inválida!")
        return None

# Função para escolher arma
def escolher_arma():
    print("\nEscolha uma arma:")
    for i, arma in enumerate(valores_armas.keys(), start=1):
        print(f"{i}. {arma}")
    escolha = int(input("Digite o número da arma que deseja equipar: ")) - 1
    if 0 <= escolha < len(valores_armas):
        return list(valores_armas.keys())[escolha]
    else:
        print("Escolha inválida!")
        return None

# Loop principal
def main():
    # Escolher armadura e arma
    armadura_escolhida = escolher_armadura()
    arma_escolhida = escolher_arma()
    
    # Equipar o personagem_criado
    if armadura_escolhida and arma_escolhida:
        equipar_personagem_criado(personagem_criado, armadura_escolhida, arma_escolhida)

    # Exibir os status do personagem_criado
    exibir_status_personagem_criado(personagem_criado)

# Executar o programa
main()