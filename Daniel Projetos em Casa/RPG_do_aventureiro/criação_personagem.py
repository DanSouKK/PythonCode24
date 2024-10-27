import random

#pontos de vida baixo (35, 70),#pontos de vida mexio (70, 100), #pontos de vida alto (100, 150),#pontos de vida muito alto (150, 200),
#ataque baixo (1,3), ataque medio(4,7), ataque alto(7,10), ataque muito alto(10,15)
#defesa baixo (1,3), defesa medio(3,7), defesa alto(7,10), defesa muito alto(10,15)
#crit rate baixo (1,3), crit rate medio(3,7), crit rate alto(7,10), crit rate o alto(10,15)
#taxa acerto baixo (1,2), taxa acerto medio(3,6), taxa acerto alto(7,9), taxa acerto muito alto(10,12)
#magia baixa(1, 3), magia medio(4,7), magia alto(7,10), magia muito alta(10,15)
#defesa magica baixa(1, 3),defesa magica medio(4,7),defesa magica alto(7,10),defesa magica muito alta(10,15)


#função geradora de dados
def rolar_d6():
    dados = [random.randint(1, 6) for _ in range(4)]
    dados.remove(min(dados))
    return sum(dados)

#função geradora de atributos para os personagens e inimigos.
def gerar_atributos():
    atributos_base = [rolar_d6() for _ in range(4)]
    print(f"Valores de atributos disponíveis para distribuição: {atributos_base}")
    return atributos_base

#função principal da criação do personagem.
def criar_personagem_aleatorio():
    racas = ["humano", "elfo", "meio-orc", "anao", "anao da terra", "halfling", "drow", "elfo do sol", "wood elf"]
    print("STR - Força: Aumenta o ataque físico\nDEX - Destreza: Aumenta taxa de acerto e crítico\nCON - Constituição: Aumenta pontos de vida e defesa física\nINT - Inteligência: Aumenta magia e defesa mágica")
    
    # Loop para garantir que o jogador escolha uma raça válida
    while True:
        raca = input(
            "\nEscolha sua raça:\n"
            "'Humano' - (sem bônus)\n"
            "'Elfo' - (-2 CON / +2 DEX)\n"
            "'Meio-orc' - (+3 STR / -3 INT)\n"
            "'Anao' - (+2 CON / -2 INT)\n"
            "'Anao da Terra' - (+2 CON / +2 STR / -2 DEX / -2 INT)\n"
            "'Halfling' - (+2 DEX / -2 STR)\n"
            "'Drow' - (-2 CON / +2 DEX)\n"
            "'Elfo do Sol' - (+2 INT / -2 CON)\n"
            "'Wood Elf' - (+2 STR / +2 DEX / -2 CON / -2 INT)\n"
        ).lower()  

        # Verifica se a raça escolhida é válida
        if raca in racas:
            print(f"\nRaça escolhida: {raca.capitalize()}")
            break  # Sai do loop se a raça for válida
        else:
            print(f"Raça inválida '{raca}'. Escolha novamente.")
    
    valores_atributos = gerar_atributos()
    
    # Distribuição dos valores para STR, DEX, CON, INT
    atributos = {}
    for atr in ["STR", "DEX", "CON", "INT"]:
        while True:
            try:
                valor = int(input(f"Escolha um valor para {atr}: "))
                if valor in valores_atributos:
                    atributos[atr] = valor
                    valores_atributos.remove(valor)
                    break
                else:
                    print("Valor inválido, escolha um valor disponível.")
            except ValueError:
                print("Por favor, insira um número válido.")
    
    # Aplicadores de modificadores raciais aos atributos
    if raca == "elfo":
        atributos["CON"] -= 2
        atributos["DEX"] += 2
    elif raca == "meio-orc":
        atributos["STR"] += 3
        atributos["INT"] -= 3
    elif raca == "anao":
        atributos["CON"] += 2
        atributos["INT"] -= 2
    elif raca == "anao da terra":
        atributos["STR"] += 2
        atributos["CON"] += 2
        atributos["DEX"] -= 2
        atributos["INT"] -= 2
    elif raca == "halfling":
        atributos["DEX"] += 2
        atributos["STR"] -= 2
    elif raca == "drow":
        atributos["CON"] -= 2
        atributos["DEX"] += 2
    elif raca == "elfo do sol":
        atributos["INT"] += 2
        atributos["CON"] -= 2
    elif raca == "wood elf":
        atributos["STR"] += 2
        atributos["DEX"] += 2
        atributos["CON"] -= 2
        atributos["INT"] -= 2
    
    # Status iniciais baseados na raça
    if raca == "humano":
        pontos_de_vida = random.randint(70, 100) * 10 
        ataque = random.randint(4, 7)
        defesa = random.randint(4, 7)
        magia = random.randint(4, 7)
        defesa_magica = random.randint(3, 7)
        taxa_acerto = random.randint(3, 6)
        crit_rate = random.randint(3, 6)
        
    
    elif raca == "elfo":
        pontos_de_vida = random.randint(35, 70) * 10
        ataque = random.randint(1, 3)
        defesa = random.randint(3, 6)
        magia = random.randint(7, 10)
        defesa_magica = random.randint(7, 10)
        taxa_acerto = random.randint(7, 9)
        crit_rate = random.randint(7, 9)
        

    elif raca == "meio-orc":
        pontos_de_vida = random.randint(150, 200) * 10
        ataque = random.randint(10, 15)
        defesa = random.randint(1, 3)
        magia = random.randint(1, 3)
        defesa_magica = random.randint(1, 3)
        taxa_acerto = random.randint(3, 6)
        crit_rate = random.randint(3, 6)
        

    elif raca == "anao":
        pontos_de_vida = random.randint(100, 150) * 10
        ataque = random.randint(7, 10)
        defesa = random.randint(7, 10)
        magia = random.randint(1, 3)
        defesa_magica = random.randint(4, 7)
        taxa_acerto = random.randint(1, 3)
        crit_rate = random.randint(1, 3)
        

    elif raca == "halfling":
        pontos_de_vida = random.randint(30, 60) * 10
        ataque = random.randint(1, 3)
        defesa = random.randint(3, 7)
        magia = random.randint(4, 7)
        defesa_magica = random.randint(1, 3)
        taxa_acerto = random.randint(10, 12)
        crit_rate = random.randint(10, 15)
        

    elif raca == "drow":
        pontos_de_vida = random.randint(35, 70) * 10
        ataque = random.randint(1, 3)
        defesa = random.randint(7, 10)
        magia = random.randint(10, 15)
        defesa_magica = random.randint(7, 10)
        taxa_acerto = random.randint(7, 9)
        crit_rate = random.randint(7, 10)
        

    elif raca == "elfo do sol":
        pontos_de_vida = random.randint(35, 70) * 10
        ataque = random.randint(1, 3)
        defesa = random.randint(7, 10)
        magia = random.randint(10, 15)
        defesa_magica = random.randint(7, 10)
        taxa_acerto = random.randint(7, 9)
        crit_rate = random.randint(7, 10)
        

    elif raca == "wood elf":
        pontos_de_vida = random.randint(35, 70) * 10
        ataque = random.randint(1, 3)
        defesa = random.randint(7, 10)
        magia = random.randint(10, 15)
        defesa_magica = random.randint(7, 10)
        taxa_acerto = random.randint(7, 9)
        crit_rate = random.randint(7, 10)
        

    # Cálculo dos status finais com base nos atributos
    pontos_de_vida += atributos["CON"] * 5
    ataque += atributos["STR"]
    defesa += atributos["CON"]
    magia += atributos["INT"]
    defesa_magica += atributos["INT"]
    taxa_acerto += atributos["DEX"]
    crit_rate += max(1, atributos["DEX"] // 2)  # Garantir que crit rate não fique menor que 1
    nivel = 1
    exp = 0

     
    # Criação do personagem
    personagem = f"""
    ===========================
           Personagem Gerado   
    ===========================    
    Raça: {raca.capitalize()}
    Atributos:
      STR: {atributos["STR"]}
      DEX: {atributos["DEX"]}
      CON: {atributos["CON"]}
      INT: {atributos["INT"]}
    Status:
      Pontos de Vida: {pontos_de_vida}
      Ataque: {ataque}
      Defesa: {defesa}
      Ataque Magia: {magia}
      Defesa Mágica: {defesa_magica}
      Taxa de Acerto: {taxa_acerto}
      Crítico: {crit_rate}
    ===========================
    Level do personagem: {nivel}
    Pontos de Experiencia: {exp}
    """
    
    print(personagem)
#exemplo de chamada do codigo de criação do personagem...
criar_personagem_aleatorio()

