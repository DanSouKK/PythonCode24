import random
import math

# Exemplos de nome dos inimigos
prefixos = ["Ela", "Ara", "The", "Dro", "Fa", "Mor", "Bar", "Nor", "Gal", "Heru", "Oro", "Ing"]
sufixos = ["dor", "wyn", "las", "iel", "nor", "rok", "mir", "ion", "ar", "rodel", "anar", "izel"]
tipos = ["Goblin", "meio-orc", "Troll", "Esqueleto", "Zumbi", "Ogro"]

# Função para gerar um nome aleatório para o inimigo
def gerar_nome():
    tipo = random.choice(tipos)
    prefixo = random.choice(prefixos)
    sufixo = random.choice(sufixos)
    return f"{tipo} {prefixo}{sufixo}"

# Função para criar um inimigo aleatório
def random_enemy(x=1, y=20):
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
    return {
        "Nome": gerar_nome(),
        "HP": hp_enemy,
        "ATK": atk,
        "DEF": defense,
        "Crit. rate": crit_rate,
        "Taxa de Acerto": accuracy,
        "N/D": nd
    }

# Função para obter os parâmetros de dificuldade do usuário
def obter_dificuldade():
    while True:
        opcao = input("Deseja definir a dificuldade do inimigo? (s/n): ").lower()
        
        if opcao == 's':
            x = int(input("Digite o valor mínimo para o nível de dificuldade (ND) (1-20): "))
            y = int(input("Digite o valor máximo para o nível de dificuldade (ND) (1-20): "))

            # Verifica se os valores são válidos
            if 1 <= x <= 20 and 1 <= y <= 20 and x <= y:
                return x, y
            else:
                print("Os valores devem estar entre 1 e 20 e o mínimo deve ser menor ou igual ao máximo.")
        
        elif opcao == 'n':
            return 1, 20  # Retorna valores padrão se não desejar definir a dificuldade

        else:
            print("Opção inválida, por favor escolha 's' ou 'n'.")

# Gera o inimigo com os valores válidos ou de forma padrão
x, y = obter_dificuldade()
enemy_gerado = random_enemy(x, y)

# Exibe as características do inimigo de forma organizada
print("\nCaracterísticas do Inimigo:")
for chave, valor in enemy_gerado.items():
    print(f"{chave}: {valor}")
