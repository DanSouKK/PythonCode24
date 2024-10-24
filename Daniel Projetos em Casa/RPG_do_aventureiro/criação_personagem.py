import random
import math

#ataque baixo (1,3), ataque medio(4,7), ataque alto(7,10), ataque muito alto(10,15)
#defesa baixo (1,3), defesa medio(3,7), defesa alto(7,10), defesa muito alto(10,15)
#crit rate baixo (1,3), crit rate medio(3,7), crit rate alto(7,10), crit rate o alto(10,15)
#taxa acerto baixo (1,2), taxa acerto medio(3,6), taxa acerto alto(7,9), taxa acerto muito alto(10,12)


prefixos = ["Ela", "Ara", "The", "Dro", "Fa", "Mor", "Bar", "Nor", "Gal","Heru","Oro","Ing"]
sufixos = ["dor", "wyn", "las", "iel", "nor", "rok", "mir", "ion", "ar","rodel","anar","izel"]
tipos = ["Goblin", "Orc", "Troll", "Esqueleto","Zumbi","Ogro"]

def gerar_nome():
    prefixo = random.choice(prefixos)
    sufixo = random.choice(sufixos)
    tipo = random.choice(tipos)  
    return f"{tipo.capitalize()} {prefixo}{sufixo}"


#definindo raça entre humanos, elfos, orc, anao, halflings
def criar_personagem_aleatorio():
    racas = ["humano", "elfo", "orc", "anao", "halfling"]
    raca = input("Escolha sua raça:\n'Humano' - (sem bonus)\n'Elfo' - (-1 CON /-1STR /+3 DEX)\n'Orc' - (+3 CON/+1 STR /-2 DEX)\n'Anao' - (+1 CON /+1 STR /-2 DEX)\n'Halfling' - (-1 CON /-1 STR / +3 DEX)\n").lower()

    if raca not in racas:
        print(f"Raça inválida '{raca}'. Uma raça aleatória será escolhida.")
        raca = random.choice(racas)
    
    # Definindo os atributos com base na raça escolhida
    if raca == "humano": 
        pontos_de_vida = random.randint(50, 100) * 10 
        ataque = random.randint(4, 7) 
        defesa = random.randint(3, 7)
        taxa_acerto = random.randint(3, 6)
        crit_rate = random.randint(3, 7)

    elif raca == "elfo": 
        pontos_de_vida = random.randint(35, 70) * 10 
        ataque = random.randint(1, 3) 
        defesa = random.randint(7, 10) 
        taxa_acerto = random.randint(7, 9) 
        crit_rate = random.randint(7, 10) 

    elif raca == "orc": 
        pontos_de_vida = random.randint(120, 200) *10 
        ataque = random.randint(10, 15)
        defesa = random.randint(1, 3)
        taxa_acerto = random.randint(3, 6)
        crit_rate = random.randint(3, 7)

    elif raca == "anao": 
        pontos_de_vida = random.randint(100, 150) *10
        ataque = random.randint(7, 10)
        defesa = random.randint(7, 10)
        taxa_acerto = random.randint(1, 2)
        crit_rate = random.randint(1, 3)

    elif raca == "halfling": 
        pontos_de_vida = random.randint(30, 60) * 10
        ataque = random.randint(1, 3)
        defesa = random.randint(3, 7)
        taxa_acerto = random.randint(10, 12)
        crit_rate = random.randint(10, 15)

    # Cria um dicionário com as características do personagem
    personagem = {
        "Raça": raca.capitalize(),
        "Pontos de Vida": pontos_de_vida,
        "Ataque": ataque,
        "Defesa": defesa,
        "Taxa de Acerto": taxa_acerto,
        "Taxa de Crítico": crit_rate
    }
    
    return personagem

# Função para criar um inimigo aleatório e seus status
def random_enemy(x=1, y=20): # Valores padrão definidos

    # Garante que x e y estão dentro do intervalo de 1 a 20
    x = max(1, min(x, 20))
    y = max(1, min(y, 20))

    nd = random.randint(x, y)
    hp_enemy = 100 * nd
    atk = random.randint(1, 15) + math.ceil(nd / 2)
    defense = random.randint(1, 15) + math.ceil(nd / 2)
    crit_rate = random.randint(1, 15) + math.ceil(nd / 2)
    accuracy = random.randint(1, 12) + math.ceil(nd / 2)

    # Retorna um dicionário contendo as informações do inimigo
    enemy = {
        "Nome": gerar_nome(),
        "HP": hp_enemy,
        "ATK": atk,
        "DEF": defense,
        "Crit_rate": crit_rate,
        "Taxa de Acerto": accuracy,
        "N/D": nd
    }

    return enemy

